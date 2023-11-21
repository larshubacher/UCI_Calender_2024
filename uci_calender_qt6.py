#Importing the components we need
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

#The sys module is responsible for processing commmand line arguments
import sys

## Subclass QMainWindow to customize your application's main window
class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__
        self.setWindowTitle("Button Holder App")
        button = QPushButton("PressMe!")
        ## Set our button as the central widget
        self.setCentralWidget(button)




app = QApplication(sys.argv)
window = ButtonHolder()

window.show()
#Start the event loop
app.exec()