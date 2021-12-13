from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.browser = QWebEngineView()
        self.url = 'https://duckduckgo.com'
        self.browser.setUrl(QUrl(self.url))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navigation bar
        navigation_bar = QToolBar()
        self.addToolBar(navigation_bar)

        # back
        back = QAction('Go Back',self)
        back.triggered.connect(self.browser.back)
        navigation_bar.addAction(back)

        # front
        front = QAction('Forward',self)
        front.triggered.connect(self.browser.forward)
        navigation_bar.addAction(front)

        # reload
        reload = QAction('Reload', self)
        reload.triggered.connect(self.browser.reload)
        navigation_bar.addAction(reload)

        # home
        home = QAction('Home', self)
        home.triggered.connect(self.go_home)
        navigation_bar.addAction(home)

        # url bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.goto_url)
        navigation_bar.addWidget(self.url_bar)

        # change in url
        self.browser.urlChanged.connect(self.update_url)

    def go_home(self):
        self.browser.setUrl(QUrl(self.url))

    def goto_url(self):
        url = self.url_bar.text()
        if 'https://' not in url:
            url = 'https://' + str(url)
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(str(q))


app = QApplication(sys.argv)
QApplication.setApplicationName('Python Browser')
window = Window()
app.exec_()
