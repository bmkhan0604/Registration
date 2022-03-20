from sqlite3 import Row
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget

class StartFrame(QWidget):
    def __init__(self, controller):
        super(StartFrame,self).__init__()
        self.controller = controller
        self.initUI()
        self.setAttribute(QtCore.Qt.WA_StyledBackground)
    
    def initUI(self):
        self.setObjectName("StartScreen")
        self.setStyleSheet("QWidget#"+self.objectName()+"{\n"
                            "background-color: rgb(0, 0, 255);\n"
                            "background-color: qlineargradient(spread:reflect, x1:0.135, y1:0.216227, x2:0.782, y2:0.602273, stop:0 rgba(0, 0, 247, 255), stop:1 rgba(0, 0, 0, 255));\n"
                            "}")
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 70, 721, 401))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(100, 0, 100, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet( "font: 36pt;\n"
                                  "color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet( "color: rgb(255, 255, 255);\n"
                                    "font:  26pt;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setTabletTracking(False)
        self.pushButton.setStyleSheet(  "border-radius:20px;\n"
                                        "background-color: rgb(255, 170, 0);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "font:  26pt;\n"
                                        "")
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.Grid = QtWidgets.QGridLayout()
        self.Grid.setRowStretch(1,1)
        self.Grid.setColumnStretch(0,1)

        self.setLayout(self.Grid)

        self.label.setText("Welcome")
        self.label_2.setText("Sign In")
        self.pushButton.setText("Login")
        self.pushButton.clicked.connect(lambda: self.controller.changeFrame("ScanFrame"))

    def update(self):
        print("StartScreen Update")
        #self.b1.setStyleSheet("Border: 5px solid rgb(255, 0, 0);\n"
        #                      "Border-Radius: "+ str(self.b1.width()) + ";\n"
        #                      "Background: rgb(255, 255, 0)")
        