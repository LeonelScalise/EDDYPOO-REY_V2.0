class Comision:
    def __init__(self, codigo_comision, aula, profesor,materia, dia_y_horario = {}):
        self.codigo_comision = codigo_comision
        self.aula = aula
        self.profesor = profesor
        self.dia_y_horario = dia_y_horario
        self.alumnos = []
        self.materia=materia

        
    def __str__(self):
        return "La comision {self.codigo_comision}, de la materia {self.materia} la dicta el profesor {self.profesor} de la materia "