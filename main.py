from PySide6.QtWidgets import QApplication
from QList import Qlist
import sys

app = QApplication(sys.argv)

window = Qlist()
window.show()

app.exec()