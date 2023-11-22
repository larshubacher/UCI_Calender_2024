from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QDateEdit, QPushButton, QWidget
from PySide6.QtCore import Qt

class DateSelectionWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Date Selection")
        self.setGeometry(100, 100, 400, 200)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        self.date_edit1 = QDateEdit(self)
        self.date_edit2 = QDateEdit(self)

        layout.addWidget(self.date_edit1)
        layout.addWidget(self.date_edit2)

        submit_button = QPushButton("Submit", self)
        submit_button.clicked.connect(self.submit_dates)
        layout.addWidget(submit_button)

    def submit_dates(self):
        selected_date1 = self.date_edit1.date().toString(Qt.ISODate)
        selected_date2 = self.date_edit2.date().toString(Qt.ISODate)

        print("Selected Date 1:", selected_date1)
        print("Selected Date 2:", selected_date2)

if __name__ == "__main__":
    app = QApplication([])
    window = DateSelectionWindow()
    window.show()
    app.exec_()
