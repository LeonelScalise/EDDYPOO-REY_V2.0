# PyQt5 modules
from math import inf
from PyQt5.QtWidgets import QMainWindow, QListWidgetItem, QColorDialog, QFileDialog, QStyle
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5 import uic

# Project modules
from src.ui.mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

