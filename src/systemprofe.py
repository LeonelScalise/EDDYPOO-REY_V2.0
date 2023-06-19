from PyQt5.QtWidgets import QMainWindow, QListWidgetItem, QColorDialog, QFileDialog, QStyle
from PyQt5.QtCore import Qt, QCoreApplication


# Project modules
from src.ui.systemadmin import Ui_Systemprofe


class SystemprofeWindow(QMainWindow, Ui_Systemprofe):
    def __init__(self):
        super(SystemprofeWindow, self).__init__()
        self.setupUi(self)
