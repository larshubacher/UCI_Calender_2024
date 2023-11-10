#Importing the components we need
from PySide6.QtWidgets import QApplication, QPushButton
from button_holder import ButtonHolder

#The sys module is responsible for processing commmand line arguments
import sys

## The slot: respons when something happens
def button_clicked(data):
    print("You clicked the button, didn't you: ", data)


app = QApplication(sys.argv)
button = QPushButton("Press Me")
button.setCheckable(True) ## Makes the button checkable. It's unchecked by default.
## Future clicks toggle between checked and unchecked states

## Clicked is a signal of QPushButton. It's emitted when you click onthe button
## You can wire a slot to the signal using the syntax below:
button.clicked.connect(button_clicked)

button.show()

#window = ButtonHolder()
#window.show()

#Start the event loop
app.exec()