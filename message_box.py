from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMessageBox

class message_box(QMessageBox):
    def __init__(self, app):
        super().__init__() 
        
        self.setWindowTitle("QMessageBox")

        button_hard = QPushButton("Hard")
        button_hard.clicked.connect(self.button_clicked_hard)

        button_critical = QPushButton("Critical")
        button_critical.clicked.connect(self.button_clicked_critital)

        button_question = QPushButton("Question")
        button_question.clicked.connect(self.button_clicked_question)

        button_information = QPushButton("Information")
        button_information.clicked.connect(self.button_clicked_Information)

        button_warning = QPushButton("Warning")
        button_warning.clicked.connect(self.button_clicked_warning)

        ## Layout
        layout = QVBoxLayout()
        layout.addWidget(button_hard)
        layout.addWidget(button_critical)
        layout.addWidget(button_question)
        layout.addWidget(button_information)
        layout.addWidget(button_warning)
        self.setLayout(layout)

    def button_clicked_hard(self):
        print("Hard")

    def button_clicked_critical(self):
        print("Critical")

    def button_clicked_question(self):
        print("Question")

    def button_clicked_Information(self):
        print("Information")

    def button_clicked_warning(self):
        print("warning")



    # def button_clicked_hard(self):
    #     message = QMessageBox()
    #     message.setMinimumSize(700, 200)
    #     message.setWindowTitle("Message Title")
    #     message.setText("Something happend")
    #     message.setInformativeText("Do you want to do something about it ?")
    #     message.setIcon(QMessageBox.critical)
    #     message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    #     ## Standardeinstellung
    #     message.defaultButton(QMessageBox.Ok)
    #     ret = message.exec()
    #     if ret == QMessageBox.Ok:
    #         print("User chose OK")
    #     else:
    #         print("User chose Cancel")

    # def button_clicked_critital(self):
    #     """Can be: critital - question - information - warning - about"""
    #     ret = QMessageBox.critical(self, "Message Title", "Critical Message!", QMessageBox.Ok | QMessageBox.Cancel)
    #     if ret == QMessageBox.Ok:
    #         print("User chose OK")
    #     else:
    #         print("User chose cancel")

