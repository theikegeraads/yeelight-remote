import PyQt5.QtWidgets as qtw 
from PyQt5.QtCore import *
from yeelight import *
from PyQt5 import *

ipAddress = ""

class mainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Yeelight Control")
        self.setLayout(qtw.QVBoxLayout())
        self.setStyleSheet("background-color: #121212;")
        self.setWindowIcon(QtGui.QIcon('icon/app-icon.png'))
        self.keypad()
         







    def keypad(self):
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())
        self.isConnected = False 

        def lConnect():
            if self.isConnected == False:
                global ipAddress
                ipAddress = ipField.text()
                try:
                    yl = Bulb(ipAddress)
                    yl.toggle()
                    yl.toggle()
                    ipLabel.setText(f"{ipAddress}")
                    connectButton.setText("Disconnect")
                    ipField.setText("")
                    ipField.setPlaceholderText(f"Connected to {ipAddress}.")
                    ipField.setDisabled(1)
                    ipField.setStyleSheet("background:#7F7F7F")
                    self.isConnected = True
                    print("connected")
                    
                except:
                    ipField.setText("")
                    ipLabel.setText("Not Connected")
                    ipField.setPlaceholderText(f"Failed to connect to {ipAddress}.")
                    print("failed")
            else:
                ipLabel.setText("Not Connected.")
                ipField.setStyleSheet("background:white")
                ipField.setText("")
                ipField.setPlaceholderText("Yeelight IP Address.")
                ipField.setDisabled(0)
                connectButton.setText("Connect")
                self.isConnected = False
                print("Disconnected")

                
                


        def lToggle():
            if self.isConnected == False:
                ipField.setPlaceholderText("Please enter an IP Address.")
            else:
                try:
                    yl = Bulb(ipAddress)
                    yl.toggle()
                except:
                    pass

        def lOn():
            if self.isConnected == False:
                ipField.setPlaceholderText("Please enter an IP Address.")
            else:
                try:
                    yl = Bulb(ipAddress)
                    yl.turn_on()
                except:
                    pass

        def lOff():
            if self.isConnected == False:
                ipField.setPlaceholderText("Please enter an IP Address.")
            else:
                try:
                    yl = Bulb(ipAddress)
                    yl.turn_off()
                except:
                    pass

        
        def lRed():
            if self.isConnected == False:
                ipField.setPlaceholderText("Please enter an IP Address.")
            else:
                try:
                    yl = Bulb(ipAddress)
                    yl.set_rgb(255, 0, 0)
                except:
                    pass           

        def lGreen():
            if self.isConnected == False:
                ipField.setPlaceholderText("Please enter an IP Address.")
            else:
                try:
                    yl = Bulb(ipAddress)
                    yl.set_rgb(0, 255, 0)
                except:
                    pass           

        def lBlue():
            if self.isConnected == False:
                ipField.setPlaceholderText("Please enter an IP Address.")
            else:
                try:
                    yl = Bulb(ipAddress)
                    yl.set_rgb(0, 0, 255)
                except:
                    pass           

        def lOrange():
            if self.isConnected == False:
                ipField.setPlaceholderText("Please enter an IP Address.")
            else:
                try:
                    yl = Bulb(ipAddress)
                    yl.set_rgb(255, 165, 0)
                except:
                    pass           

        def lYellow():
            if self.isConnected == False:
                ipField.setPlaceholderText("Please enter an IP Address.")
            else:
                try:
                    yl = Bulb(ipAddress)
                    yl.set_rgb(255, 255, 0)
                except:
                    pass           

        def lCFB():
            if self.isConnected == False:
                ipField.setPlaceholderText("Please enter an IP Address.")
            else:
                try:
                    yl = Bulb(ipAddress)
                    yl.set_rgb(100,149,237)
                except:
                    pass           

        def lBright():
            if self.isConnected == False:
                ipField.setPlaceholderText("Please enter an IP Address.")
            else:
                try:
                    cBrightness = brightDial.value()
                    brightLabel.setText(f"Brightness: {cBrightness}")
                    yl = Bulb(ipAddress)
                    yl.set_brightness(cBrightness)
                except:
                    pass







        toggleButton = qtw.QPushButton("Power", clicked = lToggle)
        toggleButton.setMaximumWidth(45)
        toggleButton.setMinimumHeight(42)
        toggleButton.setStyleSheet("QPushButton { color: #FF0002; background: #2d2d2d }")
        container.layout().addWidget(toggleButton, 0, 0)
        

        ipLabel = qtw.QLabel(f"Not Connected.")
        ipLabel.setStyleSheet("color: white;")
        container.layout().addWidget(ipLabel, 0, 2)

        onButton = qtw.QPushButton("On", clicked = lOn)
        onButton.setStyleSheet("QPushButton { color: white; background: #2D2D2d }")
        container.layout().addWidget(onButton, 1, 0, 1, 4)

        offButton = qtw.QPushButton("Off", clicked = lOff)
        offButton.setStyleSheet("QPushButton { background-color: #2D2D2D; color: white; }")
        container.layout().addWidget(offButton, 2, 0, 1, 4)

        spacer1 = qtw.QPushButton("")
        spacer1.setStyleSheet("background: #121212; border: 1px solid #121212 ")
        container.layout().addWidget(spacer1, 3, 0, 1, 3)

        redButton = qtw.QPushButton("Red", clicked = lRed)
        redButton.setStyleSheet("QPushButton { background-color: #2D2D2D; color: red; }")
        container.layout().addWidget(redButton, 4, 0)
        
        greenButton = qtw.QPushButton("Green", clicked = lGreen)
        greenButton.setStyleSheet("QPushButton { background-color: #2D2D2D; color: green; }")
        container.layout().addWidget(greenButton, 4, 1)

        blueButton = qtw.QPushButton("Blue", clicked = lBlue)
        blueButton.setStyleSheet("QPushButton { background-color: #2D2D2D; color: blue; }")
        container.layout().addWidget(blueButton, 4, 2)

        orangeButton = qtw.QPushButton("Orange", clicked = lOrange)
        orangeButton.setStyleSheet("QPushButton { background-color: #2D2D2D; color: orange; }")
        container.layout().addWidget(orangeButton, 5, 0)
        
        yellowButton = qtw.QPushButton("Yellow", clicked = lYellow)
        yellowButton.setStyleSheet("QPushButton { background-color: #2D2D2D; color: yellow; }")
        container.layout().addWidget(yellowButton, 5, 1)

        cfbButton = qtw.QPushButton("Cyan", clicked = lCFB)
        cfbButton.setStyleSheet("QPushButton { background-color: #2D2D2D; color: cornflowerblue; }")
        container.layout().addWidget(cfbButton, 5, 2)

        spacer2 = qtw.QPushButton("")
        spacer2.setStyleSheet("background: #121212; border: 1px solid #121212 ")
        container.layout().addWidget(spacer2, 6, 0, 1, 3)

        brightDial = qtw.QDial(valueChanged = lBright)
        brightDial.setMinimum(0)
        brightDial.setMaximum(100)
        brightDial.setStyleSheet("QDial { Background-color: #2D2D2D; }")
        container.layout().addWidget(brightDial, 7, 0, 1, 3)

        brightLabel = qtw.QPushButton("Brightness:")
        brightLabel.setStyleSheet("color: white; border: none; background:transparent;")
        container.layout().addWidget(brightLabel, 8, 0, 1, 3)

        redSlide = qtw.QSlider(Qt.Horizontal)
        redSlide.setMinimum(0)
        redSlide.setMaximum(255)
        redSlide.setTickInterval(1)
        redSlide.setSingleStep(1)
        container.layout().addWidget(redSlide, 9, 1, 1, 3)

        greenSlide = qtw.QSlider(Qt.Horizontal)
        greenSlide.setMinimum(0)
        greenSlide.setMaximum(255)
        greenSlide.setTickInterval(1)
        greenSlide.setSingleStep(1)
        container.layout().addWidget(greenSlide, 10, 1, 1, 3)

        blueSlide = qtw.QSlider(Qt.Horizontal)
        blueSlide.setMinimum(0)
        blueSlide.setMaximum(255)
        blueSlide.setTickInterval(1)
        blueSlide.setSingleStep(1)
        container.layout().addWidget(blueSlide, 11, 1, 1, 3)

        redLabel = qtw.QLabel("Red Value: ")
        redLabel.setStyleSheet("color:white;")
        container.layout().addWidget(redLabel, 9, 0)

        greenLabel = qtw.QLabel("Green Value: ")
        greenLabel.setStyleSheet("color:white;")
        container.layout().addWidget(greenLabel, 10, 0)

        blueLabel = qtw.QLabel("Blue Value: ")
        blueLabel.setStyleSheet("color:white;")
        container.layout().addWidget(blueLabel, 11, 0)

        orLabel =  qtw.QPushButton("-OR-")
        orLabel.setStyleSheet("color:white; border:none;background:transparent;")
        container.layout().addWidget(orLabel, 12, 0, 1, 3)

        hueLabel = qtw.QLabel("Hue: ")
        hueLabel.setStyleSheet("color:white;")
        container.layout().addWidget(hueLabel, 13, 0)

        saturationLabel = qtw.QLabel("Saturation: ")
        saturationLabel.setStyleSheet("color:white;")
        container.layout().addWidget(saturationLabel, 14, 0)

        lumLabel = qtw.QLabel("Luminance: ")
        lumLabel.setStyleSheet("color:white;")
        container.layout().addWidget(lumLabel, 15, 0)
        
        hueSlide = qtw.QSlider(Qt.Horizontal)
        hueSlide.setMinimum(0)
        hueSlide.setMaximum(255)
        hueSlide.setTickInterval(1)
        hueSlide.setSingleStep(1)
        container.layout().addWidget(hueSlide, 13, 1, 1, 3)
            
        saturationSlide = qtw.QSlider(Qt.Horizontal)
        saturationSlide.setMinimum(0)
        saturationSlide.setMaximum(255)
        saturationSlide.setTickInterval(1)
        saturationSlide.setSingleStep(1)
        container.layout().addWidget(saturationSlide, 14, 1, 1, 3)

        lumSlide = qtw.QSlider(Qt.Horizontal)
        lumSlide.setMinimum(0)
        lumSlide.setMaximum(255)
        lumSlide.setTickInterval(1)
        lumSlide.setSingleStep(1)
        container.layout().addWidget(lumSlide, 15, 1, 1, 3)

        spacer3 = qtw.QPushButton("-Flash Mode-")
        spacer3.setStyleSheet("background:transparent;border:none;color:white;")
        container.layout().addWidget(spacer3, 16, 0, 1, 3)

        intensityLabel = qtw.QLabel("Intensity: ")
        intensityLabel.setStyleSheet("color:white;")
        container.layout().addWidget(intensityLabel, 17, 0)

        intensitySlide = qtw.QSlider(Qt.Horizontal)
        intensitySlide.setMinimum(2)
        intensitySlide.setMaximum(6)
        intensitySlide.setTickInterval(1)
        intensitySlide.setSingleStep(1)
        container.layout().addWidget(intensitySlide, 17, 1, 1, 3)

        amountLabel = qtw.QLabel("Flashes: ")
        amountLabel.setStyleSheet("color:white;")
        container.layout().addWidget(amountLabel, 18, 0)

        amountSlide = qtw.QSlider(Qt.Horizontal)
        amountSlide.setMinimum(1)
        amountSlide.setMaximum(10)
        amountSlide.setTickInterval(1)
        amountSlide.setSingleStep(1)
        container.layout().addWidget(amountSlide, 18, 1, 1, 3)

        flashButton = qtw.QPushButton("Flash!")
        flashButton.setStyleSheet('background-color: #2D2D2D; color: white;')
        container.layout().addWidget(flashButton, 19, 0, 1, 3)

        spacer4 = qtw.QPushButton("")
        spacer4.setStyleSheet("background:transparent;border:none;color:white;")
        container.layout().addWidget(spacer4, 20, 0, 1, 3)

        ipField = qtw.QLineEdit()
        ipField.setPlaceholderText("Yeelight IP Address...")
        ipField.setStyleSheet("background:white;color:black")
        container.layout().addWidget(ipField, 21, 0, 1, 3)

        connectButton = qtw.QPushButton("Connect", clicked = lConnect)
        connectButton.setStyleSheet("background:#2d2d2d;color:white")
        container.layout().addWidget(connectButton, 22, 0, 1 ,3)

        self.show()

        self.layout().addWidget(container)
    
app = qtw.QApplication([])
mw = mainWindow()

app.setStyle('Fusion')
app.exec_()