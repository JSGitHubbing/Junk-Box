import os
from controlador import *
from lectorDeRutas import archivosEnRuta, rutaPadre
class ControladorLista(Controlador):
    indiceArchivo = 0
    def __init__(self, ruta):
        self.ruta = ruta
        self.listaArchivos = archivosEnRuta(ruta)

    def subirVolumen(self):
        self.indiceArchivo = 0 if self.indiceArchivo -1 < 0 else self.indiceArchivo -1
    def bajarVolumen(self):
        self.indiceArchivo = len(self.listaArchivos) - 1 if self.indiceArchivo >= len(self.listaArchivos) - 1 else self.indiceArchivo +1
    def flechaArriba(self):
        self.indiceArchivo = 0 if self.indiceArchivo -1 < 0 else self.indiceArchivo -3
    def flechaAbajo(self):
        self.indiceArchivo = len(self.listaArchivos) - 1 if self.indiceArchivo >= len(self.listaArchivos) - 1 else self.indiceArchivo +3


    def rebobinar(self):
        self.ruta = rutaPadre(self.ruta)
        self.listaArchivos = archivosEnRuta(self.ruta)