import shlex,subprocess,flet,flet.theme
import search as searcher

class SearchLink(flet.ListTile):
    def __init__(self, title, url):
        self.url = url
        self.searchTitle = title
        super().__init__(leading=flet.Icon(flet.icons.OPEN_IN_BROWSER,color=flet.colors.BLUE_900), title=flet.Text(self.searchTitle,color=flet.colors.BLUE_900), subtitle=flet.Text(self.url), on_click=self.head_to_link)
    
    def head_to_link(self,event):
        global isWeb,page_launch_url
        if isWeb == True:
            page_launch_url(url=self.url,web_window_name="_blank")
        else:
            subprocess.call(shlex.split(f'python browser.py -t"{self.searchTitle}" "{self.url}"'))

class SearchTab(flet.Tab):
    def __init__(self, tabs, searchText, content):
        self.tabs = tabs
        super().__init__(
            content=content,
            tab_content=flet.Row(
            [
                flet.Text(searchText,color=flet.colors.BLUE_900),
                flet.IconButton(flet.icons.CLOSE, icon_color=flet.colors.BLUE_900, on_click=self.deleteTab),
            ]),
        )
    
    def deleteTab(self,event):
        index = None
        for i,tab in enumerate(self.tabs.tabs):
            if tab == self:
                index = i
        if index != None:
            self.tabs.tabs.pop(index)
            self.tabs.update()




def main(page: flet.Page):
    page.title = "Titus Search Engine"
    page.scroll = True
    # page.window_maximized = True
    page.vertical_alignment = flet.MainAxisAlignment.START
    page.theme_mode = "light"
    # page.window_bgcolor = flet.colors.RED
    page.bgcolor = flet.colors.CYAN_100

    global isWeb,page_launch_url
    isWeb = bool(page.web)
    page_launch_url = page.launch_url

    TABS = flet.Tabs(
        tabs=[],
        selected_index=0,
        animation_duration=100,
    )

    def createTab(title, content):
        TABS.tabs.append(
            SearchTab(TABS, title, content)
        )
        TABS.selected_index = len(TABS.tabs)-1
        TABS.update()

    searchBar = flet.TextField(
        label="Search",
        hint_text="Type to Search",
        expand=True,
        border_color=flet.colors.BLUE_900,
        color=flet.colors.BLUE_900,
        hint_style=flet.TextStyle(color=flet.colors.BLUE_900),
        cursor_color=flet.colors.BLUE_900,
        label_style=flet.TextStyle(color=flet.colors.BLUE_900),
    )
    
    def search():
        title = searchBar.value
        listofsearches = flet.ListView(
            expand=True,
            horizontal=False,
            auto_scroll=False,
            controls=[]
            
        )
        createTab(
            title=title,
            # content=flet.Column(controls=[
            #     listofsearches
            # ])
            content=listofsearches,
        )
        i = 0
        while True:
            iter_search = searcher.searchGoogle(title,i)
            if iter_search == 0:
                listofsearches.controls += [flet.ListTile(
                    leading=flet.Icon(flet.icons.ERROR,color=flet.colors.BLUE_900), title=flet.Text("Google Blocked Me :(",color=flet.colors.BLUE_900), subtitle=flet.Text("Google found out I'm a Robot! They will unblock me in a few minutes; Just wait..."),
                )]
                listofsearches.update()
                break
            if iter_search == None:
                break
            listofsearches.controls += [SearchLink(search["title"],search["link"]) for search in iter_search if search["link"] != None] 
            listofsearches.update()
            i += 1

    
    searchBar.on_submit = lambda e: search()

    page.add(
        flet.Row(alignment=flet.MainAxisAlignment.SPACE_BETWEEN,controls=[
            flet.Text("App made by Shanvanth Arunmozhi",color=flet.colors.BLUE_900),
            flet.Text("Logo made by Titus Kishore Kumar",color=flet.colors.BLUE_900),
        ]),
        flet.Divider(color=flet.colors.BLUE_900),
        flet.Row(controls=[
            flet.Container(padding=flet.padding.only(left=25),content=flet.Image(
                src_base64=r"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",
                width=100,
                height=100,
            )),
            searchBar,
            flet.IconButton(
                icon_color=flet.colors.BLUE_900,
                icon=flet.icons.SEARCH,
                on_click=lambda e: search(),
            ),
        ]),
        TABS,
    )

if __name__ == "__main__":
    if False:
        flet.app(target=main)
    else:
        # flet.app(target=main, view=flet.WEB_BROWSER, port=int(80))
        flet.app(target=main, view=None, port=int(80), assets_dir="assets")