
class Tramite():
    def __init__(self, id, alumno, administrativo, tipo_de_tramite, fecha_de_inicio, profesor = None, estado="Pendiente", comision=None):
        self.id = id
        self.alumno = alumno
        self.administrativo = administrativo
        self.tipo_de_tramite = tipo_de_tramite
        self.fecha_de_inicio = fecha_de_inicio
        self.estado = estado
        self.profesor = profesor
        self.comision = comision
    
    def __str__(self):
        return f"{self.id} es un tramite del tipo: {self.tipo_de_tramite}, creado por {self.alumno} y el administrativo encargado es {self.administrativo}"
    
    