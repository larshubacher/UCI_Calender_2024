import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon

def window():
    app = QApplication(sys.argv)
    ## Create a window
    win = QMainWindow()
    ## Frist two parameters specify where the window pops up and the next two specify the size of the window
    win.setGeometry(1200, 300, 500, 500)
    win.setWindowTitle("UCI XCO Calender 2024")
    win.setWindowIcon(QIcon("images/icon.jpeg"))
    win.setToolTip("TurtleCode")
    win.show()
    sys.exit(app.exec())


window()