#Importing the components we need
from PySide6.QtWidgets import QApplication, QPushButton, QSlider
from PySide6.QtCore import Qt
from button_holder import ButtonHolder

#The sys module is responsible for processing commmand line arguments
import sys

## The slot: respons when something happens
def respond_to_slider(data):
    print("Slider moved to: ", data)


app = QApplication()

slider = QSlider(Qt.Horizontal)
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(25)


#button = QPushButton("Press Me")
#button.setCheckable(True) ## Makes the button checkable. It's unchecked by default.
## Future clicks toggle between checked and unchecked states

## Clicked is a signal of QPushButton. It's emitted when you click onthe button
## You can wire a slot to the signal using the syntax below:
#button.clicked.connect(button_clicked)
#button.show()

#window = ButtonHolder()
#window.show()

## Do the connection. QT takes care of the passing of the data from the signal to the slot
slider.valueChanged.connect(respond_to_slider)
slider.show()

#Start the event loop
app.exec()