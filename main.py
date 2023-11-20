from PySide6.QtWidgets import QApplication
from message_box import Message_box
import sys

app = QApplication(sys.argv)

window = Message_box()
window.show()

app.exec()