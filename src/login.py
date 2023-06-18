from math import inf
from PyQt5.QtWidgets import QMainWindow, QListWidgetItem, QColorDialog, QFileDialog, QStyle
from PyQt5.QtCore import Qt, QCoreApplication


# Project modules
from src.ui.login import Ui_Login
from src.system import SystemWindow
from Proyecto.popularInstitucion import ITBA



class LoginWindow(QMainWindow, Ui_Login):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)
        self.system_window = SystemWindow()

        self.btn_login.clicked.connect(self.validLogin)
        self.system_window.btn_logout.clicked.connect(self.logout)


    def validLogin(self):
        legajo_ingresado = int(self.input_legajo.text())
        contraseña_ingresada = self.input_pass.text()
        self.label_error.setText("")
        for alumno in ITBA.alumnos:
            if alumno.legajo == legajo_ingresado:
                alumno_elegido = alumno
        if alumno_elegido.contraseña == contraseña_ingresada:
            self.hide()
            # if self.label_tipo.text() == "ADMINISTRADOR":
            #     self.system_window.label_info.setText("Se ingresa como Administrador")
            if self.label_tipo.text() == "ALUMNO":
                self.system_window.label_info.setText("Se ingresa como Alumno")
            # else:
            #     self.system_window.label_info.setText("Se ingresa como Profesor")
            # self.system_window.show()
        else:
            self.label_error.setText("Los datos son incorrectos. Intente nuevamente")
    
    def logout(self):
        self.system_window.hide()
        self.label_error.setText("")
        self.input_legajo.setText("")
        self.input_pass.setText("")
        self.show()
    


