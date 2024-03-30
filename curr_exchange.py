import requests
import sys
from PyQt5.QtGui import QPalette, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QListWidget, QLineEdit, QHBoxLayout, QMainWindow,QComboBox
class curr_converter(QWidget):
    def __init__(self):   
        super().__init__()
        self.setWindowTitle("Currency Converter")
        self.setStyleSheet("background-color: #58A4B0;")
        self.setFixedWidth(400)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        curr_data, curr_list = self.load_api() #curr data do converta


        lists = self.lists(curr_list)
        inputs = self.input_fields()

        self.layout.addLayout(lists) #dodanie listy i pol na inputy
        self.layout.addLayout(inputs)

    def lists(self, curr_list):  #listy horyznotalnie 
        from_list = QComboBox() #drop down
        from_list.setStyleSheet("background-color: #BAC1B8; color: black; border-radius:5px;")
        from_list.addItems(curr_list)
        from_list.setCurrentIndex(curr_list.index('USD'))
        to_list = QComboBox()
        to_list.setStyleSheet("background-color: #BAC1B8; color: black; border-radius:5px;")
        to_list.addItems(curr_list)
        to_list.setCurrentIndex(curr_list.index('PLN'))

        layout = QHBoxLayout()
        layout.addWidget(from_list)
        layout.addWidget(to_list)
        return layout

    def input_fields(self):   #inputy horyzontalnie
        input_f = QLineEdit()
        input_f.setStyleSheet("background-color: #FFFFFF; color: black; border-radius:5px;")
        output_f = QLineEdit()
        output_f.setStyleSheet("background-color: #FFFFFF; color: black; border-radius:5px;")
        output_f.setReadOnly(True)  #wynik
        
        layout = QHBoxLayout()
        layout.addWidget(input_f)
        layout.addWidget(output_f)
        return layout

    def convert(self, curr_data, from_curr, to_curr, n):  #convert
        pass

    def load_api(self):
        url = 'https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_ybAM6h8asWboJSTGOSUy9TLPda85XRCXKRst6SoX' #wczytanie danych z api
        response = requests.get(url)
        curr_data = response.json()['data']
        curr_list=list(curr_data.keys())
        return curr_data, curr_list







if __name__== "__main__":
  application=QApplication(sys.argv)
  win= curr_converter()
  win.show()
  sys.exit(application.exec_())