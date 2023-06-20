from PyQt5.QtWidgets import QMainWindow, QListWidgetItem, QColorDialog, QFileDialog, QStyle
from PyQt5.QtCore import Qt, QCoreApplication


# Project modules
from src.ui.systemadmin import Ui_Systemadmin


class SystemadminWindow(QMainWindow, Ui_Systemadmin):
    def __init__(self):
        super(SystemadminWindow, self).__init__()
        self.setupUi(self)

        self.btn_alta_admin.clicked.connect(self.showWindowAltaAdmin)
        self.btn_alta_alu.clicked.connect(self.showWindowAltaAlu)
        self.btn_alta_profe.clicked.connect(self.showWindowAltaProfe)
        self.btn_alta_materia.clicked.connect(self.showWindowAltaMateria)
        self.btn_alta_comi.clicked.connect(self.showWindowAltaComi)
        self.btn_alta_carrera.clicked.connect(self.showWindowAltaCarrera)


    def showWindowAltaAdmin(self):
        self.stackedWidget.setCurrentWidget(self.page_alta_admin)
    
    def showWindowAltaAlu(self):
        self.stackedWidget.setCurrentWidget(self.page_alta_alu)

    def showWindowAltaProfe(self):
        self.stackedWidget.setCurrentWidget(self.page_alta_profe)
    
    def showWindowAltaMateria(self):
        self.stackedWidget.setCurrentWidget(self.page_alta_materia)

    def showWindowAltaComi(self):
        self.stackedWidget.setCurrentWidget(self.page_alta_comi)
    
    def showWindowAltaCarrera(self):
        self.stackedWidget.setCurrentWidget(self.page_alta_carrera)

    


    