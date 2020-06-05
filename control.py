import PyQt5.QtWidgets as qtw 

from yeelight import *
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
        self.ipField = qtw.QLineEdit()
        self.ipField.setPlaceholderText("Lamp IP address...")

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

        connectButton = qtw.QPushButton("Connect", clicked = lconnect)
        onButton = qtw.QPushButton("On", clicked = lOn)
        offButton = qtw.QPushButton("Off", clicked = lOff)
        brightDial = qtw.QDial(valueChanged = lBrightness)
        brightDial.setMinimum(0)
        brightDial.setMaximum(100)
        brightDial.setValue(128)
        brightLabel = qtw.QLabel("Brightness: ")
        container.layout().addWidget(self.ipField, 0, 0, 1, 5)
        container.layout().addWidget(connectButton, 1, 0, 1, 5)
        container.layout().addWidget(onButton, 2, 0, 1, 2)
        container.layout().addWidget(offButton, 2, 3, 1, 2)
        container.layout().addWidget(brightDial, 3, 1)
        container.layout().addWidget(brightLabel, 3, 0)

        connectButton.setStyleSheet("QPushButton { background-color: #2D2D2D; color: white; }")
        onButton.setStyleSheet("QPushButton { background-color: #2D2D2D; color: white; }")
        offButton.setStyleSheet("QPushButton { background-color: #2D2D2D; color: white; }")
        brightDial.setStyleSheet("QDial { Background-color: #2D2D2D; }")
        brightLabel.setStyleSheet("QLabel { color: white; }")
        self.ipField.setStyleSheet("background-color: white;")
        self.show()

        self.layout().addWidget(container) # de container in de layout zetten

    
app = qtw.QApplication([])
mw = mainWindow()
mw.resize(600, 200)
app.setStyle('Fusion')
app.exec_() # app starten