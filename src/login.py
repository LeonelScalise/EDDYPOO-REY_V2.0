from math import inf
from PyQt5.QtWidgets import QMainWindow, QListWidgetItem, QColorDialog, QFileDialog, QStyle, QListWidget, QVBoxLayout, QWidget, QVBoxLayout, QApplication
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
        # self.systemadmin_window.cb_alta_mat_carrera
        esValidoLogin = self.btn_login.clicked.connect(self.validLogin)
        if esValidoLogin:
            self.cargarDatosCombobox('cb_alta_mat_carrera', 'systemadmin_window', ITBA, 'carreras')
            self.cargarDatosCombobox('cb_alta_comi_carrera', 'systemadmin_window', ITBA, 'carreras')
            self.cargarDatosCombobox('cb_alta_mat_carrera', 'systemadmin_window', ITBA, 'carreras', 'materias', 'cb_alta_mat_corre')
            self.cargarDatosCombobox('cb_alta_comi_carrera', 'systemadmin_window', ITBA, 'carreras', 'materias', 'cb_alta_comi_materia')
            self.systemalu_window.ultimoTramiteAlumno()
            self.systemprofe_window.ultimoTramiteProfesor()

        self.systemadmin_window.cb_alta_mat_carrera.currentIndexChanged.connect(lambda: self.cargarDatosCombobox('cb_alta_mat_carrera', 'systemadmin_window', ITBA, 'carreras', 'materias', 'cb_alta_mat_corre'))
        self.systemadmin_window.cb_alta_comi_carrera.currentIndexChanged.connect(lambda: self.cargarDatosCombobox('cb_alta_comi_carrera', 'systemadmin_window', ITBA, 'carreras', 'materias', 'cb_alta_comi_materia'))
        self.systemadmin_window.btn_add_alta_mat_corre.clicked.connect(lambda: self.agregarTextoListView('listWidget_alta_mat', 'cb_alta_mat_corre', 'systemadmin_window'))
        self.systemadmin_window.btn_borrar_item_alta_mat.clicked.connect(lambda: self.borrarItemListWidget('listWidget_alta_mat', 'systemadmin_window'))
        self.systemadmin_window.btn_registro_alta_mat.clicked.connect(lambda: self.registrarAltaMat(ITBA))
        self.systemadmin_window.btn_logout_admin.clicked.connect(self.logout)
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

    def cargarDatosCombobox(self, nombre_combobox_padre, nombre_ventana, institucion, attr_q_buscar1, attr_q_buscar2=None, nombre_combobox_hija=None):
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
                    self.hide()
                    self.systemadmin_window.label_info_usuario_log.setText(f"Logeado como {admin_elegido.nombre_apellido} - {admin_elegido.legajo}")
                    self.systemadmin_window.show()
                    return True
                else:
                    self.setTextColor("label_error","Los datos son incorrectos. Intente nuevamente.", "red")
                    self.label_error.setText()    
            
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
                    self.hide()
                    self.systemprofe_window.label_info_usuario_log.setText(f"Logeado como {profesor_elegido.nombre_apellido} - {profesor_elegido.legajo}")
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


