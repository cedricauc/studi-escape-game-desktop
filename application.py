from PyQt5.QtWidgets import QMainWindow
from pui.interface import Ui_MainWindow


class AppWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
