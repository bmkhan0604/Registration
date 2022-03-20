import sys
from PyQt5.QtWidgets import QApplication
from mainWindow import MainWindow

def window():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

window()
