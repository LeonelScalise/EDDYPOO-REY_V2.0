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



    def validLegajoAlumno(self, institucion, legajo_ingresado):
        try:
            legajoingresado = int(legajo_ingresado)
        except ValueError:
            self.label_error.setText("El legajo ingresado debe ser un numero.")
            return False  # volve antes porque el codigo que sigue depende de la conversion

        if len(str(legajoingresado)) != 5:
            self.label_error.setText("El legajo debe ser de 5 digitos.")
            return False
        elif legajoingresado not in institucion.legajos_alumnos:
            self.label_error.setText("El legajo no existe.")
            return False

        return True

    def validLegajoAdminyProf(self, institucion, legajo_ingresado, rol = 'administrativo'):
        try:
            legajoingresado = legajo_ingresado.upper().strip()
        except ValueError:
            self.label_error.setText("El legajo ingresado debe ser un numero.")
            return False  # volve antes porque el codigo que sigue depende de la conversion
        
        if len(legajoingresado) != 7:
            self.label_error.setText("El legajo debe ser de 7 caracteres.")
            return False
        if rol == 'profesor':
                if legajoingresado[:2] != "PR":
                    self.label_error.setText("El legajo debe comenzar con las primeras dos letras de su rol.")
                    return False
                if legajoingresado not in institucion.legajos_profesores:
                    self.label_error.setText("El legajo no existe, intente nuevamente.")
                    return False
        else:
                if legajoingresado[:2] != "AD":
                    self.label_error.setText("El legajo debe comenzar con las primeras dos letras de su rol.")
                    return False
                if legajoingresado not in institucion.legajos_administrativos:
                    self.label_error.setText("El legajo no existe, intente nuevamente.") #si no cumple con la condición que se indica levanta un error con un mensaje
                    return False
        return True

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
                legajo_es_valido = self.validLegajoAdminyProf(ITBA, legajo_ingresado)
                if not legajo_es_valido:
                    return  # si el legajo no es valido no ejecutes lo siguiente
                
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
                legajo_es_valido = self.validLegajoAlumno(ITBA, legajo_ingresado)
                if not legajo_es_valido:
                    return  # si el legajo no es valido no ejecutes lo siguiente

                alumno_elegido = None
                for alumno in ITBA.alumnos:
                    if alumno.legajo == int(legajo_ingresado):
                        alumno_elegido = alumno
                
                if alumno_elegido and alumno_elegido.contraseña == contraseña_ingresada:
                    self.hide()
                    self.systemalu_window.label_info.setText(f"Logeado como {alumno_elegido.nombre_apellido}")
                    self.systemalu_window.show()
                # else:
                #     self.label_error.setText("Los datos son incorrectos. Intente nuevamente")
            
            else:
                legajo_es_valido = self.validLegajoAdminyProf(ITBA, legajo_ingresado, 'profesor')
                if not legajo_es_valido:
                    return  # si el legajo no es valido no ejecutes lo siguiente
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
    


