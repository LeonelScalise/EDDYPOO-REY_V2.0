import re
from popularInstitucion import *
from datetime import *

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


def validadorDia():
    inicio = True
    patron = "^\s*(lunes|martes|miercoles|jueves|viernes|sabado){1}\s*([,]{1}\s*(lunes|martes|miercoles|jueves|viernes|sabado){1}\s*)*$"
    while inicio:
        try:
            dias = input("\nIngrese el/los dia/s de la semana separados por (,): ")
            if re.match(patron, dias) == None:
                raise Exception("\nIngrese un dia de semana valido siguiendo el formato indicado.\n")
            else:
                inicio = False
        except ValueError:
                print('\nEl dato introducido no corresponde al valor esperado.\n')
        except Exception as e: 
                print(e)
    
    return dias

def validadorFecha():
    inicio = True
    while inicio:
        try:
            fecha = input(f'\nIngrese la fecha de nacimiento: ') 
            if datetime.strptime(fecha, '%d/%m/%Y'):
                if int(datetime.today().year) - int(datetime.strptime(fecha, '%d/%m/%Y').year) >= 18:
                    inicio = False
                else:
                    raise Exception("\nLa persona tiene que ser mayor de edad\n")
        except ValueError:
                print('\nIntroduzca una fecha con formato valido (dd/mm/yyyy)\n')
        except Exception as e: 
                print(e)
    
    return datetime.strptime(fecha, '%d/%m/%Y')
