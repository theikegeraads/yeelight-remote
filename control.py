import PyQt5.QtWidgets as qtw 
from PyQt5.QtCore import *
from yeelight import *
from PyQt5 import *

ipAdress = ""

class mainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Yeelight Control")
        self.setLayout(qtw.QVBoxLayout())
        self.setStyleSheet("background-color: #121212;")
        self.keypad()
         
    def keypad(self): #container maken
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout()) #layout setten

        def lconnect():
            ipConnect = self.ipField.text()
            try:
                light = Bulb(ipConnect)
                light.toggle()
                light.toggle()
                self.ipField.setText("")
                self.ipField.setPlaceholderText(f"Connected to {ipConnect}")
                global ipAdress
                ipAdress = ipConnect
            except:
                self.ipField.setText("")
                self.ipField.setPlaceholderText(f"Could not connect to {ipConnect} (Invalid IP)")
                
        def lToggle():
            global ipAdress
            if ipAdress == "":
                self.ipField.setPlaceholderText(f"Please enter an IP Adress")
            else:
                light = Bulb(ipAdress)
                light.toggle()

        def lOn():
            global ipAdress
            if ipAdress == "":
                self.ipField.setPlaceholderText(f"Please enter an IP Adress")
            else:
                light = Bulb(ipAdress)
                light.turn_on()

        def lOff():
            global ipAdress
            if ipAdress == "":
                self.ipField.setPlaceholderText(f"Please enter an IP Adress")
            else:     
                light = Bulb(ipAdress)
                light.turn_off()

        def lBrightness():
            cValue = brightDial.value()
            global ipAdress
            if ipAdress == "":
                self.ipField.setPlaceholderText(f"Please enter an IP Adress")
            else:
                brightLabel.setText(f"Brightness: {cValue}")     
                light = Bulb(ipAdress)
                light.set_brightness(cValue)
        def lRed():
            if ipAdress == "":
                self.ipField.setPlaceholderText(f"Please enter an IP Adress")
            else:   
                light = Bulb(ipAdress)
                light.set_rgb(255, 0, 0)

        






        self.show()

        self.layout().addWidget(container) # de container in de layout zetten

    
app = qtw.QApplication([])
mw = mainWindow()
mw.resize(250, 600)
app.setStyle('Fusion')
app.exec_() # app starten