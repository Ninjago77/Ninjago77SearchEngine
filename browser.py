# importing required libraries
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
import argparse
import sys

# creating main window class
class MainWindow(QMainWindow):

    # constructor
    def __init__(self, url, title=None):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(url))
        if title != None:
            self.setWindowTitle(f"URL Viewer - {title}")
        else:
            self.setWindowTitle("URL Viewer")
        self.setCentralWidget(self.browser)
        self.showMaximized()
        
        # self.setFocus(True)
        # self.activateWindow()
        # self.raise_()
        self.show()
# os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--enable-logging --log-level=3"

parser = argparse.ArgumentParser(
    prog = "URL Viewer",
    description = "Opens a URL",
    epilog = "URL Viewer",
)
parser.add_argument("url",
    help="URL of Webpage",
)
parser.add_argument("-t", "--title",
    help="Set Window's Title",
    required=False,
)
args = parser.parse_args()
app = QApplication(sys.argv)
app.setApplicationName("URL Viewer")
window = MainWindow(url=args.url,title=args.title)
app.exec_()
# def open_in_browser(url,title=None):
#     app = QApplication(sys.argv)
#     app.setApplicationName("URL Viewer")
#     window = MainWindow(url=url,title=title)
#     app.exec_()
