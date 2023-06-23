from math import inf
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QListWidgetItem, QColorDialog, QFileDialog, QStyle, QListWidget, QVBoxLayout, QWidget, QVBoxLayout, QApplication
from PyQt5.QtCore import Qt, QCoreApplication, QAbstractItemModel, QStringListModel


# Project modules
from src.ui.login import Ui_Login
from src.systemadmin import SystemadminWindow
from src.systemalu import SystemaluWindow
from src.systemprofe import SystemprofeWindow
from ProyectoV2.popularInstitucion import ITBA
from ProyectoV2.popularPersona import *

class LoginWindow(QMainWindow, Ui_Login):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)
        self.systemadmin_window = SystemadminWindow()
        self.systemalu_window = SystemaluWindow()
        self.systemprofe_window = SystemprofeWindow()

        self.btn_login.clicked.connect(self.validLogin)
        
        

        self.systemalu_window.cb_inscrip_mat.currentIndexChanged.connect(lambda : self.comboboxInscripcionMateriaAlumno(2))
        self.systemalu_window.cb_inscrip_mat_comi.currentIndexChanged.connect(lambda : self.cambioHorarios())
        self.systemalu_window.btn_inscr_mat.clicked.connect(lambda : self.inscribirMateria())
        self.systemadmin_window.cb_alta_mat_carrera.currentIndexChanged.connect(lambda: self.cargarDatosComboboxGeneral('cb_alta_mat_carrera', 'systemadmin_window', ITBA, 'carreras', 'materias', 'cb_alta_mat_corre'))
        self.systemadmin_window.cb_alta_comi_carrera.currentIndexChanged.connect(lambda: self.cargarDatosComboboxGeneral('cb_alta_comi_carrera', 'systemadmin_window', ITBA, 'carreras', 'materias', 'cb_alta_comi_materia'))
        self.systemprofe_window.cb_subir_nota_mat_disponible.currentIndexChanged.connect(lambda: self.comboboxSubirNotaFinal(2))
        self.systemprofe_window.cb_subir_nota_com_a_cargo.currentIndexChanged.connect(lambda: self.cambiarAlumnos())
        self.systemprofe_window.btn_subir_nota.clicked.connect(lambda: self.registroNotaFinal())
        self.systemadmin_window.btn_add_alta_mat_corre.clicked.connect(lambda: self.agregarTextoListView('listWidget_alta_mat', 'cb_alta_mat_corre', 'systemadmin_window'))
        self.systemadmin_window.btn_borrar_item_alta_mat.clicked.connect(lambda: self.borrarItemListWidget('listWidget_alta_mat', 'systemadmin_window'))
        self.systemadmin_window.btn_registro_alta_mat.clicked.connect(lambda: self.registrarAltaMat(ITBA))
        self.systemadmin_window.btn_logout_admin.clicked.connect(self.logout)
        self.systemadmin_window.btn_registro_carrera.clicked.connect(lambda: self.registroAltaCarrera())
        self.systemadmin_window.btn_asig_prof_busc_comi.clicked.connect(lambda: self.buscarAsignarProf())
        self.systemalu_window.btn_logout_alu.clicked.connect(self.logout)
        self.systemprofe_window.btn_logout_profe.clicked.connect(self.logout)
    

    def registrarAltaMat(self, institucion):
        ventana = getattr(self, 'systemadmin_window')
        listWidget = getattr(ventana, 'listWidget_alta_mat')
        nombre_carrera = getattr(ventana, 'cb_alta_mat_carrera')
        codigo = getattr(ventana, 'input_alta_mat_cod')
        nombre_materia = getattr(ventana, 'input_alta_mat_nom')
        creditos = getattr(ventana, 'input_alta_mat_cred')
        sede = getattr(ventana, 'cb_alta_mat_sede')
        codigo_texto = codigo.text()
        nombre__materia_texto = nombre_materia.text()
        creditos_texto = int(creditos.text())
        sede_nombre = sede.currentText()
        nombre_carrera_texto = nombre_carrera.currentText()
        lista_correlativas = []
        for carrera in institucion.carreras:
            if carrera.nombre == nombre_carrera_texto:
                objeto_carrera = carrera
        contador_items = listWidget.count()
        if contador_items != 0:
            for i in range(contador_items):
                for materia in objeto_carrera.materias:
                    if materia.nombre == listWidget.item(i).text():
                        lista_correlativas.append(materia)
            materia_nueva = Materia(codigo_texto, nombre__materia_texto, creditos_texto, sede_nombre, lista_correlativas)
            print(f'Se creo la materia de codigo {codigo_texto}, nombre {nombre__materia_texto} con {creditos_texto} creditos en {sede_nombre} y correlativas {lista_correlativas}')
        
        else:
            materia_nueva = Materia(codigo_texto, nombre__materia_texto, creditos_texto, sede_nombre)
            print(f'Se creo la materia de codigo {codigo_texto}, nombre {nombre__materia_texto} con {creditos_texto} creditos en {sede_nombre}')
        objeto_carrera.materias.append(materia_nueva)
        print(len(objeto_carrera.materias))
        print('materia agregada :)')
        self.systemadmin_window.cb_alta_mat_carrera.setCurrentIndex(0)
        self.systemadmin_window.input_alta_mat_cod.setText("")
        self.systemadmin_window.input_alta_mat_nom.setText("")
        self.systemadmin_window.input_alta_mat_cred.setText("")
        self.systemadmin_window.cb_alta_mat_sede.setCurrentIndex(0)
        self.systemadmin_window.listWidget_alta_mat.clear()

    def agregarTextoListView(self, nombre_list_widget, nombre_Combobox, nombre_ventana):
        ventana = getattr(self, nombre_ventana)
        combobox = getattr(ventana, nombre_Combobox)
        listWidget = getattr(ventana, nombre_list_widget)
        valor_combobox = combobox.currentText()
        contador_items = listWidget.count()
        if contador_items != 0:
            for indice in range(contador_items):
                if listWidget.item(indice).text() == valor_combobox:
                    return
                
            listWidget.addItem(valor_combobox)
        else:
            listWidget.addItem(valor_combobox)


    def borrarItemListWidget(self, nombre_list_widget, nombre_ventana):
        ventana = getattr(self, nombre_ventana)
        listWidget = getattr(ventana, nombre_list_widget)
        listWidget.takeItem(listWidget.currentRow())

    def cargarDatosComboboxGeneral(self, nombre_combobox_padre, nombre_ventana, institucion, attr_q_buscar1, attr_q_buscar2=None, nombre_combobox_hija=None):
        lista_valores = []
        institucionPuntoAtributo1 = getattr(institucion, attr_q_buscar1)

        ventana = getattr(self, nombre_ventana)
        combobox_padre = getattr(ventana, nombre_combobox_padre)
        valor_combobox_padre = combobox_padre.currentText()  # Obtener el valor seleccionado del combobox padre

        for elemento1 in institucionPuntoAtributo1:
            if attr_q_buscar2 is not None and elemento1.nombre == valor_combobox_padre:
                institucionPuntoAtributo2 = getattr(elemento1, attr_q_buscar2)
                for elemento2 in institucionPuntoAtributo2:
                    lista_valores.append(elemento2)
            elif attr_q_buscar2 is None:
                lista_valores.append(elemento1)

        if nombre_combobox_hija is not None:
            combobox = getattr(ventana, nombre_combobox_hija)
        else:
            combobox= getattr(ventana, nombre_combobox_padre)

        combobox.clear()

        for valor in lista_valores:
            combobox.addItem(valor.nombre)


    def comboboxInscripcionMateriaAlumno(self, nivel=1):
        ventana = getattr(self, 'systemalu_window')
        combobox_padre = getattr(ventana, 'cb_inscrip_mat')
        combobox_hijo = getattr(ventana, 'cb_inscrip_mat_comi')
        lista_valores = []
        if len(self.systemalu_window.label_info_usuario_log.text()) != 0:
            alumno = self.systemalu_window.obtenerAlumno()
        else:
            return #no encontró alumno, abort abort
        
        materia_selec = None  # Inicializar la variable materia_selec
        combobox_texto = None

        if nivel == 1:
            for materia in alumno.carrera.materias:
                lista_valores.append(materia.nombre)
            for valor in lista_valores:
                combobox_padre.addItem(valor)
        else:
            combobox_texto = combobox_padre.currentText()
            for materia in alumno.carrera.materias:
                if materia.nombre == combobox_texto:
                    for comision in materia.comisiones:
                        materia_selec = materia  # Asignar la materia seleccionada a materia_selec
                        lista_valores.append(comision.codigo_comision)

            combobox_hijo.clear()

            for valor in lista_valores:
                combobox_hijo.addItem(valor)


    def cambioHorarios(self):
        if len(self.systemalu_window.label_info_usuario_log.text()) != 0:
            alumno = self.systemalu_window.obtenerAlumno()

        ventana = getattr(self, 'systemalu_window')
        
        combobox_padre = getattr(ventana, 'cb_inscrip_mat')
        combobox_padre_texto = combobox_padre.currentText()
        
        combobox_hijo = getattr(ventana, 'cb_inscrip_mat_comi')
        combobox_hijo_texto = combobox_hijo.currentText()
        
        materia_selec = None
        dia_horario = None
        
        for materia in alumno.carrera.materias:
            if materia.nombre == combobox_padre_texto:
                materia_selec = materia
                break

        if materia_selec is not None:
            for comision in materia_selec.comisiones:
                if comision.codigo_comision == combobox_hijo_texto and comision.dia_y_horario is not None:
                    dia_horario = comision.dia_y_horario
                    break

        if dia_horario is not None:
            # Establecer el número de filas en la tabla
            self.systemalu_window.tW_inscr_mat.setRowCount(len(dia_horario["Dia"]))

            # Insertar los nuevos valores en la tabla
            for i, dia in enumerate(dia_horario["Dia"]):
                inicio = dia_horario["Horario"][i].split("-")[0]
                fin = dia_horario["Horario"][i].split("-")[1]
                self.systemalu_window.tW_inscr_mat.setItem(i, 0, QTableWidgetItem(dia))
                self.systemalu_window.tW_inscr_mat.setItem(i, 1, QTableWidgetItem(inicio))
                self.systemalu_window.tW_inscr_mat.setItem(i, 2, QTableWidgetItem(fin))
        else:
            # Si no hay horarios disponibles, vaciar la tabla
            self.systemalu_window.tW_inscr_mat.clearContents()
            self.systemalu_window.tW_inscr_mat.setRowCount(0)

    def inscribirMateria(self):
        if len(self.systemalu_window.label_info_usuario_log.text()) != 0:
            alumno = self.systemalu_window.obtenerAlumno()
        ventana = getattr(self, 'systemalu_window')
        combobox_materia = getattr(ventana, 'cb_inscrip_mat')
        combobox_comision = getattr(ventana, 'cb_inscrip_mat_comi')
        combobox_materia_texto = combobox_materia.currentText()
        combobox_comision_texto = combobox_comision.currentText()

        for carrera in ITBA.carreras:
            if carrera.nombre == alumno.carrera.nombre:
                carrera_alumno = carrera

        for materia in carrera_alumno.materias:
            if materia.nombre == combobox_materia_texto:
                materia_elegida = materia
        
        for comision in materia_elegida.comisiones:
            if comision.codigo_comision == combobox_comision_texto:
                comision_elegida = comision

        comision_elegida.alumnos.append(alumno)
        materia_elegida.alumnos.append(alumno)
        alumno.materias_en_curso.append(materia_elegida)
        alumno.comisiones_en_curso.append(comision_elegida)

        self.systemalu_window.setTextColor('label_informe_inscr_mat', f'Se ha inscripto a {materia_elegida.nombre} en la comision {comision_elegida.codigo_comision} existosamente.', 'green')
        self.systemalu_window.cb_inscrip_mat.setCurrentIndex(0)
        self.systemalu_window.cb_inscrip_mat_comi.setCurrentIndex(0)

    # Función para establecer el color del texto
    def setTextColor(self, nombre_label, text, color):

        label = getattr(self, nombre_label)
        label.setText(text)
        label.setStyleSheet("color: %s;" % color)
        return label
    
    # Funcion para resetar los labels de informe
    def resetLabelsInforme(self):
        self.systemadmin_window.label_informe_alta_admin.setText("")
        self.systemadmin_window.label_informe_alta_alu.setText("")
        self.systemadmin_window.label_informe_alta_profe.setText("")
        self.systemadmin_window.label_informe_alta_mat.setText("")
        self.systemadmin_window.label_informe_alta_comision.setText("")
        self.systemadmin_window.label_informe_alta_carrera.setText("")
        self.systemadmin_window.label_informe_baja_admin.setText("")
        self.systemadmin_window.label_informe_baja_alumno.setText("")
        self.systemadmin_window.label_informe_baja_profe.setText("")
        self.systemadmin_window.label_informe_baja_mat.setText("")
        self.systemadmin_window.label_informe_baja_comi.setText("")
        self.systemadmin_window.label_informe_desasig_profe_comi.setText("")
        self.systemadmin_window.label_informe_asig_profe.setText("")
        self.systemadmin_window.label_informe_desasig_profe_mat.setText("")
        self.systemadmin_window.label_informe_materia.setText("")
        self.systemadmin_window.label_informe_modif_aluxcarrera.setText("")
        self.systemadmin_window.label_informe_modif_nom_carr.setText("")
        self.systemadmin_window.label_informe_modif_nom_mat.setText("")
        self.systemadmin_window.label_informe_modif_pass.setText("")
        self.systemadmin_window.label_informe_tramite.setText("")
        self.systemprofe_window.label_informe_ini_tram_profe.setText("")
        self.systemprofe_window.label_informe_modif_pass_profe.setText("")
        self.systemprofe_window.label_informe_subir_nota.setText("")
        self.systemalu_window.label_informe_desinscr_mat.setText("")
        self.systemalu_window.label_informe_inscr_mat.setText("")
        self.systemalu_window.label_informe_ini_tram_alu.setText("")
        self.systemalu_window.label_informe_modif_pass_alu.setText("")        

    def validLegajoAlumno(self, institucion, legajo_ingresado):
        try:
            legajoingresado = int(legajo_ingresado)
        except ValueError:
            self.setTextColor("label_error","El legajo ingresado debe ser un numero.", "red")
            return False  # volve antes porque el codigo que sigue depende de la conversion

        if len(str(legajoingresado)) != 5:
            self.setTextColor("label_error","El legajo debe ser de 5 digitos.", "red")
            return False
        elif legajoingresado not in institucion.legajos_alumnos:
            self.setTextColor("label_error","El legajo no existe. Intente nuevamente.", "red")
            return False

        return True

    def validLegajoAdminyProf(self, institucion, legajo_ingresado, rol = 'administrativo'):
        try:
            legajoingresado = legajo_ingresado.upper().strip()
        except ValueError:
            self.setTextColor("label_error","El legajo ingresado debe ser un numero.", "red")
            return False  # volve antes porque el codigo que sigue depende de la conversion
        
        if len(legajoingresado) != 7:
            self.setTextColor("label_error","El legajo debe ser de 7 caracteres.", "red")
            return False
        if rol == 'profesor':
                if legajoingresado[:2] != "PR":
                    self.setTextColor("label_error","El legajo debe comenzar con las primeras dos letras de su rol.", "red")
                    return False
                if legajoingresado not in institucion.legajos_profesores:
                    self.setTextColor("label_error","El legajo no existe. Intente nuevamente.", "red")
                    return False
        else:
                if legajoingresado[:2] != "AD":
                    self.setTextColor("label_error","El legajo debe comenzar con las primeras dos letras de su rol.", "red")
                    return False
                if legajoingresado not in institucion.legajos_administrativos:
                    self.setTextColor("label_error","El legajo no existe. Intente nuevamente.", "red") #si no cumple con la condición que se indica levanta un error con un mensaje
                    return False
        return True


    def validLogin(self):
        try:
            ITBA.cargarDatos()
        except FileNotFoundError:
            pass

        legajo_ingresado = self.input_legajo.text().upper()
        contraseña_ingresada = self.input_pass.text()

        if len(legajo_ingresado) == 0 or len(contraseña_ingresada) == 0:
            self.setTextColor("label_error","Hay campos sin completar. Intente nuevamente.", "red")
        else:
            if self.label_tipo.text() == "ADMINISTRATIVO":
                legajo_es_valido = self.validLegajoAdminyProf(ITBA, legajo_ingresado)
                if not legajo_es_valido:
                    return  # si el legajo no es valido no ejecutes lo siguiente
                
                admin_elegido = None
                for admin in ITBA.administrativos:
                    if admin.legajo == legajo_ingresado:
                        admin_elegido = admin
                
                if admin_elegido and admin_elegido.contraseña == contraseña_ingresada:
                    self.systemadmin_window.label_info_usuario_log.setText(f"Logeado como {admin_elegido.nombre_apellido} - {admin_elegido.legajo}")
                    self.cargarDatosComboboxGeneral('cb_alta_mat_carrera', 'systemadmin_window', ITBA, 'carreras')
                    self.cargarDatosComboboxGeneral('cb_alta_comi_carrera', 'systemadmin_window', ITBA, 'carreras')
                    self.cargarDatosComboboxGeneral('cb_alta_mat_carrera', 'systemadmin_window', ITBA, 'carreras', 'materias', 'cb_alta_mat_corre')
                    self.cargarDatosComboboxGeneral('cb_alta_comi_carrera', 'systemadmin_window', ITBA, 'carreras', 'materias', 'cb_alta_comi_materia')
                    self.hide()
                    self.systemadmin_window.show()
                    return True
                else:
                    self.setTextColor("label_error","Los datos son incorrectos. Intente nuevamente.", "red")   
            
            elif self.label_tipo.text() == "ALUMNO":
                legajo_es_valido = self.validLegajoAlumno(ITBA, legajo_ingresado)
                if not legajo_es_valido:
                    return  # si el legajo no es valido no ejecutes lo siguiente

                alumno_elegido = None
                for alumno in ITBA.alumnos:
                    if alumno.legajo == int(legajo_ingresado):
                        alumno_elegido = alumno
                
                if alumno_elegido and alumno_elegido.contraseña == contraseña_ingresada:
                    self.hide()
                    self.systemalu_window.label_info_usuario_log.setText(f"Logeado como {alumno_elegido.nombre_apellido} - {alumno_elegido.legajo}")
                    self.systemalu_window.ultimoTramiteAlumno()
                    self.comboboxInscripcionMateriaAlumno()
                    self.systemalu_window.show()
                    return True
                else:
                    self.setTextColor("label_error","Los datos son incorrectos. Intente nuevamente.", "red")
            
            else:
                legajo_es_valido = self.validLegajoAdminyProf(ITBA, legajo_ingresado, 'profesor')
                if not legajo_es_valido:
                    return  # si el legajo no es valido no ejecutes lo siguiente
                profesor_elegido = None
                for profesor in ITBA.profesores:
                    if profesor.legajo == legajo_ingresado:
                        profesor_elegido = profesor
                
                if profesor_elegido and profesor_elegido.contraseña == contraseña_ingresada:
                    self.systemprofe_window.label_info_usuario_log.setText(f"Logeado como {profesor_elegido.nombre_apellido} - {profesor_elegido.legajo}")
                    self.systemprofe_window.ultimoTramiteProfesor()
                    self.comboboxSubirNotaFinal()
                    self.hide()
                    self.systemprofe_window.show()
                    return True
                else:
                    self.setTextColor("label_error","Los datos son incorrectos. Intente nuevamente.", "red")

    
    def logout(self):
        ITBA.guardarDatos()
        self.systemadmin_window.hide()
        self.systemalu_window.hide()
        self.systemprofe_window.hide()
        self.label_error.setText("")
        self.input_legajo.setText("")
        self.input_pass.setText("")
        self.resetLabelsInforme()
        self.show()


    def comboboxSubirNotaFinal(self, nivel = 1):
        ventana = getattr(self, 'systemprofe_window')
        combobox_abuelo = getattr(ventana, 'cb_subir_nota_mat_disponible')
        combobox_padre = getattr(ventana, 'cb_subir_nota_com_a_cargo')

        lista_materias = []
        lista_comisiones = []

        if len(self.systemprofe_window.label_info_usuario_log.text()) != 0:
            profesor = self.systemprofe_window.obtenerProfesor()
        
        for carrera in ITBA.carreras:
                for materia in carrera.materias:
                    for profe in materia.profesores:
                        if profe.legajo == profesor.legajo:
                            if materia not in lista_materias:
                                lista_materias.append(materia)

        if nivel == 1:
            for valor in lista_materias:
                combobox_abuelo.addItem(valor.nombre)

        elif nivel == 2:
            combobox_texto = combobox_abuelo.currentText()
            for materia in lista_materias:
                if materia.nombre == combobox_texto:
                    for comision in materia.comisiones:
                        lista_comisiones.append(comision)

            combobox_padre.clear()
            
            for valor in lista_comisiones:
                combobox_padre.addItem(valor.codigo_comision)
        

    def cambiarAlumnos(self):
        ventana = getattr(self, 'systemprofe_window')
        combobox_mat = getattr(ventana, 'cb_subir_nota_mat_disponible')
        combobox_mat_texto = combobox_mat.currentText()
        combobox_comi = getattr(ventana, 'cb_subir_nota_com_a_cargo')
        combobox_comi_texto = combobox_comi.currentText()
        combobox_alumnos = getattr(ventana, 'cb_subir_nota_alumnos')
        lista_alumnos = []
        for carrera in ITBA.carreras:
            for materia in carrera.materias:
                if materia.nombre == combobox_mat_texto:
                    objeto_materia = materia
        
        for comision in objeto_materia.comisiones:
            if comision.codigo_comision == combobox_comi_texto:
                for alumno in comision.alumnos:
                    lista_alumnos.append(alumno)
        
        combobox_alumnos.clear()

        for valor in lista_alumnos:
            combobox_alumnos.addItem(str(valor.legajo))


    def registroNotaFinal(self):
        ventana = getattr(self, 'systemprofe_window')
        
        combobox_materia = getattr(ventana, 'cb_subir_nota_mat_disponible')
        combobox_mat_texto = combobox_materia.currentText()
        
        combobox_comision = getattr(ventana, 'cb_subir_nota_com_a_cargo')
        combobox_comi_texto = combobox_comision.currentText()
        
        combobox_alumno = getattr(ventana, 'cb_subir_nota_alumnos')
        combobox_alumno_texto = combobox_alumno.currentText()
        
        input_nota_final = getattr(ventana, 'input_subir_nota')
        input_nota_final_texto = int(input_nota_final.text())

        for carrera in ITBA.carreras:
            for materia in carrera.materias:
                if materia.nombre == combobox_mat_texto:
                    materia_elegida = materia
        
        for comision in materia_elegida.comisiones:
            if combobox_comi_texto == comision.codigo_comision:
                comision_elegida = comision

        for alumno in ITBA.alumnos:
            if str(alumno.legajo) == combobox_alumno_texto:
                alumno_elegido = alumno



        if input_nota_final_texto >= 4:
              alumno_elegido.materias_aprobadas.append(materia_elegida)
              alumno_elegido.materias_en_curso.remove(materia_elegida)
              materia_elegida.alumnos.remove(alumno_elegido)
              alumno_elegido.comisiones_en_curso.remove(comision_elegida)
              comision_elegida.alumnos.remove(alumno_elegido)
              alumno_elegido.creditos_aprobados += materia_elegida.creditos
              print(f'el alumno {alumno_elegido.nombre_apellido} aprobo la materia {materia_elegida.nombre} en la comision {comision_elegida.codigo_comision} con una notasa mamasa de {str(input_nota_final_texto)}')
        
        alumno_elegido.historial_academico[materia_elegida.nombre] = input_nota_final_texto
        
        self.systemprofe_window.label_informe_subir_nota.setText("Ha subido la nota correctamente.")  #.setStyleSheet("color: %s;" % 'green')
        self.systemprofe_window.cb_subir_nota_mat_disponible.setCurrentIndex(0)
        self.systemprofe_window.cb_subir_nota_com_a_cargo.setCurrentIndex(0)
        self.systemprofe_window.cb_subir_nota_alumnos.setCurrentIndex(0)
        self.systemprofe_window.input_subir_nota.setText("")

    def registroAltaCarrera(self):
        ventana = getattr(self, "systemadmin_window")
        
        input_nombre_carrera = getattr(ventana, "input_alta_carrera_nom")
        input_nombre_carrera_text = input_nombre_carrera.text()
        
        input_alta_carrera_director = getattr(ventana, "input_alta_carrera_direc")
        input_alta_carrera_director_text = input_alta_carrera_director.text()

        input_alta_carrera_creditos = getattr(ventana, "input_alta_carrera_cred")
        input_alta_carrera_creditos_text = int(input_alta_carrera_creditos.text())

        carrera_creada = Carrera(input_nombre_carrera_text, input_alta_carrera_director_text, input_alta_carrera_creditos_text)
        ITBA.agregar_carrera(carrera_creada)
        self.systemadmin_window.label_informe_alta_carrera.setText("Se agregó la carrera de manera exitosa.")


    def buscarAsignarProf(self):
        ventana = getattr(self, "systemadmin_window")
        input_legajo_prof = getattr(ventana, "input_legajo_profe_asig")
        input_legajo_prof_text = input_legajo_prof.text().upper()
        input_cod_mat = getattr(ventana, "input_cod_mat_asig_profe")
        input_cod_mat_text = input_cod_mat.text()

        for profesor in ITBA.profesores:
            if profesor.legajo == input_legajo_prof_text:
                profesor_elegido = profesor
        
        self.systemadmin_window.label_asig_prof_prof_selec.setText(f"Seleccionó al profesor {profesor_elegido.nombre_apellido}")

        for carrera in ITBA.carreras:
            for materia in carrera.materias:
                if materia.codigo_materia == input_cod_mat_text:
                    materia_elegida = materia
        
        self.systemadmin_window.label_asig_prof__mat_selec.setText(f"Seleccionó a la materia {materia_elegida.nombre}")
        
        for comision in materia_elegida.comisiones:
            self.systemadmin_window.cb_comi_asig_profe.addItem(comision.codigo_comision)

        