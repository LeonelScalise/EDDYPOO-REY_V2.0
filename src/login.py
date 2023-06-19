from math import inf
from PyQt5.QtWidgets import QMainWindow, QListWidgetItem, QColorDialog, QFileDialog, QStyle
from PyQt5.QtCore import Qt, QCoreApplication


# Project modules
from src.ui.login import Ui_Login
from src.systemadmin import SystemadminWindow
from ProyectoV2.popularInstitucion import ITBA
from ProyectoV2.popularPersona import *


class LoginWindow(QMainWindow, Ui_Login):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)
        self.system_window = SystemadminWindow()
        self.btn_login.clicked.connect(self.validLogin)
        self.system_window.btn_logout.clicked.connect(self.logout)


    def validLogin(self):
        try:
            ITBA.cargarDatos()
        except FileNotFoundError:
            pass
        legajo_ingresado = self.input_legajo.text()
        contraseña_ingresada = self.input_pass.text()

        if legajo_ingresado.isdigit():
            legajo_ingresado = int(legajo_ingresado)
        else:
            self.label_error.setText("El legajo debe ser un número.")

        self.label_error.setText("")
        alumno_elegido = None
        for alumno in ITBA.alumnos:
            if alumno.legajo == legajo_ingresado:
                alumno_elegido = alumno
        if alumno_elegido and alumno_elegido.contraseña == contraseña_ingresada:
            self.hide()
            # if self.label_tipo.text() == "ADMINISTRADOR":
            #     self.system_window.label_info.setText("Se ingresa como Administrador")
            if self.label_tipo.text() == "ALUMNO":
                self.system_window.label_info.setText("Se ingresa como Alumno")
            # else:
            #     self.system_window.label_info.setText("Se ingresa como Profesor")
            self.system_window.show()
        else:
            self.label_error.setText("Los datos son incorrectos. Intente nuevamente")
    
    def logout(self):
        ITBA.guardarDatos()
        self.system_window.hide()
        self.label_error.setText("")
        self.input_legajo.setText("")
        self.input_pass.setText("")
        self.show()
    


