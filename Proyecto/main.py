import os
from armado_menu import armado_menu
from clasePersona import *
from validadores import validador
from popularPersona import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QBoxLayout, QWidget

clear = lambda : os.system('cls')

 #Funcion que despliega en menu principal en la terminal y ejecuta las funciones dependiendo del numero elegido
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

