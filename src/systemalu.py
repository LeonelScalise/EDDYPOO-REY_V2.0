from PyQt5.QtWidgets import QMainWindow, QListWidgetItem, QColorDialog, QFileDialog, QStyle
from PyQt5.QtCore import Qt, QCoreApplication
import random
from datetime import *


# Project modules
from src.ui.systemalu import Ui_Systemalu
from ProyectoV2.popularInstitucion import ITBA
from ProyectoV2.claseTramite import Tramite


class SystemaluWindow(QMainWindow, Ui_Systemalu):
    def __init__(self):
        super(SystemaluWindow, self).__init__()
        self.setupUi(self)

        # Configuración botones del menu
        self.btn_inscr_mat_alu.clicked.connect(self.showWindowInscribirMateria)
        self.btn_desinscr_mat_alu.clicked.connect(self.showWindowDesinscribirMateria)
        self.btn_iniciar_tramite_alu.clicked.connect(self.showWindowIniciarTramite)
        self.btn_modif_pass_alu.clicked.connect(self.showWindowCambiarContrasena)
        self.btn_stats_academicas.clicked.connect(self.showWindowEstadisticasAcademicas)
        self.btn_cambiar_pass_alu.clicked.connect(self.cambiarContrasena)
        self.btn_ini_tram_alu.clicked.connect(self.iniciarTramite)
    
    
    # Funcion para resetar los labels de informe de Alumno
    def resetLabelsInforme(self):
        self.label_informe_desinscr_mat.setText("")
        self.label_informe_inscr_mat.setText("")
        self.label_informe_ini_tram_alu.setText("")
        self.label_informe_modif_pass_alu.setText("")
        
    # Funciones que activan los botones para cambiar los menus
    def showWindowInscribirMateria(self):
        self.stackedWidget.setCurrentWidget(self.page_inscr_mat)
        self.resetLabelsInforme()

    def showWindowDesinscribirMateria(self):
        self.stackedWidget.setCurrentWidget(self.page_desinscr_mat)
        self.resetLabelsInforme()

    def showWindowIniciarTramite(self):
        self.stackedWidget.setCurrentWidget(self.page_iniciar_tramite_alu)
        self.resetLabelsInforme()

    def showWindowCambiarContrasena(self):
        self.stackedWidget.setCurrentWidget(self.page_modif_pass_alu)
        self.resetLabelsInforme()

    def showWindowEstadisticasAcademicas(self):
        self.stackedWidget.setCurrentWidget(self.page_stats_academicas)
        self.resetLabelsInforme()
    
    # Función para obtener el objeto alumno
    def obtenerAlumno(self):
        if len(self.label_info_usuario_log.text()) == 0:
            pass
        else:
            legajo_usuario = int(self.label_info_usuario_log.text()[-5:])
            for alumno in ITBA.alumnos:
                if alumno.legajo == legajo_usuario:
                        return alumno
    
    # Función para establecer el color del texto
    def setTextColor(self, nombre_label, text, color):
        label = getattr(self, nombre_label)
        label.setText(text)
        label.setStyleSheet("color: %s;" % color)
        return label

    
    
    # Función para cambiar la contraseña del alumno
    def cambiarContrasena(self):
        alumno = self.obtenerAlumno()
        contraseña_actual = self.input_modif_pass_actual_alu.text()
        contraseña_nueva = self.input_new_pass_alu.text()

        if len(contraseña_actual) == 0 or len(contraseña_nueva) == 0:
            self.setTextColor("label_informe_modif_pass_alu","Hay campos sin completar.", "red")
            self.input_modif_pass_actual_alu.setText("")
            self.input_new_pass_alu.setText("")

        elif contraseña_actual == alumno.contraseña:
            alumno.contraseña = contraseña_nueva
            self.setTextColor("label_informe_modif_pass_alu","Se ha cambiado la contraseña exitosamente.", "green")
            self.input_modif_pass_actual_alu.setText("")
            self.input_new_pass_alu.setText("")
        else:
            self.setTextColor("label_informe_modif_pass_alu","La contraseña actual no es válida.", "red")
            self.input_modif_pass_actual_alu.setText("")
            self.input_new_pass_alu.setText("")
    

    # Función para mostrar el último tramite del alumno
    
    def ultimoTramiteAlumno(self):
        alumno = self.obtenerAlumno()
        tramites_alumno = []
        if len(ITBA.historial_tramites) != 0:
                for tramite in ITBA.historial_tramites:
                    if tramite.alumno.legajo == alumno.legajo:
                        tramites_alumno.append(tramite)

                ultimo_tramite = tramites_alumno[-1]
                self.label_info_ult_tramite_alu.setText("Información del último trámite:")
                self.label_ini_tram_alu_fini_en.setText("Fecha de inicio:")
                self.label_ini_tram_alu_asig_en.setText("Asignado a:")
                self.label_ini_tram_alu_estado_en.setText("Estado:")
                self.label_ini_tram_alu_fini.setText(f"{ultimo_tramite.fecha_de_inicio}")
                self.label_ini_tram_alu_asig.setText(f"{ultimo_tramite.administrativo}")
                self.label_ini_tram_alu_estado.setText(f"{ultimo_tramite.estado}")

    # Función para inciar tramite del alumno
    def iniciarTramite(self):
        alumno = self.obtenerAlumno()
        id_tramite = 0
        self.label_informe_ini_tram_alu.setText("")

        if len(self.input_motivo_tramite_alu.toPlainText()) == 0:
            self.setTextColor("label_informe_ini_tram_alu","Ingrese un motivo.", "red")
        else:
            if len(ITBA.historial_tramites) != 0:
                id_tramite = ITBA.historial_tramites[-1].id + 1


            tipo_de_tramite = str(self.input_motivo_tramite_alu.toPlainText())
            cantidad_administrativos = len(ITBA.administrativos)
            i_random = random.randint(0, cantidad_administrativos - 1)
            administrativo_asignado = ITBA.administrativos[i_random] #Se asigna el tramite a un administrativo random
            fecha_ingreso = datetime.strptime(datetime.today().strftime('%d/%m/%Y'), '%d/%m/%Y')
            nuevo_tramite = Tramite(id_tramite, alumno, administrativo_asignado,tipo_de_tramite,fecha_ingreso)
            administrativo_asignado.tramites_abiertos_admin.append(nuevo_tramite)
            ITBA.tramites_abiertos.append(nuevo_tramite)
            ITBA.historial_tramites.append(nuevo_tramite)
            alumno.tramites_abiertos_alu.append(nuevo_tramite)
            self.setTextColor("label_informe_ini_tram_alu","Ya iniciaste el trámite.", "green")
            self.label_info_ult_tramite_alu.setText("Información del último trámite:")
            self.label_ini_tram_alu_fini_en.setText("Fecha de inicio:")
            self.label_ini_tram_alu_asig_en.setText("Asignado a:")
            self.label_ini_tram_alu_estado_en.setText("Estado:")
            self.label_ini_tram_alu_fini.setText(f"{nuevo_tramite.fecha_de_inicio}")
            self.label_ini_tram_alu_asig.setText(f"{nuevo_tramite.administrativo}")
            self.label_ini_tram_alu_estado.setText(f"{nuevo_tramite.estado}")
            str(self.input_motivo_tramite_alu.setPlainText(""))
    









    


