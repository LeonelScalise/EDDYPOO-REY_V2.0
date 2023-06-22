from PyQt5.QtWidgets import QMainWindow, QListWidgetItem, QColorDialog, QFileDialog, QStyle
from PyQt5.QtCore import Qt, QCoreApplication, QDate


# Project modules
from src.ui.systemadmin import Ui_Systemadmin
from ProyectoV2.popularInstitucion import ITBA
from ProyectoV2.popularPersona import *
from datetime import *

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
        self.btn_asig_mat_profe.clicked.connect(self.showWindowAsignarProfe)
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

        #Boton para alta
        self.btn_registro_alta_admin.clicked.connect(lambda: self.clickRegistrarAdmin(ITBA, 'input_alta_admin_nombre', 'input_alta_admin_dni', 'dt_alta_admin_fnac','cb_alta_admin_sexo'))
        self.btn_registro_alta_alu.clicked.connect(lambda: self.clickRegistrarAlu(ITBA, 'input_alta_alu_nombre', 'input_alta_alu_dni', 'dt_fnac_alta_alu','cb_sexo_alta_alu'))
        self.btn_registro_alta_profe.clicked.connect(lambda: self.clickRegistrarProfe(ITBA, 'input_alta_profe_nombre', 'input_alta_profe_dni', 'dt_fnac_alta_profe','cb_sexo_alta_profe'))



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

    def agarraTextoInput(self, nombre_input): #agarra lo que esta en el input de texto
        input_texto = getattr(self, nombre_input)
        texto = input_texto.text().upper()
        return texto
    
    def agarraComboBoxValue(self, nombre_combobox): #agarra el valor seleccionado del combobox
        combobox = getattr(self, nombre_combobox)
        valor = combobox.currentText().upper()
        return valor

    def agarraFechaInput(self, nombre_input_fecha): #agarra la fecha seleccionada en el datetime
        fecha_gui = getattr(self, nombre_input_fecha)
        fecha = fecha_gui.date()
        return fecha
    
    
    def clickRegistrarAdmin(self, institucion, nombre_input_nombre, nombre_input_dni, nombre_input_fecha, nombre_input_sexo):
        nombre_apellido = self.agarraTextoInput(nombre_input_nombre)
        dni = self.agarraTextoInput(nombre_input_dni)
        dni_valido = self.validadorDNI(dni, ITBA, 'administrativos', 'label_informe_alta_admin')
        if not dni_valido:
            return
        fecha_nac = self.agarraFechaInput(nombre_input_fecha)
        sexo = self.agarraComboBoxValue(nombre_input_sexo)
        contraseña = str(dni)
        if len(institucion.legajos_administrativos) != 0:
          legajo_numero = int(institucion.legajos_administrativos[-1][2:])+1
          legajo_alfa = "AD"
          legajo = legajo_alfa + str(legajo_numero)
        else:
          legajo="AD10000"
        fecha_ingreso = datetime.strptime(datetime.today().strftime('%d/%m/%Y'), '%d/%m/%Y')
        institucion.administrativos.append(Administrativo(nombre_apellido, dni, sexo, contraseña, fecha_nac, legajo, fecha_ingreso))        
        institucion.legajos_administrativos.append(legajo)
        self.label_informe_alta_admin.setText(f'Se ha creado el administrativo {nombre_apellido} de dni {dni} correctamente. Hay {len(institucion.administrativos)} administrativos')
        self.input_alta_admin_nombre.setText("")
        self.input_alta_admin_dni.setText("")
        self.dt_alta_admin_fnac.setDate(QDate(2000, 1, 1))
        self.cb_alta_admin_sexo.setCurrentIndex(0)
    

    def clickRegistrarAlu(self, institucion, nombre_input_nombre, nombre_input_dni, nombre_input_fecha, nombre_input_sexo):
        nombre_apellido = self.agarraTextoInput(nombre_input_nombre)
        dni = self.agarraTextoInput(nombre_input_dni)
        dni_valido = self.validadorDNI(dni, ITBA, 'alumnos', 'label_informe_alta_alu')
        if not dni_valido:
            return
        fecha_nac = self.agarraFechaInput(nombre_input_fecha)
        sexo = self.agarraComboBoxValue(nombre_input_sexo)
        contraseña = str(dni)
        if len(ITBA.legajos_alumnos) != 0:
            legajo = ITBA.legajos_alumnos[-1] + 1
        else:
            legajo = 10000
        fecha_ingreso = datetime.strptime(datetime.today().strftime('%d/%m/%Y'), '%d/%m/%Y')
        institucion.alumnos.append(Alumno(nombre_apellido, dni, sexo, contraseña, fecha_nac, legajo, fecha_ingreso))        
        institucion.legajos_alumnos.append(legajo)
        self.label_informe_alta_alu.setText(f'Se ha creado el alumno {nombre_apellido} de dni {dni} correctamente. Hay {len(institucion.alumnos)} alumnos')
        self.input_alta_alu_nombre.setText("")
        self.input_alta_alu_dni.setText("")
        self.dt_fnac_alta_alu.setDate(QDate(2000, 1, 1))
        self.cb_sexo_alta_alu.setCurrentIndex(0)


    def clickRegistrarProfe(self, institucion, nombre_input_nombre, nombre_input_dni, nombre_input_fecha, nombre_input_sexo):
        nombre_apellido = self.agarraTextoInput(nombre_input_nombre)
        dni = self.agarraTextoInput(nombre_input_dni)
        dni_valido = self.validadorDNI(dni, ITBA, 'profesores', 'label_informe_alta_profe')
        if not dni_valido:
            return
        fecha_nac = self.agarraFechaInput(nombre_input_fecha)
        sexo = self.agarraComboBoxValue(nombre_input_sexo)
        contraseña = str(dni)
        if len(ITBA.legajos_profesores) != 0:
            legajo_numero = int(ITBA.legajos_profesores[-1][2:]) + 1
            legajo_alfa = "PR"
            legajo = legajo_alfa + str(legajo_numero)
        else:
            legajo="PR10000"
        fecha_ingreso = datetime.strptime(datetime.today().strftime('%d/%m/%Y'), '%d/%m/%Y')
        institucion.profesores.append(Profesor(nombre_apellido, dni, sexo, contraseña, fecha_nac, legajo, fecha_ingreso))        
        institucion.legajos_profesores.append(legajo)
        self.label_informe_alta_profe.setText(f'Se ha creado el profesor {nombre_apellido} de dni {dni} correctamente. Hay {len(institucion.profesores)} profesores')
        self.input_alta_profe_nombre.setText("")
        self.input_alta_profe_dni.setText("")
        self.dt_fnac_alta_profe.setDate(QDate(2000, 1, 1))
        self.cb_sexo_alta_profe.setCurrentIndex(0)
    
    
    def validadorDNI(self, dni_a,institucion, atributo_ad_pr_al, label_informe):
        label_inf = getattr(self, label_informe)
        try:
            DNI_ingresado = int(dni_a)
        except ValueError:
            label_inf.setText("<span style='color=red;'>El dni ingresado debe ser un numero.</span>")
            return False  # volve antes porque el codigo que sigue depende de la conversion
        if len(str(DNI_ingresado)) != 8:
            label_inf.setText('<span style="color=red;">El DNI debe tener 8 digitos.</span>')
            return False
        for persona in getattr(institucion, atributo_ad_pr_al):
            if int(persona.dni) == DNI_ingresado:
                label_inf.setText("<span style='color=red;'>El DNI ya existe, inténtalo nuevamente.</span>")
                return False
        
        return True
    