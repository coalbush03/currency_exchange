import requests
import sys
from PyQt5.QtGui import QPalette, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QListWidget, QLineEdit, QHBoxLayout, QMainWindow
class curr_converter(QWidget):
    def __init__(self, curr_data, curr_list):   #curr data do converta
        super().__init__()
        self.setWindowTitle("Currency Converter")
        self.setStyleSheet("background-color: #58A4B0;")
        self.setFixedWidth(400)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        lists = self.lists(curr_list)
        inputs = self.input_fields()
        self.layout.addLayout(lists)
        self.layout.addLayout(inputs)

    def lists(self, curr_list):  #listy horyznotalnie - zrobic rozwijane (?)
        from_list = QListWidget()
        from_list.setStyleSheet("background-color: #BAC1B8; color: black; border-radius:5px;")
        from_list.addItems(curr_list)
        to_list = QListWidget()
        to_list.setStyleSheet("background-color: #BAC1B8; color: black; border-radius:5px;")
        to_list.addItems(curr_list)
        layout = QHBoxLayout()
        layout.addWidget(from_list)
        layout.addWidget(to_list)
        return layout

    def input_fields(self):   #inputy horyzontalnie
        input_field = QLineEdit()
        input_field.setStyleSheet("background-color: #BAC1B8; color: black; border-radius:5px;")
        output_field = QLineEdit()
        output_field.setStyleSheet("background-color: #BAC1B8; color: black; border-radius:5px;")
        output_field.setReadOnly(True)  #wynik
        layout = QHBoxLayout()
        layout.addWidget(input_field)
        layout.addWidget(output_field)
        return layout

    def convert(self, curr_data, from_curr, to_curr, n):  #convert
        pass
        




url = 'https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_ybAM6h8asWboJSTGOSUy9TLPda85XRCXKRst6SoX'
response = requests.get(url)
data = response.json()['data']
curr_list=list(data.keys())


if __name__== "__main__":
  application=QApplication(sys.argv)
  win= curr_converter(data,curr_list)
  win.show()
  sys.exit(application.exec_())