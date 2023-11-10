#Importing the components we need
from PySide6.QtWidgets import QApplication, QPushButton
from button_holder import ButtonHolder

#The sys module is responsible for processing commmand line arguments
import sys

def button_clicked():
    print("You clicked the button, didn't you!")


app = QApplication(sys.argv)
button = QPushButton("Press Me")

button.clicked.connect(button_clicked)

button.show()

#window = ButtonHolder()
#window.show()

#Start the event loop
app.exec()