import requests,bs4,re
import urllib.parse

def searchGoogle(text,start=0):
    searches = []
    html_code = str(requests.get(f"https://www.google.com/search?start={10*start}&q={text}").text)
    if ("Our systems have detected unusual traffic from your computer network." in html_code):
        return 0
    if ("Your search -" in html_code) and ("- did not match any documents." in html_code):
        return None
    soup = bs4.BeautifulSoup(html_code,'html.parser')
    searches += [
        {
            "title": search.getText(),
            "link": getlink(search),
        }
        for search in soup.find_all('h3')
    ]
    return searches if searches != [] else None

def Alink(link):
    link = str(link["href"])
    Qurl_match = re.match(r"^\/url\?q=(?P<url>[\s\S]*)&sa=([\s\S]*)&ved=([\s\S]*)&usg=([\s\S]*)$",link)
    if Qurl_match != None:
        return urllib.parse.unquote(Qurl_match.group("url"))
    Surl_match = re.match(r"^\/search([\s\S]*)$",link)
    if Surl_match != None:
        return urllib.parse.unquote(f"https://google.com{link}")
    return 

def getlink(search):
    if search.find("a") != None:
        return Alink(search.find("a"))
    p = search
    while True:
        p = p.parent
        if p == None:
            break
        elif p.name == "a":
            return Alink(p)
    return
