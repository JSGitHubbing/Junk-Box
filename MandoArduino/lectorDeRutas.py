import re
from pathlib import Path

def esOculto(ruta):
    return ruta.name.startswith('.')


def archivosEnRuta(ruta):
    if type(ruta) != Path:
        ruta = Path(ruta)
    listaElementos = ruta.iterdir()


    fileList = []
    allList = []
    for elem in listaElementos:
        if not esOculto(elem):
            if elem.is_dir():
                allList.append(elem)
            elif elem.is_file():
                fileList.append(elem)

    allList.extend(fileList)

    return allList

def rutaPadre(ruta):
    return Path(ruta).parent

def calcularIndiceArchivo(rutaArchivo):
    listaArchivos = archivosEnRuta(rutaPadre(rutaArchivo))
    return listaArchivos.index(rutaArchivo)




