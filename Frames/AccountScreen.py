from sqlite3 import Row
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget

class AccountFrame(QWidget):
    def __init__(self, controller):
        super(AccountFrame,self).__init__()
        self.controller = controller
        self.initUI()
    
    def initUI(self):
        self.Grid = QtWidgets.QGridLayout()

        self.label=QtWidgets.QLabel()
        self.label.setText("Account Page")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.Grid.addWidget(self.label, 0, 0)

        self.List = QtWidgets.QListWidget(self)
        self.List.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        header = QCustomQWidget()
        header.setName("Name")
        header.setAge("Age")
        a =QtWidgets.QListWidgetItem(self.List)
        a.setSizeHint(header.sizeHint())
        a.setFlags(a.flags() &~QtCore.Qt.ItemIsSelectable)
        self.List.addItem(a)
        self.List.setItemWidget(a,header)

        for i in range(1,6):
            O = Person(name = "AH", age=i)
            a =QtWidgets.QListWidgetItem(self.List)
            myQ = QCustomQWidget()
            myQ.setName(O.name)
            myQ.setAge(O.age.__str__())
            a.setSizeHint(myQ.sizeHint())
            self.List.addItem(a)
            self.List.setItemWidget(a,myQ)

        self.Grid.addWidget(self.List, 1, 0)

        self.setLayout(self.Grid)

    def update(self):
        print("Account-Screen Update")


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class QCustomQWidget (QWidget):
    def __init__ (self, parent = None):
        super(QCustomQWidget, self).__init__(parent)
        self.textQHBoxLayout = QtWidgets.QHBoxLayout()
        self.textUpQLabel    = QtWidgets.QLabel()
        self.textDownQLabel  = QtWidgets.QLabel()
        self.textQHBoxLayout.addWidget(self.textUpQLabel)
        self.textQHBoxLayout.addWidget(self.textDownQLabel)
        self.setLayout(self.textQHBoxLayout)
        # setStyleSheet
        self.textUpQLabel.setStyleSheet('''
            color: rgb(0, 0, 255);
        ''')
        self.textDownQLabel.setStyleSheet('''
            color: rgb(255, 0, 0);
        ''')

    def setName (self, text):
        self.textUpQLabel.setText(text)

    def setAge (self, text):
        self.textDownQLabel.setText(text)