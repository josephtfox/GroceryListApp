from PyQt5 import QtWidgets, QtGui

def load_stylesheet(file_path, widget):
    with open(file_path, "r") as f:
        style_sheet = f.read()
        widget.setStyleSheet(style_sheet)