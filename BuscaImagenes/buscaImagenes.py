from pathlib import Path
from PIL import Image
import shutil

Image.MAX_IMAGE_PIXELS = 3299452380


def archivosEnRuta(rutaDondeGuardar, rutaDondeMirar):

    listaElementos = rutaDondeMirar.iterdir()
    extensiones = ['.jpg', '.png']

    for elem in listaElementos:
        if elem.is_dir():
            archivosEnRuta(rutaDondeGuardar, elem)
        elif elem.suffix in extensiones:
            img = Image.open(elem)
            if img._size == (64, 64):
                c = rutaDondeGuardar.joinpath("MisFotitos")
                c.mkdir(0o777, False, True)
                shutil.copy(elem, c)



def clasificarFotos(ruta):
    rutaDondeGuardar = Path(ruta)
    rutaDondeMirar = Path(ruta)
    archivosEnRuta(rutaDondeGuardar, rutaDondeMirar)

clasificarFotos('/home/platonium/Imágenes')