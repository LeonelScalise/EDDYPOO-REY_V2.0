from math import inf
from PyQt5.QtWidgets import QMainWindow, QListWidgetItem, QColorDialog, QFileDialog, QStyle
from PyQt5.QtCore import Qt, QCoreApplication


# Project modules
from src.ui.systemadmin import Ui_Systemadmin


class SystemadminWindow(QMainWindow, Ui_Systemadmin):
    def __init__(self):
        super(SystemadminWindow, self).__init__()
        self.setupUi(self)

    


    