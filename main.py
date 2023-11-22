import sys
from PySide6.QtWidgets import QApplication
from mainwindow import layout

app = QApplication(sys.argv)

main_window = layout()

main_window.show()

app.exec()