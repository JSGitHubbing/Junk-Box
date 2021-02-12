import os

def crearListas(ruta):
    res = []
    if os.path.isfile(ruta):
        file = open(ruta, 'r')
        for line in file:
            miLinea = line.split('\t')
            valorSucio = miLinea[1]
            valorLimpio = int(valorSucio.strip())
            #if(valorLimpio > 20):
            #    res.append(valorLimpio)
            res.append(valorLimpio)
        file.close()
    else:
        print('No existe un archivo en esa ruta')

    return res

def limitarA(listaValores, cantidad):
    res = []
    for index in range(cantidad):
        res.append(listaValores[index])
    return res

def filtrarPorValor(listaValores, valorMin):
    res = []
    for valor in listaValores:
        if(valor >= valorMin):
            res.append(valor)
    return res

