from math import inf
from PyQt5.QtWidgets import QMainWindow, QListWidgetItem, QColorDialog, QFileDialog, QStyle
from PyQt5.QtCore import Qt, QCoreApplication


# Project modules
from src.ui.login import Ui_Login
from src.systemadmin import SystemadminWindow
from src.systemalu import SystemaluWindow
from src.systemprofe import SystemprofeWindow
from ProyectoV2.popularInstitucion import ITBA
from ProyectoV2.popularPersona import *


class LoginWindow(QMainWindow, Ui_Login):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)
        self.systemadmin_window = SystemadminWindow()
        self.systemalu_window = SystemaluWindow()
        self.systemprofe_window = SystemprofeWindow()

        self.btn_login.clicked.connect(self.validLogin)
        self.systemadmin_window.btn_logout_admin.clicked.connect(self.logout)
        self.systemalu_window.btn_logout_alu.clicked.connect(self.logout)
        self.systemprofe_window.btn_logout_profe.clicked.connect(self.logout)


    def validLogin(self):
        try:
            ITBA.cargarDatos()
        except FileNotFoundError:
            pass

        legajo_ingresado = self.input_legajo.text().upper()
        contraseña_ingresada = self.input_pass.text()

        if len(legajo_ingresado) == 0 or len(contraseña_ingresada) == 0:
            self.label_error.setText("Hay campos sin completar. Intente nuevamente")
        else:
            if self.label_tipo.text() == "ADMINISTRATIVO":
                admin_elegido = None
                for admin in ITBA.administrativos:
                    if admin.legajo == legajo_ingresado:
                        admin_elegido = admin
                
                if admin_elegido and admin_elegido.contraseña == contraseña_ingresada:
                    self.hide()
                    self.systemadmin_window.label_info.setText(f"Logeado como {admin_elegido.nombre_apellido}")
                    self.systemadmin_window.show()
                else:
                    self.label_error.setText("Los datos son incorrectos. Intente nuevamente")    
            
            elif self.label_tipo.text() == "ALUMNO":
                alumno_elegido = None
                for alumno in ITBA.alumnos:
                    if alumno.legajo == int(legajo_ingresado):
                        alumno_elegido = alumno
                
                if alumno_elegido and alumno_elegido.contraseña == contraseña_ingresada:
                    self.hide()
                    self.systemalu_window.label_info.setText(f"Logeado como {alumno_elegido.nombre_apellido}")
                    self.systemalu_window.show()
                else:
                    self.label_error.setText("Los datos son incorrectos. Intente nuevamente")
            
            else:
                profesor_elegido = None
                for profesor in ITBA.profesores:
                    if profesor.legajo == legajo_ingresado:
                        profesor_elegido = profesor
                
                if profesor_elegido and profesor_elegido.contraseña == contraseña_ingresada:
                    self.hide()
                    self.systemprofe_window.label_info.setText(f"Logeado como {profesor_elegido.nombre_apellido}")
                    self.systemprofe_window.show()
                else:
                    self.label_error.setText("Los datos son incorrectos. Intente nuevamente")
    
    def logout(self):
        ITBA.guardarDatos()
        self.systemadmin_window.hide()
        self.systemalu_window.hide()
        self.systemprofe_window.hide()
        self.label_error.setText("")
        self.input_legajo.setText("")
        self.input_pass.setText("")
        self.show()
    


