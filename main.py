import sys
from PySide6.QtWidgets import QApplication
from mainwindow import main_window

app = QApplication(sys.argv)

main_window = main_window()

main_window.show()

app.exec()