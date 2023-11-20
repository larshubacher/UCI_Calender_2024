from PySide6.QtWidgets import QMessageBox

class message_box(QMessageBox):
    def __init__(self, app):
        super().__init__()

    def button_clicked_hard(self):
        message = QMessageBox()
        message.setMinimumSize(700, 200)
        message.setWindowTitle("Message Title")
        message.setText("Something happend")
        message.setInformativeText("Do you want to do something about it ?")
        message.setIcon(QMessageBox.critical)
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message.defaultButton(QMessageBox.Ok)
        ret = message.exec()
        if ret == QMessageBox.Ok:
            print("User chose OK")
        else:
            print("User chose Cancel")

