from PyQt5.QtWidgets import QMainWindow, QListWidgetItem, QColorDialog, QFileDialog, QStyle
from PyQt5.QtCore import Qt, QCoreApplication


# Project modules
from src.ui.systemprofe import Ui_Systemprofe


class SystemprofeWindow(QMainWindow, Ui_Systemprofe):
    def __init__(self):
        super(SystemprofeWindow, self).__init__()
        self.setupUi(self)
        
        
        # Configuración botones del menu
        self.btn_subir_nota_final.clicked.connect(self.showWindowSubirNotaFinal)
        self.btn_modif_pass_profe.clicked.connect(self.showWindowCambiarContrasena)
        self.btn_iniciar_tramite_profe.clicked.connect(self.showWindowIniciarTramite)

    # Funciones que activan los botones para cambiar los menus
    def showWindowSubirNotaFinal(self):
        self.stackedWidget.setCurrentWidget(self.page_subir_nota)

    def showWindowCambiarContrasena(self):
        self.stackedWidget.setCurrentWidget(self.page_modif_pass_profe)

    def showWindowIniciarTramite(self):
        self.stackedWidget.setCurrentWidget(self.page_iniciar_tramite_profe)