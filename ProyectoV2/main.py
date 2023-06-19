import os
from ProyectoV2.armado_menu import armado_menu
from ProyectoV2.clasePersona import *
from ProyectoV2.validadores import validador
from ProyectoV2.popularPersona import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QBoxLayout, QWidget

clear = lambda : os.system('cls')

def menu_principal():
    try:
        ITBA.cargarDatos()
    except FileNotFoundError:
        print("No se encontraron datos previos")

    inicio = True
    while inicio:
        print("\n\t\tMENU PRINCIPAL\n\n1. Administrativo\n2. Alumno\n3. Profesor\n4. Salir")
        arranque = validador(4)
        clear()
        if arranque == 1:
            armado_menu("MENU ADMINISTRATIVO", ["Dar alta administrativo", "Iniciar sesion", "Salir"], [lambda : Administrativo.altaAdministrativo(ITBA), lambda : Administrativo.menu_registro_administrativo(ITBA)])
        elif arranque == 2:
            armado_menu("MENU ALUMNO", ["Iniciar Sesion", "Salir"], [lambda : Alumno.menu_registro_alumno(ITBA)])
        elif arranque == 3:
            armado_menu("MENU PROFESOR", ["Iniciar Sesion", "Salir"], [lambda : Profesor.menu_registro_profesor(ITBA)])
        elif arranque == 4:
            inicio = False
    
    ITBA.guardarDatos()                   
    
    print('Saliste del menu')

menu_principal()

##Prueba PYQT
# def load_data():
#     try:
#         ITBA.cargarDatos()
#     except FileNotFoundError:
#         QMessageBox.critical(win, "Error", "No se encontraron datos previos")

# def alta_administrativo():
#     lambda: Administrativo.altaAdministrativo(ITBA)

# def menu_registro_administrativo():
#     lambda: Administrativo.menu_registro_administrativo(ITBA)

# def menu_registro_alumno():
#     lambda: Alumno.menu_registro_alumno(ITBA)

# def menu_registro_profesor():
#     lambda: Profesor.menu_registro_profesor(ITBA)

# def save_data_and_exit():
#     ITBA.guardarDatos()
#     print('Saliste del menu')
#     app.exit()

# app = QApplication([])
# win = QMainWindow()
# win.setWindowTitle("Menu Principal")

# button_admin = QPushButton("Administrativo", clicked=menu_registro_administrativo)
# button_alumno = QPushButton("Alumno", clicked=menu_registro_alumno)
# button_profesor = QPushButton("Profesor", clicked=menu_registro_profesor)
# button_salir = QPushButton("Salir", clicked=save_data_and_exit)

# win.setCentralWidget(button_admin)  # establecer como widget central, esto debería modificarse para tu diseño

# win.statusBar().addWidget(button_alumno)
# win.statusBar().addWidget(button_profesor)
# win.statusBar().addWidget(button_salir)

# load_data()
# win.show()
# app.exec_()
