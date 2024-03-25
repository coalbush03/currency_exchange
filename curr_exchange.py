import requests
import sys
from PyQt5.QtGui import QPalette, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QListWidget, QLineEdit, QHBoxLayout, QMainWindow
class curr_converter(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Currency Converter")
        self.setStyleSheet("background-color: #58A4B0;")
        self.setFixedWidth(300)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)



#load api
# url = 'https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_ybAM6h8asWboJSTGOSUy9TLPda85XRCXKRst6SoX'
# response = requests.get(url)
# data = response.json()
# print(data['data']['PLN'])

if __name__== "__main__":
  application=QApplication(sys.argv) 
  win= curr_converter()
  win.show()
  sys.exit(application.exec_())