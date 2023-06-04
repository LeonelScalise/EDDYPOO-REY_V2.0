#from persona import *
from armado_menu import *
import os
from clasePersona import *
from popularPersona import *
from validadores import *

clear = lambda : os.system('cls')


def menu_principal():
    ITBA.cargarDatos() #Preguntar como arreglar lo de la Primera vez
    print(ITBA.tramites_abiertos)
    print(ITBA.administrativos[0].tramites_abiertos_admin)
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


  
