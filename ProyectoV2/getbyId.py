from ProyectoV2.popularInstitucion import ITBA

def getbyId(id):
    for tramite in ITBA.tramites_abiertos:
        if id == tramite.id:
            return tramite
    
    return None



