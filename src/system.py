from math import inf
from PyQt5.QtWidgets import QMainWindow, QListWidgetItem, QColorDialog, QFileDialog, QStyle
from PyQt5.QtCore import Qt, QCoreApplication


# Project modules
from src.ui.systemadmin import Ui_System


class SystemWindow(QMainWindow, Ui_System):
    def __init__(self):
        super(SystemWindow, self).__init__()
        self.setupUi(self)

    


    