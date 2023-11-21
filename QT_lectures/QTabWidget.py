from PySide6.QtWidgets import QLineEdit, QTabWidget, QWidget, QLabel, QHBoxLayout, QPushButton, QVBoxLayout

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QTabWidgetDemo")

        tab_widget = QTabWidget(self)

        ## Infomration
        widget_form = QWidget()
        label_full_name = QLabel("Full name: ")
        line_edit_full_name = QLineEdit()
        from_layout = QHBoxLayout()
        from_layout.addWidget(label_full_name)
        from_layout.addWidget(line_edit_full_name)
        widget_form.setLayout(from_layout)

        ## Buttons
        widget_buttons = QWidget()
        button_1 = QPushButton("One")
        button_1.clicked.connect(self.button_1_clicked)
        button_2 = QPushButton("Two")
        button_3 = QPushButton("Three")
        buttons_layout = QVBoxLayout()
        buttons_layout.addWidget(button_1)     
        buttons_layout.addWidget(button_2)   
        buttons_layout.addWidget(button_3)    
        widget_buttons.setLayout(buttons_layout)  

        ## Add tabs
        tab_widget.addTab(widget_form, "Information")
        tab_widget.addTab(widget_buttons, "Buttons")

        v_layout = QVBoxLayout()
        v_layout.addWidget(tab_widget)

        self.setLayout(v_layout)

    def button_1_clicked(self):
        print("Button clicked")
    