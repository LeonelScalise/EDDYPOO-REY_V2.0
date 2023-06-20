class Tramite():
    def __init__(self, id, alumno, administrativo, tipo_de_tramite, fecha_de_inicio, profesor = None, estado="Pendiente"):
        self.id = id
        self.alumno = alumno
        self.administrativo = administrativo
        self.tipo_de_tramite = tipo_de_tramite
        self.fecha_de_inicio = fecha_de_inicio
        self.estado = estado
        self.profesor = profesor
    def __str__(self):
        return "{} es un tramite del tipo: {}, creado por {} y el administrativo encargado es {}".format(self.id,self.tipo_de_tramite,self.alumno,self.administrativo)