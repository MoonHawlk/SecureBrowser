from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class Browser(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Secure Browser')
        self.create_layout()
        
    def create_layout(self):
        self.web_view = QWebEngineView()
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.load_url)
        self.back_button = QPushButton('<')
        self.back_button.clicked.connect(self.web_view.back)
        self.forward_button = QPushButton('>')
        self.forward_button.clicked.connect(self.web_view.forward)
        self.refresh_button = QPushButton('Refresh')
        self.refresh_button.clicked.connect(self.web_view.reload)
        
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.back_button)
        button_layout.addWidget(self.forward_button)
        button_layout.addWidget(self.refresh_button)
        
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.url_bar)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.web_view)
        self.setLayout(main_layout)
        
    def load_url(self):
        url = self.url_bar.text()
        self.web_view.load(QUrl(url))
    
if __name__ == '__main__':
    app = QApplication([])
    browser = Browser()
    browser.show()
    app.exec_()
