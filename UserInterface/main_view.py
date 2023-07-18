import sys
from PyQt5 import QtWidgets, QtGui

from Utils import common_utils
from Helper import paths


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Grocery List Application")
        self.setGeometry(100, 100, 800, 600)

        common_utils.load_stylesheet(paths.gui_theme_path, window)

        self.nav_bar = NavigationBar()
        self.setCentralWidget(QtWidgets.QWidget(self))
        self.centralWidget().setLayout(QtWidgets.QVBoxLayout())
        self.centralWidget().layout().addWidget(self.nav_bar)


class NavigationBar(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.build_navbar()

    def build_navbar(self):
        layout = QtWidgets.QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        button_widget = QtWidgets.QWidget()
        button_layout = QtWidgets.QHBoxLayout(button_widget)
        button_layout.setContentsMargins(10, 10, 10, 10)
        button_layout.setSpacing(10)
        self.home_button = QtWidgets.QPushButton("Home Button")
        self.button2 = QtWidgets.QPushButton("Button 2")
        self.button3 = QtWidgets.QPushButton("Button 3")

        self.home_button.clicked.connect(self.on_home_button_clicked)
        self.button2.clicked.connect(self.on_button2_clicked)
        self.button3.clicked.connect(self.on_button3_clicked)

        layout.addWidget(self.home_button)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)

        layout.addWidget(button_widget, alignment=QtCore.Qt.AlignBottom)

    def on_home_button_clicked(self):
        print("Home Button Clicked!")

    def on_button2_clicked(self):
        print("Button 2 clicked!")

    def on_button3_clicked(self):
        print("Button 3 clicked!")

class WindowController:
    def __

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

