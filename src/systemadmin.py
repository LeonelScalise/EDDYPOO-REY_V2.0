from PyQt5.QtWidgets import QMainWindow, QListWidgetItem, QColorDialog, QFileDialog, QStyle
from PyQt5.QtCore import Qt, QCoreApplication


# Project modules
from src.ui.systemadmin import Ui_Systemadmin


class SystemadminWindow(QMainWindow, Ui_Systemadmin):
    def __init__(self):
        super(SystemadminWindow, self).__init__()
        self.setupUi(self)

        # Boton para cada Alta
        self.btn_alta_admin.clicked.connect(self.showWindowAltaAdmin)
        self.btn_alta_alu.clicked.connect(self.showWindowAltaAlu)
        self.btn_alta_profe.clicked.connect(self.showWindowAltaProfe)
        self.btn_alta_materia.clicked.connect(self.showWindowAltaMateria)
        self.btn_alta_comi.clicked.connect(self.showWindowAltaComi)
        self.btn_alta_carrera.clicked.connect(self.showWindowAltaCarrera)

        # Boton para cada Baja
        self.btn_baja_admin.clicked.connect(self.showWindowBajaAdmin)
        self.btn_baja_alu.clicked.connect(self.showWindowBajaAlu)
        self.btn_baja_profe.clicked.connect(self.showWindowBajaProfe)
        self.btn_baja_materia.clicked.connect(self.showWindowBajaMateria)
        self.btn_baja_comi.clicked.connect(self.showWindowBajaComi)

        # Boton para sección de Profesores
        self.btn_asig_profe.clicked.connect(self.showWindowAsignarProfe)
        self.btn_desasig_mat_profe.clicked.connect(self.showWindowDesasignarProfeMateria)
        self.btn_desasig_comi_profe.clicked.connect(self.showWindowDesasignarProfeComision)

        # Boton para sección de Modificaciones
        self.btn_modif_pass.clicked.connect(self.showWindowCambiarContrasena)
        self.btn_modif_nombre_mat.clicked.connect(self.showWindowModificarNombreMateria)
        self.btn_modif_nombre_carr.clicked.connect(self.showWindowModificarNombreCarrera)
        self.btn_modif_aluxcarr.clicked.connect(self.showWindowCambiarAlumnodeCarrera)

        # Boton para sección de Estadisticas
        self.btn_aluactxcarrera.clicked.connect(self.showWindowAlumnosActualesxCarrera)
        self.btn_rend_alu.clicked.connect(self.showWindowRendimientoAlumno)

        

    # Funciones para activar con botones - Alta
    def showWindowAltaAdmin(self):
        self.stackedWidget.setCurrentWidget(self.page_alta_admin)
    
    def showWindowAltaAlu(self):
        self.stackedWidget.setCurrentWidget(self.page_alta_alu)

    def showWindowAltaProfe(self):
        self.stackedWidget.setCurrentWidget(self.page_alta_profe)
    
    def showWindowAltaMateria(self):
        self.stackedWidget.setCurrentWidget(self.page_alta_materia)

    def showWindowAltaComi(self):
        self.stackedWidget.setCurrentWidget(self.page_alta_comi)
    
    def showWindowAltaCarrera(self):
        self.stackedWidget.setCurrentWidget(self.page_alta_carrera)

    # Funciones para activar con botones - Baja
    def showWindowBajaAdmin(self):
        self.stackedWidget_2.setCurrentWidget(self.page_baja_admin)
    
    def showWindowBajaAlu(self):
        self.stackedWidget_2.setCurrentWidget(self.page_baja_alu)

    def showWindowBajaProfe(self):
        self.stackedWidget_2.setCurrentWidget(self.page_baja_profe)
    
    def showWindowBajaMateria(self):
        self.stackedWidget_2.setCurrentWidget(self.page_baja_materia)

    def showWindowBajaComi(self):
        self.stackedWidget_2.setCurrentWidget(self.page_baja_comi)
    
    # Funciones para activar con botones - Sección Profes
    def showWindowAsignarProfe(self):
        self.stackedWidget_3.setCurrentWidget(self.page_asig_profe)
    
    def showWindowDesasignarProfeMateria(self):
        self.stackedWidget_3.setCurrentWidget(self.page_desasig_mat_profe)

    def showWindowDesasignarProfeComision(self):
        self.stackedWidget_3.setCurrentWidget(self.page_desasig_comi_profe)

    # Funciones para activar con botones - Sección Modificaciones
    def showWindowCambiarContrasena(self):
        self.stackedWidget_4.setCurrentWidget(self.page_passwords)
    
    def showWindowModificarNombreMateria(self):
        self.stackedWidget_4.setCurrentWidget(self.page_nombre_mat)

    def showWindowModificarNombreCarrera(self):
        self.stackedWidget_4.setCurrentWidget(self.page_nombre_carrera)

    def showWindowCambiarAlumnodeCarrera(self):
        self.stackedWidget_4.setCurrentWidget(self.page_aluxcarrera)

    # Funciones para activar con botones - Sección Estadisticas
    def showWindowAlumnosActualesxCarrera(self):
        self.stackedWidget_5.setCurrentWidget(self.page_aluactxcarrera)
    
    def showWindowRendimientoAlumno(self):
        self.stackedWidget_5.setCurrentWidget(self.page_rend_alu)

    


    