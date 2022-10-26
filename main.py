import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidgetItem
from application import AppWindow


def main():
    app = QApplication(sys.argv)
    win = AppWindow()
    win.show()
    app.exec()


if __name__ == '__main__':
    main()