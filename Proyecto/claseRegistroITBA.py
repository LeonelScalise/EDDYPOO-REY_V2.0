import pickle

class RegistroITBA():
    def __init__(self, nombre, rector) -> None:
        self.nombre = nombre
        self.sedes = []
        self.rector = rector
        self.carreras = []
        self.alumnos = []
        self.profesores = []
        self.administrativos = []
        self.historial_alumnos = []
        self.historial_profesores = []
        self.historial_administrativos = []
        self.legajos_alumnos = []
        self.legajos_profesores = []
        self.legajos_administrativos = []
        self.tramites_resueltos = []
        self.tramites_abiertos = []
        self.historial_tramites = []
    
        
    
    def agregar_alumno(self, alumno):
        
        self.alumnos.append(alumno)
        self.legajos_alumnos.append(alumno.legajo)
        self.historial_alumnos.append(alumno)
        alumno.carrera.alumnos.append(alumno)
        print("Alumno agregado")

    def agregar_profesor(self, profesor):
        
        self.profesores.append(profesor)
        self.legajos_profesores.append(profesor.legajo)
        self.historial_profesores.append(profesor)
        print("Profesor agregado")
    
    def agregar_administrativo(self, administrativo):
        
        self.administrativos.append(administrativo)
        self.legajos_administrativos.append(administrativo.legajo)
        self.historial_administrativos.append(administrativo)
        print("Administrativo agregado")
    
    def agregar_carrera(self, carrera):
        
        self.carreras.append(carrera)
        print("Carrera agregada")

    def guardarDatos(self):
      
       with open("DatosITBA","wb") as df:
           pickle.dump(self.carreras,df)
           pickle.dump(self.alumnos,df)
           pickle.dump(self.profesores,df)
           pickle.dump(self.administrativos,df)
           pickle.dump(self.historial_alumnos,df)
           pickle.dump(self.historial_profesores,df)
           pickle.dump(self.historial_administrativos,df)
           pickle.dump(self.legajos_alumnos,df)
           pickle.dump(self.legajos_profesores,df)
           pickle.dump(self.legajos_administrativos,df)
           pickle.dump(self.tramites_resueltos,df)
           pickle.dump(self.tramites_abiertos,df)
           pickle.dump(self.historial_tramites,df)



    def cargarDatos(self):
       with open ("DatosITBA","rb") as lf:
           carreras=pickle.load(lf)
           alumnos=pickle.load(lf)
           profesores=pickle.load(lf)
           administrativos=pickle.load(lf)
           historial_alumnos=pickle.load(lf)
           historial_profesores=pickle.load(lf)
           historial_administrativos=pickle.load(lf)
           legajos_alumnos=pickle.load(lf)
           legajos_profesores=pickle.load(lf)
           legajos_admins=pickle.load(lf)
           tramites_resueltos=pickle.load(lf)
           tramites_abiertos=pickle.load(lf)
           historial_tramites=pickle.load(lf)

           self.carreras=carreras
           self.alumnos=alumnos
           self.profesores=profesores
           self.administrativos=administrativos
           self.historial_alumnos=historial_alumnos
           self.historial_profesores=historial_profesores
           self.historial_administrativos=historial_administrativos
           self.legajos_alumnos=legajos_alumnos
           self.legajos_profesores=legajos_profesores
           self.legajos_admins=legajos_admins
           self.tramites_resueltos=tramites_resueltos
           self.tramites_abiertos=tramites_abiertos
           self.historial_tramites=historial_tramites