from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon, QClipboard
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QToolBar, QLineEdit, QComboBox, QSizePolicy, QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
import sys

class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("0x7Br Secure Browser")
        self.setWindowIcon(QIcon("assets/icon.png"))
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://google.com"))
        self.setCentralWidget(self.browser)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        self.toolbar = QToolBar("Navigation")
        self.url_bar.setPlaceholderText(f"Put the full link here:")
        
        self.addToolBar(self.toolbar)

        browser_info_button = QAction(QIcon("assets/browserinfo.png"), "Browser Info", self)
        browser_info_button.triggered.connect(self.browser_info)
        self.toolbar.addAction(browser_info_button)
        
        back_button = QAction(QIcon("assets/back.png"), "Back", self)
        back_button.triggered.connect(self.browser.back)
        self.toolbar.addAction(back_button)

        forward_button = QAction(QIcon("assets/forward.png"), "Forward", self)
        forward_button.triggered.connect(self.browser.forward)
        self.toolbar.addAction(forward_button)

        refresh_button = QAction(QIcon("assets/refresh.png"), "Refresh", self)
        refresh_button.triggered.connect(self.browser.reload)
        self.toolbar.addAction(refresh_button)

        self.favorite_bar = QComboBox()
        self.favorite_bar.setFixedWidth(150)
        self.favorite_bar.setMinimumContentsLength(20)
        self.favorite_bar.addItems(["Google", "DuckGo", "Brave", "Youtube", "GitHub"])
        self.favorite_bar.currentIndexChanged.connect(self.navigate_to_favorite)
        self.toolbar.addWidget(self.favorite_bar)

        self.toolbar.addWidget(self.url_bar)

        self.url_copy_bar = QLineEdit()
        self.url_copy_bar.setFixedWidth(250)
        self.url_copy_bar.setPlaceholderText(f"To Copy URL press enter here!")
        self.url_copy_bar.returnPressed.connect(self.copy_current_url)
        
        self.toolbar.addWidget(self.url_copy_bar)

    def navigate_to_url(self):
        url = QUrl(self.url_bar.text())
        self.update_url()
        self.browser.setUrl(url)

    def navigate_to_favorite(self, index):
        favorite = self.favorite_bar.currentText()
        if favorite == "Google":
            self.browser.setUrl(QUrl("http://google.com"))
        elif favorite == "Brave":
            self.browser.setUrl(QUrl("https://brave.com/pt-br/"))
        elif favorite == "DuckGo":
            self.browser.setUrl(QUrl("https://duckduckgo.com/"))
        elif favorite == "Youtube":
            self.browser.setUrl(QUrl("https://www.youtube.com/"))
        elif favorite == "GitHub":
            self.browser.setUrl(QUrl("https://github.com/MoonHawlk"))
        else:
            pass

    def copy_current_url(self):
        clipboard = QApplication.clipboard()
        url = self.browser.url().toString()
        clipboard.setText(url)
        QMessageBox.information(self, "URL Copied!", f"Copied URL is: {url}")
   
    def browser_info(self):
        browser_name = "0x7Br Secure Browser"
        version = "3.0.0"
        staff = "Filipe Moreno ( MoonHawlk )"
        QMessageBox.information(self, "Browser info", f"Browser name is: {browser_name}\nBrowser version is: {version}\nStaff members are: {staff}")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser_window = BrowserWindow()
    browser_window.show()
    sys.exit(app.exec_())
