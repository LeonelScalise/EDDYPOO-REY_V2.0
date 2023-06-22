from PyQt5.QtWidgets import QMainWindow, QListWidgetItem, QColorDialog, QFileDialog, QStyle
from PyQt5.QtCore import Qt, QCoreApplication


# Project modules
from src.ui.systemprofe import Ui_Systemprofe
from ProyectoV2.popularInstitucion import ITBA

class SystemprofeWindow(QMainWindow, Ui_Systemprofe):
    def __init__(self):
        super(SystemprofeWindow, self).__init__()
        self.setupUi(self)
        
        # Configuración botones del menu
        self.btn_subir_nota_final.clicked.connect(self.showWindowSubirNotaFinal)
        self.btn_modif_pass_profe.clicked.connect(self.showWindowCambiarContrasena)
        self.btn_iniciar_tramite_profe.clicked.connect(self.showWindowIniciarTramite)
    
    # Función para obtener el objeto profesor
    def obtenerProfesor(self):
        if len(self.label_info_usuario_log.text()) == 0:
            pass
        else:
            legajo_usuario = self.label_info_usuario_log.text()[-7:]
            for profesor in ITBA.profesores:
                if profesor.legajo == legajo_usuario:
                    return profesor
            
    # Funcion para resetar los labels de informe de Profesor
    def resetLabelsInforme(self):
        self.label_informe_modif_pass_profe.setText("")
        self.label_informe_ini_tram_profe.setText("")
        self.label_informe_subir_nota.setText("")

    # Funciones que activan los botones para cambiar los menus
    def showWindowSubirNotaFinal(self):
        self.stackedWidget.setCurrentWidget(self.page_subir_nota)

    def showWindowCambiarContrasena(self):
        self.stackedWidget.setCurrentWidget(self.page_modif_pass_profe)

    def showWindowIniciarTramite(self):
        self.stackedWidget.setCurrentWidget(self.page_iniciar_tramite_profe)
    
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