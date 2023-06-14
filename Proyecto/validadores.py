import re
import os
from claseRegistroITBA import RegistroITBA
from popularInstitucion import ITBA
from datetime import *

def validadorAula():
    inicio = True
    patron = "^\s*[0-9]{1}[0]{1}[0-9]{1}(F|R|T){1}\s*$"
    while inicio:
        try:
            aula = input("\nIngrese el aula: ")
            if re.match(patron, aula, re.IGNORECASE) == None:
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
            if re.match(patron, dias, re.IGNORECASE) == None:
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


def validadorHorario(lista_dias):
    repe = len(lista_dias)
    inicio = True
    patron = fr"^\s*((0[0-9]|1[0-9]|2[0-3]):[0-5][0-9])\s*-\s*((0[0-9]|1[0-9]|2[0-3]):[0-5][0-9])(\s*,\s*((0[0-9]|1[0-9]|2[0-3]):[0-5][0-9])\s*-\s*((0[0-9]|1[0-9]|2[0-3]):[0-5][0-9])){{{repe-1}}}$"
    # patron = fr"^\s*(([0-1]\d)|(2[0-3])|([0-9]{{1}})):([0-5]\d)\s*[-]{{1}}\s*(([0-1]\d)|(2[0-3])|([0-9]{{1}})):([0-5]\d)(\s*[,]{{1}}\s*(([0-1]\d)|(2[0-3])|([0-9]{{1}})):([0-5]\d)\s*[-]{{1}}\s*(([0-1]\d)|(2[0-3])|([0-9]{{1}})):([0-5]\d)\s*){{{repe-1}}}$"
    # patron = fr"^\s*(([0-1]\d)|(2[0-3])|([0-9]{{2}})):([0-5]\d)\s*-\s*(([0-1]\d)|(2[0-3])|([0-9]{{2}})):([0-5]\d)(\s*,\s*(([0-1]\d)|(2[0-3])|([0-9]{{2}})):([0-5]\d)\s*-\s*(([0-1]\d)|(2[0-3])|([0-9]{{2}})):([0-5]\d)\s*){{{repe-1}}}$"
    while inicio:
        try:
            horario = input("\nIngrese el/los horario/s respectivamente a los días ingresados previamente. (Ejemplo: 08:30 - 12:40): ")
            if re.match(patron, horario) == None:
                raise Exception("\nIngrese un horario válido siguiendo el formato indicado y asegúrese de tener la misma cantidad de horarios que de días.\n")

            lista_horarios = horario.replace(" ", "").split(",")    

            for h in lista_horarios:
                hora_inicio, hora_fin = h.split("-")
                if hora_inicio >= hora_fin:
                    raise Exception("\nLa hora inicial debe ser menor que la hora final.\n")

            # Verifica si hay días repetidos
            if len(lista_dias) != len(set(lista_dias)):
                horarios_por_dia = {}
                for dia, horario in zip(lista_dias, lista_horarios):
                    if dia not in horarios_por_dia:
                        horarios_por_dia[dia] = [horario]
                    else:
                        # Verifica superposición de horarios
                        for h in horarios_por_dia[dia]:
                            if superposicion(h, horario):
                                raise Exception(f"\nSuperposición de horarios para el día {dia}.\n")
                        horarios_por_dia[dia].append(horario)

            inicio = False
        except ValueError:
            print('\nEl dato introducido no corresponde al valor esperado.\n')
        except Exception as e: 
            print(e)

    return lista_horarios

def superposicion(horario1, horario2):
    hora_inicio1, hora_fin1 = horario1.split("-")
    hora_inicio2, hora_fin2 = horario2.split("-")
    return hora_inicio1 < hora_fin2 and hora_fin1 > hora_inicio2


def validador(cant_opciones):
    inicio = True

    while inicio: #arranca el loop
        try: #intenta pedir una respuesta
            rta = int(input('\nIngresa una opción:'))
            if rta not in list(range(1, cant_opciones + 1)):
                raise Exception("\nNo es una opción válida.\n") #si no cumple con la condición que se indica levanta un error con un mensaje
            else:
                inicio = False #frena el loop si está todo ok
        except ValueError: #si ingresan un tipo de dato incorrecto no se rompe el sistema sino que te vuelve a pedir una rta.
            print('\nEl dato introducido no corresponde al valor esperado.\n')
        except Exception as e: 
            print(e) #imprime el mensaje que vos indicaste antes
    
    return rta


clear = lambda : os.system('cls')


def reintento():
    print("1. Reintentar\n2. Volver")
    eleccion = validador(2)
    if eleccion == 1:
        clear()
        return True
    elif eleccion == 2:
        clear()
        return False
        
    

def validadorLegajoAlumnos(institucion):
    inicio = True

    while inicio: #arranca el loop
        try: #intenta pedir una respuesta
            legajoingresado = int(input("Ingrese el numero de legajo: "))
            
            if len(str(legajoingresado)) != 5:
                raise Exception("\nEl legajo debe ser un numero de 5 digitos.\n") 
            if legajoingresado not in institucion.legajos_alumnos:
                raise Exception("\nEl legajo no existe, intente nuevamente.\n") #si no cumple con la condición que se indica levanta un error con un mensaje
            else:
                inicio = False #frena el loop si está todo ok
        except ValueError: #si ingresan un tipo de dato incorrecto no se rompe el sistema sino que te vuelve a pedir una rta.
            print('\nEl dato introducido no corresponde al valor esperado.\n')
            inicio = reintento()
        except Exception as e: 
            print(e)      #imprime el mensaje que vos indicaste antes
            inicio = reintento() 
    return legajoingresado

def validadorLegajoAdminyProf(institucion, rol = 'administrativo'):
    inicio = True
    while inicio: #arranca el loop
        try: #intenta pedir una respuesta
            legajoingresado = input(f'Ingrese el numero de legajo de {rol}: ').upper()
            
            if len(legajoingresado) != 7:
                raise Exception("\nEl legajo debe ser una cadena de 7 digitos.\n")
            if rol == 'profesor':
                if legajoingresado[:2] != "PR":
                    raise Exception("\nEl legajo debe comenzar con las primeras dos letras de su rol.\n")
                if legajoingresado not in institucion.legajos_profesores:
                    raise Exception("\nEl legajo no existe, intente nuevamente.\n") 
                else:
                    inicio = False
            else:
                if legajoingresado[:2] != "AD":
                    raise Exception("\nEl legajo debe comenzar con las primeras dos letras de su rol.\n")
                if legajoingresado not in institucion.legajos_administrativos:
                    raise Exception("\nEl legajo no existe, intente nuevamente.\n") #si no cumple con la condición que se indica levanta un error con un mensaje
                else:
                    inicio = False #frena el loop si está todo ok
        except ValueError: #si ingresan un tipo de dato incorrecto no se rompe el sistema sino que te vuelve a pedir una rta.
            print('\nEl dato introducido no corresponde al valor esperado.\n')
            inicio = reintento()
        except Exception as e: 
            print(e)      #imprime el mensaje que vos indicaste antes
            inicio = reintento() 
    return legajoingresado

def validadorNota():
    inicio = True
    while inicio:
        try:
            Nota_final = int(input("\nIngrese la nota final del alumno: "))
            if Nota_final > 10 or Nota_final < 1:
                raise Exception("\nLa nota debe ser un numero entero de 1 a 10.\n")
            else:
                inicio = False
        except ValueError:
                print('\nEl dato introducido no corresponde al valor esperado.\n')
        except Exception as e: 
                print(e)
    
    return Nota_final

def validadorSexo():
    inicio = True
    while inicio:
        try:
            sexo = input("\nIngrese el sexo (M/F): ")
            if sexo not in ["M", "F"]:
                raise Exception("\nEl sexo debe ser 'M' o 'F'.\n")
            else:
                inicio = False
        except ValueError:
                print('\nEl dato introducido no corresponde al valor esperado.\n')
        except Exception as e: 
                print(e)
    
    return sexo


def validadorCodigoMateria():
     inicio = True
     patron = "^\s*[0-9]{1}\s*[0-9]{1}\s*\.{1}\s*[0-9]{1}\s*[0-9]{1}\s*$"
     while inicio:
        try:
            codigo_de_materia = input("\nIngrese el codigo de la materia\nCuatro digitos separados por un punto (.) en la mitad (56.45): ")
            if re.match(patron, codigo_de_materia) == None:
                raise Exception("\nEl código no sigue el formato válido, inténtelo nuevamente.\n")
            else:
                inicio = False
            for carrera in ITBA.carreras:
                for materia in carrera.materias:
                    if materia.codigo_materia == codigo_de_materia:
                        raise Exception("\nEl código de la materia ya está asignado a otra materia, introduzca otro.\n")
        except ValueError:
                print('\nEl dato introducido no corresponde al valor esperado.\n')
        except Exception as e: 
                print(e)
     return codigo_de_materia

def validadorCreditos():
     inicio = True
     while inicio:
        try:
            creditos = int(str(input("Ingrese los creditos de la materia: ")).strip())
            if creditos > 6 or creditos < 1:
                raise Exception("\nLos créditos deben ser un dígito entre 1 y 6.\n")
            else:
                inicio = False       
        except ValueError:
             print('\nEl dato introducido no corresponde al valor esperado.\n')
        except Exception as e:
             print(e)
     return creditos

def validadorSede():
     inicio = True
     patron = "^(SDF|SDT|SDR)$"

     while inicio:
        try:
            sede = input("Ingrese la sede de cursada (SDF, SDT, SDR): ")
            if (re.match(patron, sede, re.IGNORECASE)) == None:
                     raise Exception("\nLa sede introducida no es una válida, inténtelo nuevamente.\n")
            else:
                inicio = False
        
        except ValueError:
             print('\nEl dato introducido no corresponde al valor esperado.\n')
        except Exception as e:
             print(e)
     return sede

def validadorCorrelativas():
     inicio = True
     while inicio:
        try:
            materias = []
            correlativas = input("Ingrese el nombre de las correlativas separadas por comas (,): ").replace(" ", "").split(",")

            for carrera in ITBA.carreras:
                for materia in carrera.materias:
                    materias.append(materia.nombre.lower().replace(" ", ""))
            for correlativa in correlativas:
                if correlativa.lower() not in materias:
                     raise Exception(f'La materia ingresada no se encuentra en el sistema, por favor ingrese una materia válida.\n')
                else:
                     inicio = False
        except ValueError:
             print('\nEl dato introducido no corresponde al valor esperado.\n')
        except Exception as e:
             print(e)
    
     return correlativas
                      


        
def validadorCodigoMateriaExistente():
    inicio = True
    while inicio:
        try:
            cod_materia = input("Ingrese el codigo de la materia: ")
            for carrera in ITBA.carreras:
                lista_cod_mat = [materia.codigo_materia for materia in carrera.materias if materia.codigo_materia == cod_materia]
                if len(lista_cod_mat) == 0:
                    raise Exception("Ingrese un codigo de materia existente.")
                else:
                    inicio = False
                    break


        except ValueError:
            print('\nEl dato introducido no corresponde al valor esperado.\n')
        except Exception as e:
            print(e)
    return cod_materia


















def validadorCodigoComisionExistente(cod_materia):
    inicio = True
    while inicio:
        try:
            cod_comision = input("Ingrese el codigo de la comision: ")
            for carrera in ITBA.carreras:
                for materia in carrera.materias:
                    if materia.codigo_materia == cod_materia:
                        c=0
                        for comision in materia.comisiones:
                            if comision.codigo_comision==cod_comision:
                                c+=1
                        if c==0:
                            raise Exception ("Ingrese un codigo de comisión existente.")
                        else:
                            inicio=False
                            break
        except ValueError:
            print('\nEl dato introducido no corresponde al valor esperado.\n')
        except Exception as e:
            print(e)
    return cod_comision


                         