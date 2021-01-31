import os
import re
def leerPorPalabra(ruta):
    if os.path.isfile(ruta):
        palabrasEnLista = []
        file = open(ruta, 'r')
        for line in file:
            for word in line.split():
                palabrasEnLista.append(word)
        file.close()
        palabrasMin = []
        for word in palabrasEnLista:
            palabrasMin.append(word.lower())

    else:
        print('No existe un archivo en esta ruta')

    palabras = []
    for word in palabrasMin:
        palabras.append(re.sub('\W+', '', word))
    return palabras

def contarPalabras(listaDePalabras):
    frecuenciaPalab = []
    for word in listaDePalabras:
        frecuenciaPalab.append(listaDePalabras.count(word))
    return(list(zip(frecuenciaPalab, listaDePalabras)))

def ordenar(listaContada):
    listaContada.sort(reverse=True)
    limpia = []
    for item in listaContada:
        if item not in limpia:
            limpia.append(item)
    return limpia

def escribir(ordenada, ruta):
    archivo = open(ruta, 'w')
    for i in range(len(ordenada)):
        archivo.write(ordenada[i][1]+'\t'+str(ordenada[i][0])+'\n')
    archivo.close()

x = leerPorPalabra('Prologo.pag')
y = contarPalabras(x)
z = ordenar(y)
escribir(z, 'Prologo.csv')



