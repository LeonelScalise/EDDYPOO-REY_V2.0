class Materia:
    def __init__(self, codigo_materia, nombre, creditos, sede, correlativas=[]):
        self.codigo_materia = codigo_materia
        self.nombre = nombre
        self.creditos = creditos
        self.sede = sede
        self.correlativas = correlativas
        self.comisiones = []
        self.profesores = []
        self.alumnos = []

    def str(self):
        return f"{self.codigo_materia} - {self.nombre}"