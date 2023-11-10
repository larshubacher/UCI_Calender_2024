from PySide6.QtWidgets import QMainWindow

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app ## ceclare an app member
        self.setWindowTitle("Custom MainWindow")

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit)

        edit_menu = menu-bar.addMenu("&Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

        menu_bar.addMenu("&Window")
        menu_bar.addMenu("&Setting")
        menu_bar.addMenu("&Help")
