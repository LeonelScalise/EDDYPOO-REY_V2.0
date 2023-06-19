# PyQt5 modules
from PyQt5 import QtWidgets
from qt_material import apply_stylesheet

# Python modules
import sys

# Main window ui import
from src.mainwindow import MainWindow

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    apply_stylesheet(app, theme='light_blue.xml')
    window.show()
    sys.exit(app.exec())
