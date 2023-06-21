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
    


        # self.systemadmin_window.cb_alta_mat_carrera
        esValidoLogin = self.btn_login.clicked.connect(self.validLogin)
        if esValidoLogin:
            self.cargarDatosCombobox('cb_alta_mat_carrera', 'systemadmin_window', ITBA, 'carreras')
        self.systemadmin_window.btn_logout_admin.clicked.connect(self.logout)
        self.systemalu_window.btn_logout_alu.clicked.connect(self.logout)
        self.systemprofe_window.btn_logout_profe.clicked.connect(self.logout)

        # Función para establecer el color del texto
    def setTextColor(self, nombre_label, text, color):
        label = getattr(self, nombre_label)
        label.setText(text)
        label.setStyleSheet("color: %s;" % color)
        return label

    def cargarDatosCombobox(self, nombre_combobox, nombre_ventana, institucion, attr_q_buscar):
        lista_valores = []
        institucionPuntoAtributo = getattr(institucion, attr_q_buscar)
        
        for elemento in institucionPuntoAtributo:
            lista_valores.append(elemento)
        
        ventana = getattr(self, nombre_ventana)
        combobox = getattr(ventana, nombre_combobox)

        combobox.clear()
        
        for valor in lista_valores:
            combobox.addItem(valor.nombre)


    def validLegajoAlumno(self, institucion, legajo_ingresado):
        try:
            legajoingresado = int(legajo_ingresado)
        except ValueError:
            self.setTextColor("label_error","El legajo ingresado debe ser un numero.", "red")
            return False  # volve antes porque el codigo que sigue depende de la conversion

        if len(str(legajoingresado)) != 5:
            self.setTextColor("label_error","El legajo debe ser de 5 digitos.", "red")
            return False
        elif legajoingresado not in institucion.legajos_alumnos:
            self.setTextColor("label_error","El legajo no existe. Intente nuevamente.", "red")
            return False

        return True

    def validLegajoAdminyProf(self, institucion, legajo_ingresado, rol = 'administrativo'):
        try:
            legajoingresado = legajo_ingresado.upper().strip()
        except ValueError:
            self.setTextColor("label_error","El legajo ingresado debe ser un numero.", "red")
            return False  # volve antes porque el codigo que sigue depende de la conversion
        
        if len(legajoingresado) != 7:
            self.setTextColor("label_error","El legajo debe ser de 7 caracteres.", "red")
            return False
        if rol == 'profesor':
                if legajoingresado[:2] != "PR":
                    self.setTextColor("label_error","El legajo debe comenzar con las primeras dos letras de su rol.", "red")
                    return False
                if legajoingresado not in institucion.legajos_profesores:
                    self.setTextColor("label_error","El legajo no existe. Intente nuevamente.", "red")
                    return False
        else:
                if legajoingresado[:2] != "AD":
                    self.setTextColor("label_error","El legajo debe comenzar con las primeras dos letras de su rol.", "red")
                    return False
                if legajoingresado not in institucion.legajos_administrativos:
                    self.setTextColor("label_error","El legajo no existe. Intente nuevamente.", "red") #si no cumple con la condición que se indica levanta un error con un mensaje
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
            self.setTextColor("label_error","Hay campos sin completar. Intente nuevamente.", "red")
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
                    self.systemadmin_window.label_info_usuario_log.setText(f"Logeado como {admin_elegido.nombre_apellido}")
                    self.systemadmin_window.show()
                    return True
                else:
                    self.setTextColor("label_error","Los datos son incorrectos. Intente nuevamente.", "red")
                    self.label_error.setText()    
            
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
                    self.systemalu_window.label_info_usuario_log.setText(f"Logeado como {alumno_elegido.nombre_apellido}")
                    self.systemalu_window.show()
                    return True
                else:
                    self.setTextColor("label_error","Los datos son incorrectos. Intente nuevamente.", "red")
            
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
                    self.systemprofe_window.label_info_usuario_log.setText(f"Logeado como {profesor_elegido.nombre_apellido}")
                    self.systemprofe_window.show()
                    return True
                else:
                    self.setTextColor("label_error","Los datos son incorrectos. Intente nuevamente.", "red")
    
    def logout(self):
        ITBA.guardarDatos()
        self.systemadmin_window.hide()
        self.systemalu_window.hide()
        self.systemprofe_window.hide()
        self.label_error.setText("")
        self.input_legajo.setText("")
        self.input_pass.setText("")
        self.show()
    


