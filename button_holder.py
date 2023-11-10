#Importing the components we need
from PySide6.QtWidgets import QMainWindow, QPushButton

## Subclass QMainWindow to customize your application's main window
class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button Holder App")
        button = QPushButton("PressMe!")
        ## Set our button as the central widget
        self.setCentralWidget(button)