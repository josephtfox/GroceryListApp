import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.uic.properties import QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Grocery List Application")
        self.setGeometry(100, 100, 300, 200)

        self.setup_buttons()

    def setup_buttons(self):
        button1 = QtWidgets.QPushButton("Open Notepad", self)
        button1.setGeometry(50, 50, 200, 30)
        button1.clicked.connect(self.open_notepad)

        button2 = QtWidgets.QPushButton("Open Calculator", self)
        button2.setGeometry(50, 100, 200, 30)
        button2.clicked.connect(self.open_calculator)

    def open_notepad(self):
        subprocess.Popen("notepad.exe")

    def open_calculator(self):
        subprocess.Popen("calc.exe")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

