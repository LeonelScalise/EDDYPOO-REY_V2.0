import re

def validadorAula():
    inicio = True
    patron = "^\s*[0-9]{1}[0]{1}[0-9]{1}[T,R,F]\s*$"
    while inicio:
        try:
            aula = input("\nIngrese el aula: ")
            if re.match(patron, aula) == None:
                raise Exception("\nEl aula no existe, ingrese un aula valida.\n")
            else:
                inicio = False
        except ValueError:
                print('\nEl dato introducido no corresponde al valor esperado.\n')
        except Exception as e: 
                print(e)
    
    return aula

from popularInstitucion import *

def validadorDNI():
    inicio = True
    while inicio:
        try:
            DNI = int(input("\nIngrese el DNI: "))
            if len(str(DNI)) != 8:
                raise Exception("\nEl DNI debe tener 8 digitos.\n")
            for alumno in ITBA.alumnos:
                 if alumno.dni == DNI:
                      raise Exception("\nEl DNI ya existe, intentalo nuevamente.")
            else:
                inicio = False
        except ValueError:
                print('\nEl dato introducido no corresponde al valor esperado.\n')
        except Exception as e: 
                print(e)
    
    return DNI
