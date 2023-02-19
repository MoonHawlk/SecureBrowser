from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QToolBar, QLineEdit, QComboBox, QSizePolicy
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
import sys

class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Secure Browser")
        self.setWindowIcon(QIcon("icon.png"))
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://google.com"))
        self.setCentralWidget(self.browser)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        self.toolbar = QToolBar("Navigation")
        self.addToolBar(self.toolbar)

        back_button = QAction(QIcon("back.png"), "Back", self)
        back_button.triggered.connect(self.browser.back)
        self.toolbar.addAction(back_button)

        forward_button = QAction(QIcon("forward.png"), "Forward", self)
        forward_button.triggered.connect(self.browser.forward)
        self.toolbar.addAction(forward_button)

        refresh_button = QAction(QIcon("refresh.png"), "Refresh", self)
        refresh_button.triggered.connect(self.browser.reload)
        self.toolbar.addAction(refresh_button)

        self.favorite_bar = QComboBox()
        self.favorite_bar.setFixedWidth(150)
        self.favorite_bar.setMinimumContentsLength(20)
        self.favorite_bar.addItems(["Google", "DuckGo", "Brave", "GitHub"])
        self.favorite_bar.currentIndexChanged.connect(self.navigate_to_favorite)
        self.toolbar.addWidget(self.favorite_bar)

        self.toolbar.addWidget(self.url_bar)

    def navigate_to_url(self):
        url = QUrl(self.url_bar.text())
        self.browser.setUrl(url)

    def navigate_to_favorite(self, index):
        favorite = self.favorite_bar.currentText()
        if favorite == "Google":
            self.browser.setUrl(QUrl("http://google.com"))
        elif favorite == "Brave":
            self.browser.setUrl(QUrl("https://brave.com/pt-br/"))
        elif favorite == "DuckGo":
            self.browser.setUrl(QUrl("https://duckduckgo.com/"))
        elif favorite == "GitHub":
            self.browser.setUrl(QUrl("https://github.com/MoonHawlk"))
        else:
            pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser_window = BrowserWindow()
    browser_window.show()
    sys.exit(app.exec_())
