import os


def gestorRutaInicio():
    if not os.path.exists('Data/GuardarRuta.txt'):
        f = open('Data/GuardarRuta.txt', 'w')
        f.write('/home')
        f.close()
    f = open('Data/GuardarRuta.txt', 'r')
    miRuta = f.readline()
    f.close()
    return miRuta
