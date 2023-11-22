from PySide6.QtWidgets import QWidget, QCalendarWidget, QGridLayout

class time_filter_widget(QWidget):
    def __init__(self):
        super().__init__()

        calendar = QCalendarWidget()
        calendar.setGridVisible(True)
        grid_layout = QGridLayout()
        grid_layout.addWidget(calendar,0,0)
        self.setLayout(grid_layout)
