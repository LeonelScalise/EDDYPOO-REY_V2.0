from PyQt5.QtWidgets import QMainWindow, QListWidgetItem, QColorDialog, QFileDialog, QStyle
from PyQt5.QtCore import Qt, QCoreApplication


# Project modules
from src.ui.systemprofe import Ui_Systemprofe
from ProyectoV2.popularInstitucion import ITBA
from ProyectoV2.claseTramite import Tramite
from datetime import *
import random

class SystemprofeWindow(QMainWindow, Ui_Systemprofe):
    def __init__(self):
        super(SystemprofeWindow, self).__init__()
        self.setupUi(self)
        
        # Configuración botones del menu
        self.btn_subir_nota_final.clicked.connect(self.showWindowSubirNotaFinal)
        self.btn_modif_pass_profe.clicked.connect(self.showWindowCambiarContrasena)
        self.btn_iniciar_tramite_profe.clicked.connect(self.showWindowIniciarTramite)
        self.btn_cambiar_pass_profe.clicked.connect(self.cambiarContrasena)
        self.btn_ini_tram_profe.clicked.connect(self.iniciarTramite)
    
    # Función para obtener el objeto profesor
    def obtenerProfesor(self):
        if len(self.label_info_usuario_log.text()) == 0:
            pass
        else:
            legajo_usuario = self.label_info_usuario_log.text()[-7:]
            for profesor in ITBA.profesores:
                if profesor.legajo == legajo_usuario:
                    return profesor
                
    # Función para establecer el color del texto
    def setTextColor(self, nombre_label, text, color):
        label = getattr(self, nombre_label)
        label.setText(text)
        label.setStyleSheet("color: %s;" % color)
        return label
    
    # Funcion para resetar los labels de informe de Profesor
    def resetLabelsInforme(self):
        self.label_informe_modif_pass_profe.setText("")
        self.label_informe_ini_tram_profe.setText("")
        self.label_informe_subir_nota.setText("")

    # Funciones que activan los botones para cambiar los menus
    def showWindowSubirNotaFinal(self):
        self.stackedWidget.setCurrentWidget(self.page_subir_nota)
        self.resetLabelsInforme()

    def showWindowCambiarContrasena(self):
        self.stackedWidget.setCurrentWidget(self.page_modif_pass_profe)
        self.resetLabelsInforme()

    def showWindowIniciarTramite(self):
        self.stackedWidget.setCurrentWidget(self.page_iniciar_tramite_profe)
        self.resetLabelsInforme()
    
    # Función para cambiar la contraseña del profesor
    def cambiarContrasena(self):
        profesor = self.obtenerProfesor()
        contraseña_actual = self.input_modif_pass_actual_profe.text()
        contraseña_nueva = self.input_new_pass_profe.text()

        if len(contraseña_actual) == 0 or len(contraseña_nueva) == 0:
            self.setTextColor("label_informe_modif_pass_profe","Hay campos sin completar.","red")
            self.input_modif_pass_actual_profe.setText("")
            self.input_new_pass_profe.setText("")

        elif contraseña_actual == profesor.contraseña:
            profesor.contraseña = contraseña_nueva
            self.setTextColor("label_informe_modif_pass_profe","Se ha cambiado la contraseña exitosamente.","green")
            self.input_modif_pass_actual_profe.setText("")
            self.input_new_pass_profe.setText("")
        else:
            self.setTextColor("label_informe_modif_pass_profe","La contraseña actual no es válida.","red")
            self.input_modif_pass_actual_profe.setText("")
            self.input_new_pass_profe.setText("")

   # Función para mostrar el último tramite del profesor
    
    def ultimoTramiteProfesor(self):
        profesor = self.obtenerProfesor()
        tramites_profesor = []
        if len(ITBA.historial_tramites) != 0:
                for tramite in ITBA.historial_tramites:
                    if tramite.profesor.legajo == profesor.legajo:
                        tramites_profesor.append(tramite)

                ultimo_tramite = tramites_profesor[-1]
                self.label_info_ult_tramite_profe.setText("Información del último trámite:")
                self.label_ini_tram_profe_fini_en.setText("Fecha de inicio:")
                self.label_ini_tram_profe_asig_en.setText("Asignado a:")
                self.label_ini_tram_profe_estado_en.setText("Estado:")
                self.label_ini_tram_profe_fini.setText(f"{ultimo_tramite.fecha_de_inicio}")
                self.label_ini_tram_profe_asig.setText(f"{ultimo_tramite.administrativo}")
                self.label_ini_tram_profe_estado.setText(f"{ultimo_tramite.estado}")

    # Función para inciar tramite del profesor
    def iniciarTramite(self):
        profesor = self.obtenerProfesor()
        id_tramite = 0
        self.label_informe_ini_tram_profe.setText("")

        if len(self.input_motivo_tramite_profe.toPlainText()) == 0:
            self.setTextColor("label_informe_ini_tram_profe","Ingrese un motivo.", "red")
        else:
            if len(ITBA.historial_tramites) != 0:
                id_tramite = ITBA.historial_tramites[-1].id + 1


            tipo_de_tramite = str(self.input_motivo_tramite_profe.toPlainText())
            cantidad_administrativos = len(ITBA.administrativos)
            i_random = random.randint(0, cantidad_administrativos - 1)
            administrativo_asignado = ITBA.administrativos[i_random] #Se asigna el tramite a un administrativo random
            fecha_ingreso = datetime.strptime(datetime.today().strftime('%d/%m/%Y'), '%d/%m/%Y')
            nuevo_tramite = Tramite(id_tramite, profesor, administrativo_asignado,tipo_de_tramite,fecha_ingreso)
            administrativo_asignado.tramites_abiertos_admin.append(nuevo_tramite)
            ITBA.tramites_abiertos.append(nuevo_tramite)
            ITBA.historial_tramites.append(nuevo_tramite)
            profesor.tramites_abiertos_profe.append(nuevo_tramite)
            self.setTextColor("label_informe_ini_tram_profe","Ya iniciaste el trámite.", "green")
            self.label_info_ult_tramite_profe.setText("Información del último trámite:")
            self.label_ini_tram_profe_fini_en.setText("Fecha de inicio:")
            self.label_ini_tram_profe_asig_en.setText("Asignado a:")
            self.label_ini_tram_profe_estado_en.setText("Estado:")
            self.label_ini_tram_profe_fini.setText(f"{nuevo_tramite.fecha_de_inicio}")
            self.label_ini_tram_profe_asig.setText(f"{nuevo_tramite.administrativo}")
            self.label_ini_tram_profe_estado.setText(f"{nuevo_tramite.estado}")
            str(self.input_motivo_tramite_profe.setPlainText(""))