from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from widgets import layout, time_filter_widget

class main_window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("UCI Calender 2024")

        container = QWidget()
        containerLayout = QVBoxLayout()
        container.setLayout(containerLayout)

        layout_widget = layout()
        containerLayout.addWidget(layout_widget)

        #time_filter = time_filter_widget()
        #containerLayout.addWidget(time_filter)

        self.setCentralWidget(container)