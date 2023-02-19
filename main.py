from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QToolBar, QLineEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
import sys

class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Browser")
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

        self.toolbar.addWidget(self.url_bar)

    def navigate_to_url(self):
        url = QUrl(self.url_bar.text())
        self.browser.setUrl(url)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser_window = BrowserWindow()
    browser_window.show()
    sys.exit(app.exec_())
