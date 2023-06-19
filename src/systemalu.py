from PyQt5.QtWidgets import QMainWindow, QListWidgetItem, QColorDialog, QFileDialog, QStyle
from PyQt5.QtCore import Qt, QCoreApplication


# Project modules
from src.ui.systemadmin import Ui_Systemalu


class SystemaluWindow(QMainWindow, Ui_Systemalu):
    def __init__(self):
        super(SystemaluWindow, self).__init__()
        self.setupUi(self)
