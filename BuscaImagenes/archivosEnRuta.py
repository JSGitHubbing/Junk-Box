from pathlib import Path
from PIL import Image
Image.MAX_IMAGE_PIXELS = 3299452380

def archivosEnRuta(ruta):
    if type(ruta) != Path:
        ruta = Path(ruta)
    listaElementos = ruta.iterdir()

    for elem in listaElementos:
        if elem.suffix == '.jpg' or elem.suffix == '.png':
            img = Image.open(elem)
            print(img._size)
            if img._size == (64, 64):
                print('ok')
            else:
                print('no es imagen pequeña')





archivosEnRuta('/home/platonium/Imágenes')
