# importación de las bibliotecas necesarias
import os
import random
import matplotlib.pyplot as plt
from string import ascii_uppercase
# importación de las funciones y clases propias del sistema
from armado_menu import armado_menu
from claseRegistroITBA import RegistroITBA
from claseTramite import Tramite
from popularInstitucion import ITBA
from getbyId import getbyId
from claseComision import Comision
from claseCarrera import Carrera
from validadores import *
from claseMateria import Materia

# función para limpiar la pantalla de la consola
clear = lambda : os.system('cls')

# clase Persona con los atributos base
class Persona:
  def __init__(self, nombre_apellido, dni, sexo, fecha_nac):
    self.dni=dni
    self.nombre_apellido = nombre_apellido
    self.sexo = sexo
    self.fecha_nac = fecha_nac

# clase Alumno que hereda de Persona
class Alumno(Persona):

  # método de clase para registrar al alumno en el sistema
  def menu_registro_alumno(institucion:RegistroITBA):
    inicio = True
    while inicio:
      x = "o"
      legajo_ingresado = validadorLegajoAlumnos(institucion)
      contraseña_ingresada = input("Contraseña: ")
      clear()
      # Bucle que valida el legajo y contraseña ingresados por el alumno
      for alumno in institucion.alumnos:
          if alumno.legajo == legajo_ingresado and alumno.contraseña == contraseña_ingresada:
            if alumno.sexo == "F":
              x = "a"
            return armado_menu(f"Bienvenid{x} {alumno.nombre_apellido}", ["Inscripcion a materia", "Desinscripción a materia", "Iniciar Tramite", "Cambiar contraseña", "Estadisticas", "Materias Aprobadas", "Volver"], [lambda : alumno.displayMateriasDisponibles(), lambda : alumno.desinscribirMateria() , lambda : alumno.iniciarTramite(ITBA), lambda : alumno.actualizarContraseña(), lambda : alumno.estadisticasAlumno(), lambda: alumno.materiasAprobadas()])

          elif alumno.legajo == legajo_ingresado:
            print("La contraseña es incorrecta. Intente nuevamente o consulte en Administración")
            print("\n1. Reintentar\n2. Volver")
            opcion_elegida=validador(2)
            clear()
            if opcion_elegida == 2:
                inicio = False

  # inicializador de la clase Alumno
  def __init__(self, nombre_apellido, dni, sexo, contraseña, fecha_nac, legajo,fecha_ingreso,estado_alumno="Activo", carrera=None, fecha_baja = None):
    super().__init__(nombre_apellido, dni, sexo, fecha_nac)
    self.legajo = legajo
    self.materias_aprobadas = []
    self.materias_en_curso = []
    self.comisiones_en_curso = []
    self.fecha_ingreso = fecha_ingreso
    self.carrera = carrera
    self.fecha_baja = fecha_baja
    self.creditos_aprobados = 0
    self.historial_academico = {}
    self.estado_alumno = estado_alumno
    self.tramites_abiertos_alu = []
    self.tramites_resueltos_alu = []
    self.contraseña = contraseña

 
  # Devuelve una representación legible de la instancia de la clase Alumno cuando se convierte en cadena de texto.
  def __str__(self):
    return self.nombre_apellido
  

  def iniciarTramite(self, institucion):
    id_tramite = 0

    # Verificar si existen trámites previos para asignar un nuevo ID
    if len(institucion.historial_tramites) != 0:
      id_tramite= institucion.historial_tramites[-1].id + 1
    tipo_de_tramite = input("Ingrese el motivo del tramite o 'exit' si no quiere iniciar tramite: ")
    if tipo_de_tramite == 'exit':
      return print("No se inició tramite") 
    else:
      cantidad_administrativos = len(institucion.administrativos)
      i_random = random.randint(0, cantidad_administrativos - 1)
      administrativo_asignado=institucion.administrativos[i_random]
      # Crear un nuevo objeto Tramite y asignarlo al administrativo y al alumno
      nuevo_tramite = Tramite(id_tramite, self, administrativo_asignado,tipo_de_tramite,"24/4/2023")
      administrativo_asignado.tramites_abiertos_admin.append(nuevo_tramite)
      institucion.tramites_abiertos.append(nuevo_tramite)
      institucion.historial_tramites.append(nuevo_tramite)
      self.tramites_abiertos_alu.append(nuevo_tramite)
      return print("Ya iniciaste el tramite")

#Este metodo permite que un alumno se inscriba en una materia
  def inscribirMateria(self, materia):
    contador = 0
    flag = True

    print(f"\t\t\nComisiones disponibles para inscripcion en {materia.nombre}\n")
    if len(materia.comisiones) != 0:
      horarios_inscripcion_actual = []
      for comision_inscripcion_actual in self.comisiones_en_curso:
        horarios_inscripcion_actual.append(comision_inscripcion_actual.dia_y_horario)

      while flag:
        for comisiones in materia.comisiones:
          contador += 1
        print(f"{contador}. {comisiones.codigo_comision}: {comisiones.dia_y_horario}")

        print(f"{contador + 1}. Volver")

        opcion_elegida = validador(contador + 1)
        clear()

        if opcion_elegida == contador + 1:
          flag = False
        else:
          comision = materia.comisiones[opcion_elegida - 1]

          # Validar superposición de horarios
          for horario_inscripcion in horarios_inscripcion_actual:
            if any(dia in horario_inscripcion['Dia'] for dia in comision.dia_y_horario['Dia']):
              for i in range(len(horario_inscripcion['Horario'])):
                for j in range(len(comision.dia_y_horario['Horario'])):
                  horario_existente = horario_inscripcion['Horario'][i].split('-')
                  horario_nuevo = comision.dia_y_horario['Horario'][j].split('-')

                  if (horario_nuevo[0] < horario_existente[1] and horario_nuevo[1] > horario_existente[0]):
                    clear()
                    print("No puedes inscribirte en esta comision por superposicion de horarios")
                    return

          comision.alumnos.append(self)
          materia.alumnos.append(self)
          self.materias_en_curso.append(materia)
          self.comisiones_en_curso.append(comision)
          clear()
          flag = False
          print(f"Te has inscripto correctamente a la comision {comision.codigo_comision} de la materia {materia.nombre}")
    else:
        print("La materia no posee comisiones por el momento")

  # Metodo que despliega las materias a las que un alumno puede inscribirse
  def displayMateriasDisponibles(self):
    materias_disponibles = []
    c1 = 0
    c2 = 0
    flag = True
    # Mostrar las materias disponibles para inscripción
    print(f"\t\t\nMaterias disponibles para inscripcion de {self.nombre_apellido}\n")
    # Verificar si las materias tienen correlativas y si están disponibles para inscripción
    for materia in self.carrera.materias:
      if len(materia.correlativas) != 0:
        for corre in materia.correlativas:
          if corre in self.materias_aprobadas:
            c1 += 1 #sirve para verificar si es igual a la cantidad de correlativas que tiene la materia, eso implicaría que tiene todas las correlativas aprobadas
        if c1 == len(materia.correlativas) and materia not in self.materias_aprobadas and materia not in self.materias_en_curso:
            materias_disponibles.append(materia)
      elif materia not in self.materias_aprobadas and materia not in self.materias_en_curso:
        materias_disponibles.append(materia)

    while flag:
      for materia in materias_disponibles:
        c2 += 1
        print(f"{c2}. {materia.codigo_materia} {materia.nombre}")

      print(f"{c2 + 1}. Volver")
      opcion_elegida = validador(c2 + 1)
      clear()
      if opcion_elegida == c2 + 1:
        flag = False
      else:
        self.inscribirMateria(materias_disponibles[opcion_elegida - 1])
        flag = False
  
  # Metodo que permite la desiscripcion de una materia (alumno)
  def desinscribirMateria(self):
    contador = 0
    flag = True
    print("Materias en las que está inscripto\n")
    if len(self.materias_en_curso) != 0:
      while flag:
        for materia in self.materias_en_curso:
          contador += 1
          print(f"{contador}. {materia.codigo_materia} {materia.nombre}")
        
        print(f"{contador + 1}. Volver")

        opcion_elegida = validador(contador + 1)
        clear()

        if opcion_elegida == contador + 1:
          flag = False
        else:
          materia_elegida = self.materias_en_curso[opcion_elegida - 1]
          clear()
          flag = False
          self.materias_en_curso.remove(materia_elegida)
          materia_elegida.alumnos.remove(self)
          for comision in materia_elegida.comisiones:
              if self in comision.alumnos:
                comision.alumnos.remove(self)
          print(f"Ya no se encuentra inscripto en {materia_elegida.nombre}")

    else:
      print("No se encuentra anotado en ninguna materia")

  # Metodo que muestra el menu de las estadisticas el alumno puede observar en el sistema
  def estadisticasAlumno(self):
    armado_menu("ESTADISTICAS DEL ALUMNO", ['Ver el promedio de la carrera', "Volver"], [lambda : self.verPromedioCarrera()])
  
  # Metodo que muestra el promedio de carrera del alumno
  def verPromedioCarrera(self):
    suma = 0
    cantidad_notas = 0
    promedio = 0

    for nota in self.historial_academico.values():
      suma += nota
      cantidad_notas += 1
    
    if cantidad_notas != 0:
      promedio = suma / cantidad_notas
      return print(f"Promedio lineal de la carrera: {promedio}")
    
    else:
      print(f"{self.nombre_apellido} no tiene notas cargadas por el momento")
  
  # Metodo que le permite al alumno actualizar su contraseña
  def actualizarContraseña(self):
    contraseña_nueva = input("Ingrese su contraseña nueva: ")
    self.contraseña = contraseña_nueva
    print("Su contraseña ha sido modificada exitosamente")
    
  # Metodo que le permite al alumno ver las materias que tiene aprobadas
  def materiasAprobadas(self):
    flag=True
    print("\t\t\nMaterias Aprobadas\t\t\n")
    while flag:
        for materia in self.materias_aprobadas:
          print(f"{materia.codigo_materia} {materia.nombre}")
        
        print(f"1. Volver")
        opcion_elegida = validador(1)
        clear()
        if opcion_elegida == 1:
            flag = False

#Inicializacion clase Profes
class Profesor(Persona):
  def menu_registro_profesor(institucion:RegistroITBA):
    inicio = True
    while inicio:
      x = "o"
      legajo_ingresado = validadorLegajoAdminyProf(institucion, 'profesor')
      contraseña_ingresada = input("Contraseña: ")
      clear()
      for prof in institucion.profesores:
          if prof.legajo == legajo_ingresado and prof.contraseña == contraseña_ingresada:
            if prof.sexo == "F":
              x = "a"
              # Retorna el menú de opciones para el profesor
            return armado_menu(f"Bienvenid{x} {prof.nombre_apellido}", ["Subir nota final", "Iniciar Tramite", "Cambiar contraseña", "Volver"], [lambda : prof.displayMateriasActivas(), lambda: prof.iniciarTramite(ITBA), lambda : prof.actualizarContraseña()])
          elif prof.legajo == legajo_ingresado:
              print("La contraseña es incorrecta. Intente nuevamente o consulte en Administración")
              print("\n1. Reintentar\n2. Volver")
              opcion_elegida=validador(2)
              clear()
              if opcion_elegida == 2:
                  inicio = False

  def __init__(self, nombre_apellido, dni, sexo, contraseña, fecha_nac, legajo, fecha_ingreso, fecha_baja = None):
    super().__init__(nombre_apellido, dni, sexo, fecha_nac)
    self.legajo = legajo
    self.fecha_ingreso = fecha_ingreso
    self.fecha_baja = fecha_baja
    self.comisiones_a_cargo = []
    self.tramites_abiertos_profe = []
    self.tramites_resueltos_profe = []
    self.contraseña = contraseña


  #Este metodo permite que el profesor inicie un tramite
  def iniciarTramite(self, institucion):
    id_tramite = 0

    if len(institucion.historial_tramites) != 0:
      id_tramite= institucion.historial_tramites[-1].id + 1
    tipo_de_tramite = input("Ingrese el motivo del tramite o 'exit' si no quiere iniciar tramite: ")
    if tipo_de_tramite == 'exit':
      return print("No se inició tramite") 
    else:
      cantidad_administrativos = len(institucion.administrativos)
      i_random = random.randint(0, cantidad_administrativos - 1)
      administrativo_asignado=institucion.administrativos[i_random]
      nuevo_tramite = Tramite(id_tramite, None, administrativo_asignado,tipo_de_tramite,"24/4/2023", self)
      administrativo_asignado.tramites_abiertos_admin.append(nuevo_tramite)
      institucion.tramites_abiertos.append(nuevo_tramite)
      institucion.historial_tramites.append(nuevo_tramite) 
      self.tramites_abiertos_profe.append(nuevo_tramite)
      return print("Ya iniciaste el tramite")


  # Este metodo permite que el profesor suba la nota final de un alumno
  def subirNotaFinal(self, materia):
    comisiones_a_cargo = []
    contador = 0
    flag = True
    print("Seleccione la comision a la que desea subir la nota final:\n")
    for comision in materia.comisiones:
      if self == comision.profesor:
        comisiones_a_cargo.append(comision)  # Agregar comisiones a cargo del profesor
    while flag:
      for comision in comisiones_a_cargo:
        contador += 1
        print(f"{contador}. Comision {comision.codigo_comision} de {materia.nombre}")
      
      print(f"{contador + 1}. Volver")

      opcion_elegida1 = validador(contador + 1) # Obtener la opción elegida por el usuario
      clear()

      if opcion_elegida1 == contador + 1:
        flag = False
        comision_elegida = None  # El usuario eligió volver, no se selecciona ninguna comisión
      else:
        comision_elegida = comisiones_a_cargo[opcion_elegida1 - 1] # Obtener la comisión elegida por el usuario
        clear()
        flag = False

    if comision_elegida is not None:
      contador = 0
      flag = True
      print("Seleccione el alumno al que desea subir la nota final:\n")
      if len(comision_elegida.alumnos) != 0:
        while flag:
          for alumno in comision_elegida.alumnos:
            contador += 1
            print(f"{contador}. {alumno.nombre_apellido}")
          
          print(f"{contador + 1}. Volver")

          opcion_elegida2 = validador(contador + 1) # Obtener la opción elegida por el usuario
          clear()

          if opcion_elegida2 == contador + 1:
            flag = False # El usuario eligió volver, finalizo el bucle
          else:
            clear()
            alumno_elegido = comision_elegida.alumnos[opcion_elegida2 - 1] # Obtener el alumno elegido
            Nota_final = validadorNota() # Solicitar la nota final al usuario
            alumno_elegido.historial_academico[materia.nombre] = Nota_final  # Actualizar el historial académico del alumno
            flag = False
            if Nota_final >= 4: # El alumno aprobó la materia
              alumno_elegido.materias_aprobadas.append(materia) # Agregar la materia aprobada al alumno
              alumno_elegido.materias_en_curso.remove(materia) # Eliminar la materia de las materias en curso
              materia.alumnos.remove(alumno_elegido) # Eliminar al alumno de la lista de alumnos de la materia
              alumno_elegido.comisiones_en_curso.remove(comision_elegida) # Eliminar la comisión en curso del alumno
              comision_elegida.alumnos.remove(alumno_elegido) # Eliminar al alumno de la lista de alumnos de la comisión
              alumno_elegido.creditos_aprobados += materia.creditos  # Incrementar los créditos aprobados del alumno
              print(f"La nota final se cargó correctamente. {alumno_elegido} aprobó {materia.nombre}")
            else:
              print(f"La nota final se cargó correctamente. {alumno_elegido} no aprobó {materia.nombre}")
      else:
        print("No hay alumnos en esta comision")
  
  # Metodo que despliega las materias activas del profesor
  def displayMateriasActivas(self):
    contador = 0
    materias_activas = []
    flag = True
    print("Materias a las que está inscripto\n")
    for carrera in ITBA.carreras:
      for materia in carrera.materias:
        if self in materia.profesores:
          materias_activas.append(materia)
    while flag:
      for materia in materias_activas:
        contador += 1
        print(f"{contador}. {materia.codigo_materia} {materia.nombre}")

      print(f"{contador + 1}. Volver")

      opcion_elegida = validador(contador + 1)
      clear()

      if opcion_elegida == contador + 1:
        flag = False
      else:
        clear()
        flag = False
        self.subirNotaFinal(materias_activas[opcion_elegida - 1])
      
  #Este metodo permite actualizar la contrasena del profesor
  def actualizarContraseña(self):
    contraseña_nueva = input("Ingrese su contraseña nueva: ")
    self.contraseña = contraseña_nueva
    print("Su contraseña ha sido modificada exitosamente")

class Administrativo(Persona):

  #Metodo que le permite a un administrativo dar de alta
  def altaAdministrativo(institucion:RegistroITBA):
        
        nombre_apellido = input("Ingrese el nombre y apellido del administrativo: ")
        dni = validadorDNI()
        fecha_nac = validadorFecha()
        sexo = validadorSexo()
        contraseña = str(dni)
        if len(ITBA.legajos_administrativos) != 0:
          legajo_numero = int(ITBA.legajos_administrativos[-1][2:])+1
          legajo_alfa = "AD"
          legajo = legajo_alfa + str(legajo_numero)
        else:
          legajo="AD10000"
        fecha_ingreso = datetime.strptime(datetime.today().strftime('%d/%m/%Y'), '%d/%m/%Y')

        institucion.administrativos.append(Administrativo(nombre_apellido, dni, sexo, contraseña, fecha_nac, legajo, fecha_ingreso))
        institucion.legajos_administrativos.append(legajo)
        clear()
        print(f'El administrativo {nombre_apellido} se ha creado correctamente')
        print(f"El legajo del administrativo es: {legajo} y la contraseña es su dni: {contraseña}")
  
  # Metodo que valida el registro del administrativo
  def menu_registro_administrativo(institucion:RegistroITBA):
    inicio = True
    while inicio:
      x = "o"
      legajo_ingresado = validadorLegajoAdminyProf(institucion)
      contraseña_ingresada = input("Contraseña: ")
      clear()
      for admin in institucion.administrativos:
          if admin.legajo == legajo_ingresado and admin.contraseña == contraseña_ingresada:
            if admin.sexo == "F":
              x = "a"
            return armado_menu(f"Bienvenid{x} {admin.nombre_apellido}", ["Dar de alta alumno", "Dar de baja alumno", "Dar de alta profesor", "Dar de baja profesor","Dar de baja Administrativo", "Tramites","Crear Comisión", "Dar de baja una Comisión", "Asignar profesor a materia", "Desasignar profesor a materia", "Alta de Materia", "Baja de Materia", "Crear nueva carrera" ,"Estadisticas", "Cambiar contraseña", "Volver"], [lambda : admin.altaAlumno(), lambda : admin.bajaAlumno(), lambda : admin.altaProfesor(), lambda : admin.bajaProfesor(), lambda : admin.bajaAdministrativo(), lambda : admin.displayTramiteActivo(), lambda:admin.crearComision(), lambda: admin.bajaComision(), lambda : admin.asignarProfesor(), lambda : admin.desasignarProfesor(), lambda : admin.crearMateria(), lambda : admin.bajaMateria(), lambda : admin.altaCarrera(ITBA), lambda : admin.estadisticasGenerales(), lambda : admin.actualizarContraseña(ITBA)])
          elif admin.legajo == legajo_ingresado:
                print("La contraseña es incorrecta. Intente nuevamente o consulte con otro administrador")
                print("\n1. Reintentar\n2. Volver")
                opcion_elegida=validador(2)
                clear()
                if opcion_elegida == 2:
                    inicio = False
  
  
  def __init__(self, nombre_apellido, dni, sexo, contraseña, fecha_nac, legajo, fecha_ingreso, fecha_baja=None):
    super().__init__(nombre_apellido, dni, sexo, fecha_nac)
    self.legajo = legajo
    self.fecha_ingreso = fecha_ingreso
    self.fecha_baja = fecha_baja
    self.tramites_abiertos_admin = []
    self.tramites_resueltos_admin = []
    self.contraseña = contraseña

#Este metodo permite asignar al profesor a una materia o comision
  def asignarProfesor(self):
    contador = 0
    flag1 = False
    flag2 = True
    legajo_profesor = validadorLegajoAdminyProf(ITBA,"profesor")
    materias_disponibles = []
    for profesor in ITBA.profesores:
      if profesor.legajo == legajo_profesor:
        profesor_elegido = profesor
        clear()
    print("Materias a las que se lo puede asignar\n")
    while flag2:
      for carrera in ITBA.carreras:
        for materia in carrera.materias:
            if len(materia.comisiones) > 0:
              for comision in materia.comisiones:
                if comision.profesor == None:
                  flag1 = True
            if flag1:
              contador += 1
              materias_disponibles.append(materia)
              print(f"{contador}. {materia.codigo_materia} {materia.nombre}")
              flag1 = False

      if len(materias_disponibles) == 0:
        print("No hay materias disponibles para asignar al profesor")
        flag2 = False
      else:
        print(f"{contador + 1}. Volver")
        opcion_elegida1 = validador(contador + 1)
        if opcion_elegida1 == contador + 1:
          flag2 = False
        else:
          materia_elegida = materias_disponibles[opcion_elegida1 - 1]
          clear()
          flag2 = False

        print(f"Comisiones de {materia_elegida.nombre} a las que se lo puede asignar\n")
    
        contador = 0
        flag2 = True    

        while flag2:
          for comision in materia_elegida.comisiones:
            if comision.profesor == None:
              contador += 1
              print(f"{contador}. Comision {comision.codigo_comision} de {materia_elegida.nombre}")

          print(f"{contador + 1}. Volver")

          opcion_elegida2 = validador(contador + 1)
          if opcion_elegida2 == contador + 1:
              flag2 = False
          else:
            comision_elegida = materia_elegida.comisiones[opcion_elegida2 - 1]
            comision_elegida.profesor = profesor_elegido
            if profesor_elegido not in materia_elegida.profesores:
              materia_elegida.profesores.append(profesor_elegido)
            flag2 = False
        
          print(f"Se ha asignado correctamente a {profesor_elegido.nombre_apellido} a la comision {comision_elegida.codigo_comision} de {materia_elegida.nombre}")

#Este metodo permite desasignar a un profesor de una materia o comision
  def desasignarProfesor(self):
    materias_de_profesor = []
    c1 = 0
    c2 = 0
    legajo_profesor = validadorLegajoAdminyProf(ITBA,"profesor")
    if legajo_profesor not in ITBA.legajos_profesores:
      return 
    for profesor in ITBA.profesores:
      if profesor.legajo == legajo_profesor:
        profesor_elegido = profesor
        clear()

    for carrera in ITBA.carreras:
        for materia in carrera.materias:
          for profesor in materia.profesores:
            if profesor.legajo == legajo_profesor:
              if materia not in materias_de_profesor:
                materias_de_profesor.append(materia)

    print(f'¿Quiere desasignar a {profesor_elegido.nombre_apellido} de una materia o de una comisión en específico?\n\n1. Materia\n2. Comision\n')
    
    opcion_elegida1 = validador(2)

    if opcion_elegida1 == 1:

      if len(materias_de_profesor) == 0:
        print("El profesor no tiene materias asignadas.")
      else:

        print(f'Elija materia para desasignar a {profesor_elegido.nombre_apellido}\n\n')
        for materia in materias_de_profesor:
          c1 += 1
          print(f'{c1}. {materia.nombre}')

        opcion_elegida2 = validador(c1)
        materia_elegida = materias_de_profesor[opcion_elegida2 - 1]

        print(f'¿Seguro que quiere desasignar al profesor {profesor_elegido.nombre_apellido} de la materia {materia_elegida.nombre}?\n\n1. Sí\n2. No (Volver)\n')
        opcion_elegida3 = validador(2)
        if opcion_elegida3 == 1:
          materia_elegida.profesores.remove(profesor_elegido)
          for comi in materia_elegida.comisiones:
            if comi.profesor.legajo == legajo_profesor:
              comi.profesor = None
        
        
        print(f'La materia {materia_elegida.nombre} tiene {len(materia_elegida.profesores)} profesores')
  

    elif opcion_elegida1 == 2:
      if len(materias_de_profesor) != 0:

        print(f'¿De qué materia es la comisión de la cual quiere desasignar al profesor {profesor_elegido.nombre_apellido}?\n\n')
        for materia in materias_de_profesor:
          c1 += 1
          print(f'{c1}. {materia.nombre}')

        opcion_elegida4 = validador(c1)
        materia_elegida = materias_de_profesor[opcion_elegida4 - 1]
        print(f'Escoja la comisión para desasignar\n\n')
        for comi in materia_elegida.comisiones:
          if comi.profesor != None and comi.profesor == profesor_elegido:
            c2 += 1
            print(f'{c2}. {comi.codigo_comision}')
          
        opcion_elegida5 = validador(c2)
        comision_elegida = materia_elegida.comisiones[opcion_elegida5 - 1]

        print(f'¿Seguro que quiere desasignar al profesor {profesor_elegido.nombre_apellido} de la comision {comision_elegida.codigo_comision} de la materia {materia_elegida.nombre}?\n\n1. Sí\n2. No (Volver)\n')
        opcion_elegida6 = validador(2)
        if opcion_elegida6 == 1:
          comision_elegida.profesor = None
          chequeo_profe_en_materia = 0
          for comi in materia_elegida.comisiones:
            if comi.profesor == profesor_elegido:
              chequeo_profe_en_materia += 1
          if chequeo_profe_en_materia == 0:
            materia_elegida.profesores.remove(profesor_elegido)
        
        
        print(f'La materia {materia_elegida.nombre} tiene {len(materia_elegida.profesores)} profesores')
      
      else:
        print("El profesor no tiene comisiones a cargo.")

#Este metodo permite dar de alta una nueva carrera
  def altaCarrera(self, institucion:RegistroITBA):
    nombre = input("Ingrese el nombre de la carrera:")
    director = input("Ingrese el nombre del director de la carrera:")
    creditos = int(input("Ingrese cuantos creditos son necesarios para recibirse: "))
    nuevaCarrera = Carrera(nombre, director, creditos)
    institucion.agregar_carrera(nuevaCarrera)
    print(f"La nueva carrera {nombre} ha sido creada exitosamente.")


  def __str__(self):
      return "{} es administrativo y tiene el legajo {}".format(self.nombre_apellido,self.legajo)

#Este metodo permite actualizar las contrasenas de todos los usuarios
  def actualizarContraseña(self, institucion:RegistroITBA):
    inicio = True
    opcion_elegida = 0
    while inicio:
      print("¿A que tipo de usuario desea modificarle la contraseña?\n")
      print("1. Administrativo\n2. Alumno\n3. Profesor\n4. Volver")

      opcion_elegida = validador(4)
      clear()

      if opcion_elegida == 1:
        contraseña_nueva = input("Ingrese su contraseña nueva: ")
        self.contraseña = contraseña_nueva
        print("Su contraseña ha sido modificada exitosamente")
        inicio = False
      elif opcion_elegida == 2:
        legajo_ingresado = validadorLegajoAlumnos(institucion)
        for alumno in institucion.alumnos:
          if alumno.legajo == legajo_ingresado:
            contraseña_nueva = input("Ingrese la contraseña nueva: ")
            alumno.contraseña = contraseña_nueva
            print(f"La contraseña del alumno {alumno.nombre_apellido} ha sido modificada exitosamente")
            inicio = False
      elif opcion_elegida == 3:
        legajo_ingresado = validadorLegajoAdminyProf(institucion, "profesor")
        for profesor in institucion.profesores:
          if profesor.legajo == legajo_ingresado:
            contraseña_nueva = input("Ingrese la contraseña nueva: ")
            profesor.contraseña = contraseña_nueva
            print(f"La contraseña del profesor {profesor.nombre_apellido} ha sido modificada exitosamente")
            inicio = False
      else:
        inicio = False

    #Este metodo permite que el administrativo pueda resolver los tramites que tiene pendiente de los alumnos o profesores
  def resolverTramite(self, tramite): #menu para resolver trámite
    if tramite.alumno != None:
      print(f'\n¿Quiere resolver el tramite "{tramite.tipo_de_tramite}" del alumno {tramite.alumno.nombre_apellido}?\n')
      print("1. Resolver tramite\n2. Volver")
      rta = validador(2)
      if rta == 1:
            if getbyId(tramite.id) is not None:
            #Si esta, tengo que eliminarlo de las listas que estan en Institución y la propia lista del administrativo
              ITBA.tramites_abiertos.remove(getbyId(tramite.id))
              self.tramites_abiertos_admin.remove(tramite)
          #Una vez que lo saco de las listas, tengo que cambiar el estado del tramite a "Resuelto"
              tramite.estado = "Resuelto"
            #Una vez que le cambio el estado, tengo que poner el tramite en la lista de tramites resueltos de la Institución y el administrativo
              ITBA.tramites_resueltos.append(tramite)
              self.tramites_resueltos_admin.append(tramite)
              if tramite.alumno != None:
                tramite.alumno.tramites_abiertos_alu.remove(tramite)
                tramite.alumno.tramites_resueltos_alu.append(tramite)
              elif tramite.profesor != None:
                tramite.profesor.tramites_abiertos_profe.remove(tramite)
                tramite.profesor.tramites_resueltos_profe.append(tramite)

            return print("El tramite {} ha sido resuelto".format(tramite.tipo_de_tramite))
            
      clear()
    else:
      print(f"\n¿Quiere resolver el tramite {tramite.tipo_de_tramite} del profesor {tramite.profesor.nombre_apellido}?\n")
      print("1. Resolver tramite\n2. Volver")
      rta = validador(2)
      if rta == 1:
          if tramite.id == tramite.id:
            if getbyId(tramite.id) is not None:
            #Si esta, tengo que eliminarlo de las listas que estan en Institución y la propia lista del administrativo
              ITBA.tramites_abiertos.remove(getbyId(tramite.id))
              self.tramites_abiertos_admin.remove(tramite)
          #Una vez que lo saco de las listas, tengo que cambiar el estado del tramite a "Resuelto"
              tramite.estado = "Resuelto"
            #Una vez que le cambio el estado, tengo que poner el tramite en la lista de tramites resueltos de la Institución y el administrativo
              ITBA.tramites_resueltos.append(tramite)
              self.tramites_resueltos_admin.append(tramite)
              if tramite.alumno != None:
                tramite.alumno.tramites_abiertos_alu.remove(tramite)
                tramite.alumno.tramites_resueltos_alu.append(tramite)
              elif tramite.profesor != None:
                tramite.profesor.tramites_abiertos_profe.remove(tramite)
                tramite.profesor.tramites_resueltos_profe.append(tramite)

            return print(f"\nEl tramite {tramite.tipo_de_tramite} ha sido resuelto\n")
            
      clear()   
    #Este metodo permite mostrar los tramites que tiene disponibles el administrativo para resolver
  def displayTramiteActivo(self):
    resolviendo_tramites = True
    while resolviendo_tramites:
      cont_opciones = 1
      print("\nTrámites disponibles para resolver\n")
      for tramite in self.tramites_abiertos_admin: #por cada tramite activo que tiene el administrativo
            print(f'{cont_opciones}. {tramite.tipo_de_tramite}') # lo muestra como opcion
            cont_opciones += 1
      
      if len(self.tramites_abiertos_admin) == 0:
        print("No tiene trámites disponibles para resolver. Revise mas tarde\n")
      
      print(f'{cont_opciones}. Volver')
      opcion_elegida = validador(cont_opciones)
      
      if opcion_elegida == cont_opciones:
        resolviendo_tramites = False
      else:
        self.resolverTramite(self.tramites_abiertos_admin[opcion_elegida-1])

#Este metodo permite dar de alta un alumno nuevo
  def altaAlumno(self):
    nombre = input("Ingrese el nombre del alumno: ")
    dni = validadorDNI()
    sexo = validadorSexo()
    fecha_nacimiento = validadorFecha()
    contraseña = str(dni)
    if len(ITBA.legajos_alumnos) != 0:
      legajo = ITBA.legajos_alumnos[-1] + 1
    else:
      legajo = 10000
    fecha_ingreso = datetime.strptime(datetime.today().strftime('%d/%m/%Y'), '%d/%m/%Y')
    contador = 0
    flag = True
    alumno_nuevo = Alumno(nombre, dni, sexo, contraseña, fecha_nacimiento, legajo, fecha_ingreso)
    clear()
    #Para que el administrativo anote al alumno en un objeto carrera
    print(f'\n\t\t Seleccione la carrera del alumno\n')
    while flag:
      for carrera in ITBA.carreras:
        contador += 1
        print(f"{contador}. {carrera.nombre}")

      print(f"{contador + 1}. Cancelar")

      opcion_elegida = validador(contador + 1)
      if opcion_elegida == contador + 1:
          flag = False
      else:
        alumno_nuevo.carrera = ITBA.carreras[opcion_elegida-1]
        clear()
        flag = False
        print("Se ha anotado al alumno a la carrera: ", alumno_nuevo.carrera.nombre)
        print(f"El legajo del alumno es: {alumno_nuevo.legajo} y su contraseña es su dni: {contraseña}")
        ITBA.agregar_alumno(alumno_nuevo)
        alumno_nuevo.carrera.alumnos_actuales.append(alumno_nuevo)

#Este metodo permite dar de alta un profesor nuevo
  def altaProfesor(self):
    nombre = input("Ingrese el nombre del profesor: ")
    dni = validadorDNI()
    sexo = validadorSexo()
    fecha_nacimiento= validadorFecha()
    contraseña = str(dni)
    if len(ITBA.legajos_profesores) != 0:
      legajo_numero = int(ITBA.legajos_profesores[-1][2:]) + 1
      legajo_alfa = "PR"
      legajo = legajo_alfa + str(legajo_numero)
    else:
      legajo="PR10000"
    fecha_ingreso = datetime.strptime(datetime.today().strftime('%d/%m/%Y'), '%d/%m/%Y')

    profesor_nuevo = Profesor(nombre, dni, sexo, contraseña, fecha_nacimiento, legajo, fecha_ingreso)
    ITBA.agregar_profesor(profesor_nuevo)
    print(f"El legajo del profesor es: {profesor_nuevo.legajo} y su contraseña es su dni: {contraseña}")

#Este metodo permite dar de baja un alumno
  def bajaAlumno(self):
    legajo_alumno = validadorLegajoAlumnos(ITBA)
    for alumno in ITBA.alumnos:
      if alumno.legajo == legajo_alumno:
        ITBA.alumnos.remove(alumno)
        alumno.carrera.alumnos_actuales.remove(alumno)
        alumno.fecha_baja = datetime.strptime(datetime.today().strftime('%d/%m/%Y'), '%d/%m/%Y')

#Este metodo permite dar de baja un profesor
  def bajaProfesor(self):
    flag = False
    legajo_profesor = validadorLegajoAdminyProf(ITBA,"profesor")
    clear()
    for profesor in ITBA.profesores:
      if profesor.legajo == legajo_profesor:
        profesor_elegido = profesor
        profesor_elegido.fecha_baja = datetime.strptime(datetime.today().strftime('%d/%m/%Y'), '%d/%m/%Y')
    for carrera in ITBA.carreras:
      for materia in carrera.materias:
        if len(materia.comisiones) != 0:
          for comision in materia.comisiones:
            if legajo_profesor == comision.profesor.legajo:
              flag = True
              comision.profesor = None
              print(f"Se ha dado de baja al profesor {profesor_elegido.nombre_apellido} de la Comision {comision.codigo_comision} de la Materia {materia.nombre}")
        
        if flag:
          materia.profesores.remove(profesor_elegido)
          flag = False
      
    ITBA.profesores.remove(profesor_elegido)

#Este metodo permite dar de baja un administrativo
  def bajaAdministrativo(self):
    almacen_tramites=[]
    legajo_admin = validadorLegajoAdminyProf(ITBA)
    if legajo_admin == self.legajo:
      print("Usted no se puede dar de baja a si mismo")
    else:
      for administrativo in ITBA.administrativos:
        if legajo_admin == administrativo.legajo:
          if len(administrativo.tramites_abiertos_admin) != 0:
            if len(ITBA.administrativos)-1 == 0:
              print(f"Usted no puede dar de baja al Administrativo {administrativo.nombre_apellido} ya que no hay otro Administrativo que pueda hacer sus tramites pendientes")
            else:
              for tramite in administrativo.tramites_abiertos_admin:
                almacen_tramites.append(tramite)
              ITBA.administrativos.remove(administrativo)
              cantidad_administrativos = len(ITBA.administrativos)
              i_random = random.randint(0, cantidad_administrativos - 1)
              administrativo_asignado=ITBA.administrativos[i_random]
              for tramite in almacen_tramites:
                tramite.administrativo=administrativo_asignado
                administrativo_asignado.tramites_abiertos_admin.append(tramite)
              print(f"El Administrativo ha sido de baja correctamente, sus tramites fueron asignados al Administrativo {administrativo_asignado.nombre_apellido}")
          else:
            ITBA.administrativos.remove(administrativo)
            print("El Administrativo ha sido dado de baja correctamente")

#Este metodo permite crear una nueva materia
  def crearMateria(self):
    contador = 0
    carreras_total = []
    flag = True
    print("Carreras de la institución\n")
    while flag:
      for carrera in ITBA.carreras:
        contador += 1
        carreras_total.append(carrera)
        print(f'{contador}. {carrera.nombre}')
      print(f'{contador + 1}. Volver')
    
      opcion_elegida = validador(contador + 1)
      if opcion_elegida == contador + 1:
          flag = False
      else:
        carrera_elegida = carreras_total[opcion_elegida - 1]
        clear()
        flag = False

        print(f'Creación de la materia para la carrera {carrera.nombre}\n')
        codigo_materia = validadorCodigoMateria()
        nombre = input("Ingrese el nombre de la materia: ")
        creditos = validadorCreditos()
        sede = validadorSede()
        correlativas = validadorCorrelativas()

        nueva_materia = Materia(codigo_materia, nombre, creditos, sede, correlativas)

        carrera_elegida.materias.append(nueva_materia)
        print(f"\nLa materia {nueva_materia.nombre} de la carrera {carrera_elegida.nombre} fue creada correctamente. ")


#Este metodo permite dar de baja una materia
  def bajaMateria(self): 
    codigo_elegido = validadorCodigoMateria()

    for materia in ITBA.materias:
      if codigo_elegido == materia.codigo_materia:
        materia_elegida = materia
    
    if len(materia_elegida.profesores) != 0:
      for comision in materia_elegida.comisiones:
        comision.profesor.comisiones_a_cargo.remove(comision)
        comision.profesor = None
      materia_elegida.profesores.clear()
    
    if len(materia_elegida.alumnos) != 0:
      for comision in materia_elegida.comsiones:
        for alumno in comision.alumnos:
          alumno.comisiones_en_curso.remove(comision)
          alumno.materias_en_curso.remove(materia_elegida)
      
      comision.alumnos.clear()
      materia_elegida.alumnos.clear()
    
    if len(materia_elegida.comisiones) != 0:
      materia_elegida.comisiones.clear()

    for carrera in ITBA.carreras:
      if materia_elegida in carrera.materias:
        carrera.materias.remove(materia_elegida)
    
    print(f"La materia {materia_elegida.nombre} se ha dado de baja con exito.")

#Este metodo permite dar de alta una comision
  def crearComision(self):
    contador = 0
    materias_total = []
    flag = True
    print("Materias de la institución\n")
    while flag:
      for carrera in ITBA.carreras:
        for materia in carrera.materias:
          contador += 1
          materias_total.append(materia)
          print(f"{contador}. {materia.codigo_materia} {materia.nombre}")
      
      print(f"{contador + 1}. Volver")

      opcion_elegida = validador(contador + 1)
      if opcion_elegida == contador + 1:
          flag = False
      else:
        materia_elegida = materias_total[opcion_elegida - 1]
        clear()
        flag = False
        cod_comi = "A"
        if len(materia_elegida.comisiones) != 0:
          cod_comi = ascii_uppercase[len(materia_elegida.comisiones)]

        print(f"Creación de la comision para {materia_elegida.nombre}\n")
        aula = validadorAula()
        legajo_profesor_asignado = validadorLegajoAdminyProf(ITBA,"profesor")

        for profesor in ITBA.profesores:
          if profesor.legajo == legajo_profesor_asignado:
            profesor_asignado = profesor

        dia = validadorDia().upper().replace(" ","").split(",")
        horario = validadorHorario(dia)
        dia_horario = {"Dia":dia,"Horario":horario}
        clear()
        
        nueva_comision = Comision(cod_comi, aula, profesor_asignado,materia_elegida.nombre, dia_horario)

        materia_elegida.comisiones.append(nueva_comision)
        materia_elegida.profesores.append(profesor_asignado)
        profesor_asignado.comisiones_a_cargo.append(nueva_comision)

        print(f"La comision {nueva_comision.codigo_comision} de {materia_elegida.nombre} fue creada correctamente ")
 

 #Este metodo permite dar de baja una comision
  def bajaComision(self):
    comisiones=[]
    materias=[]
    #Crear validadores de codigo de comision y materias, para validar que existan
    cod_materia=validadorCodigoMateriaExistente()
    cod_comi=validadorCodigoComisionExistente(cod_materia)
    for carrera in ITBA.carreras:
      for materia in carrera.materias:
        materias.append(materia)
        for comision in materia.comisiones:
          comisiones.append(comision)
    for materia in materias:
      if cod_materia == materia.codigo_materia:
        for comision in materia.comisiones:
          if cod_comi==comision.codigo_comision:
            comision_seleccionada=comision
            materia.comisiones.remove(comision)
            comision.profesor.comisiones_a_cargo.remove(comision)
            for alumno in comision.alumnos:
              alumno.comisiones_en_curso.remove(comision)
            print(f"La comision {comision_seleccionada.codigo_comision} de la materia {comision_seleccionada.materia} ha sido eliminada")


  def estadisticasGenerales(self):
    armado_menu("ESTADISTICAS GENERALES", ['Alumnos actuales por carrera','Rendimiento Alumno', "Volver"], [lambda : self.alumnosActualesxCarrera(), lambda : self.histogramaNotasFinalesAlumno()])
  
  #Metodo que le permite ver los alumnos actuales por carrera al admin
  def alumnosActualesxCarrera(self):
   alumnos=[]
   carreras=[]
   for carrera in ITBA.carreras:
     c = 0
     carreras.append(carrera.nombre)
     for alumno in carrera.alumnos_actuales:
       c += 1
     alumnos.append(c)
   plt.pie(alumnos, labels=carreras, autopct='%1.1f%%')
   plt.title(label = "Alumnos por Carrera")
   plt.show()

  #Metodo que le permite ver un histrograma de las notas finales de los alumnos
  def histogramaNotasFinalesAlumno(self):
    legajo_alumno=validadorLegajoAlumnos(ITBA)
    for alumno in ITBA.alumnos:
      if alumno.legajo==legajo_alumno:
        alumno_elegido=alumno

    notas=alumno_elegido.historial_academico.values()
    lista_notas=[]
    notas_posibles=[1,2,3,4,5,6,7,8,9,10]
    lista_frecuencias=[]
    for nota in notas:
      lista_notas.append(nota)
    c=0
    for nota in notas_posibles:
      for elemento in lista_notas:
        if nota==elemento:
          c+=1
      lista_frecuencias.append(c)
      c=0
    plt.title(f"Rendimiento del alumno {alumno_elegido.nombre_apellido}")
    plt.bar(notas_posibles,lista_frecuencias)
    plt.xticks(notas_posibles)
    plt.ylabel("Frecuencia")
    plt.show()
  
