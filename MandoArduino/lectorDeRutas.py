import os
from pathlib import Path

def archivosEnRuta(ruta):
    if type(ruta) != Path:
        ruta = Path(ruta)

    listaElementos = ruta.iterdir()
    fileList = []
    allList = []
    for elem in listaElementos:
        if elem.is_dir():
            allList.append(elem)
        else:
            fileList.append(elem)

    allList.extend(fileList)

    return allList

def rutaPadre(ruta):
    return Path(ruta).parent


