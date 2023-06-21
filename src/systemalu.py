from PyQt5.QtWidgets import QMainWindow, QListWidgetItem, QColorDialog, QFileDialog, QStyle
from PyQt5.QtCore import Qt, QCoreApplication


# Project modules
from src.ui.systemalu import Ui_Systemalu


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
        
    # Funciones que activan los botones para cambiar los menus
    def showWindowInscribirMateria(self):
        self.stackedWidget.setCurrentWidget(self.page_inscr_mat)

    def showWindowDesinscribirMateria(self):
        self.stackedWidget.setCurrentWidget(self.page_desinscr_mat)

    def showWindowIniciarTramite(self):
        self.stackedWidget.setCurrentWidget(self.page_iniciar_tramite_alu)

    def showWindowCambiarContrasena(self):
        self.stackedWidget.setCurrentWidget(self.page_modif_pass_alu)

    def showWindowEstadisticasAcademicas(self):
        self.stackedWidget.setCurrentWidget(self.page_stats_academicas)

    