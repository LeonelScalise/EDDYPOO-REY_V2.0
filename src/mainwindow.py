# PyQt5 modules
from math import inf
from PyQt5.QtWidgets import QMainWindow, QListWidgetItem, QColorDialog, QFileDialog, QStyle
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5 import QtWidgets


# Project modules
from src.ui.mainwindow import Ui_MainWindow
from src.login import LoginWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.login_window = LoginWindow()
    
        self.btn_admin.clicked.connect(lambda : self.open_login_window("admin"))
        self.btn_alu.clicked.connect(lambda : self.open_login_window("alu"))
        self.btn_profe.clicked.connect(lambda : self.open_login_window("profe"))
        self.btn_salir.clicked.connect(self.salir)
        self.login_window.btn_back.clicked.connect(self.regresar)
    
    
    def open_login_window(self, tipo:str):
        self.hide()
        if tipo == "admin":
            self.login_window.label_tipo.setText("ADMINISTRADOR")
        elif tipo == "alu":
            self.login_window.label_tipo.setText("ALUMNO")
        else:
            self.login_window.label_tipo.setText("PROFESOR")
        self.login_window.show()
    
    def salir():
        QtWidgets.QApplication.exit()
    
    def regresar(self):
        self.login_window.hide()
        self.login_window.label_error.setText("")
        self.login_window.input_legajo.setText("")
        self.login_window.input_pass.setText("")
        self.show()


        