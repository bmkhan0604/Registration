from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget, QLineEdit
import RPi.GPIO as GPIO
from picamera import PiCamera
from picamera.array import PiRGBArray
from threading import Thread, Event
import time
from pyzbar.pyzbar import decode
from PyQt5.QtCore import QThread, QObject
#from events import Events

class ScanFrame(QWidget):
    def __init__(self, controller):
        super(ScanFrame,self).__init__()
        self.controller = controller
        self.initUI()
        self.exiting = False
        self.t1 = Thread(target=self.StartCamera)
        self.t1.start()
        self.events = Event()
    
    def initUI(self):
        self.label=QtWidgets.QLabel(self)
        self.label.setText("Enter or Scan your Confirmation Code")
        self.label.move(100,100)
        
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("StartScreen")
        self.b1.move(100,200)
        self.b1.clicked.connect(lambda: self.controller.changeFrame("StartFrame"))

        self.entrybox = QLineEdit(self)
        self.entrybox.move(100,300)
        self.entrybox.setPlaceholderText("Enter you Confirmation Code")

        self.enterButton = QtWidgets.QPushButton(self)
        self.enterButton.setText("Enter")
        self.enterButton.move(100,350)
        self.enterButton.clicked.connect(self.Enter)

    def Enter(self):
        text = self.entrybox.text()
        #Validation Check
        if text != "":
            self.ConfirmationCode = text
            self.controller.changeFrame("AccountFrame")

    def StartCamera(self):
        #setup 
        self.ledpin = 10
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.ledpin, GPIO.OUT)
        self.camera = PiCamera()
        #While on this Page
        GPIO.output(self.ledpin, GPIO.HIGH)
        while(not self.exiting):
            #Capture Image
            rawCapture = PiRGBArray(self.camera)
            time.sleep(.1)
            self.camera.capture(rawCapture, format = 'bgr')
            #Decode Image
            image = rawCapture.array
            decodedObjects = decode(image)
            if len(decodedObjects) > 0:
                print(decodedObjects )
                self.exiting = True
                #implement validation check on confirmation code to DB here
                self.ConfirmationCode = decodedObjects[0].data
                self.entrybox.setText(str(self.ConfirmationCode))
                
    

    def destroy(self):
        #set condition to close open thread
        self.exiting = True
        #wait for thread to finish
        self.t1.join()
        #Cleanup
        print("cleanup")
        self.camera.close()
        GPIO.output(self.ledpin,GPIO.LOW)
        GPIO.cleanup()

        print("Confirmation Code:", self.ConfirmationCode)
        super(ScanFrame,self).destroy()
