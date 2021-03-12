import json


def cargarConfiguracionJson(rutaArchivoConfiguracion):
    archivoConfiguracion = open(rutaArchivoConfiguracion, 'r')
    datosFichero = archivoConfiguracion.read()
    return json.loads(datosFichero)
