from popularInstitucion import ITBA

#Funcion que permite tomar un objeto en funcion de su id
def getbyId(id):
    for tramite in ITBA.tramites_abiertos:
        if id == tramite.id:
            return tramite
    
    return None



