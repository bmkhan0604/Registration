from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QFrame, QStackedWidget
from Frames.StartScreen import *
from Frames.ScanScreen import *
from Frames.AccountScreen import *

class MainWindow(QMainWindow):
    resized = QtCore.pyqtSignal()
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(0,0,1000,1000)
        self.setWindowTitle("Registration")
        self.initUI()
        self.resized.connect(self.update)
        
    def initUI(self):
        self.Page = StartFrame(self)
        #self.Page = AccountFrame(self)
        self.setCentralWidget(self.Page)
        
    def resizeEvent(self, event):
        self.resized.emit()
        return super(MainWindow, self).resizeEvent(event)

    def changeFrame(self, dest):
        #Switch
        print("Changing Views: " + dest)
        self.Page.destroy()
        if dest == "ScanFrame": 
            self.Page = ScanFrame(self)
        elif dest == "StartFrame":
            self.Page = StartFrame(self)
        elif dest == "AccountFrame":
            self.Page = AccountFrame(self)
        else:
            self.Page = StartFrame(self)

        self.setCentralWidget(self.Page)

    def update(self):
        self.Page.update()
