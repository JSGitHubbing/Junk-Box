import os
from pathlib import Path

from MandoArduino.notificaciones import controladorNoEncontrado
from controlador import *
from lectorDeRutas import archivosEnRuta, rutaPadre, calcularIndiceArchivo
class ControladorLista(Controlador):
    indiceArchivo = 0
    mostrarAyuda = False

    def __init__(self, ruta):
        self.ruta = ruta if type(ruta) == Path else Path(ruta)
        self.listaArchivos = archivosEnRuta(ruta)

    def subirVolumen(self):
        self.indiceArchivo = 0 if self.indiceArchivo -1 < 0 else self.indiceArchivo -1
    def bajarVolumen(self):
        self.indiceArchivo = len(self.listaArchivos) - 1 if self.indiceArchivo >= len(self.listaArchivos) - 1 else self.indiceArchivo +1

    def flechaArriba(self):
        self.indiceArchivo = 0 if self.indiceArchivo -5 < 0 else self.indiceArchivo -5
    def flechaAbajo(self):
        self.indiceArchivo = len(self.listaArchivos) - 1 if self.indiceArchivo >= len(self.listaArchivos) - 5 else self.indiceArchivo +5


    def rebobinar(self):
        self.indiceArchivo = calcularIndiceArchivo(self.ruta)
        self.ruta = rutaPadre(self.ruta)
        self.recargarRuta()

    def avanzar(self):
        # si la ruta es un directorio lo abres, si no, mensajito
        if self.listaArchivos[self.indiceArchivo].is_dir():
            self.ruta = self.listaArchivos[self.indiceArchivo]
            self.recargarRuta()
            self.indiceArchivo = 0
        else:
            controladorNoEncontrado()

    def recargarRuta(self):
        self.listaArchivos = archivosEnRuta(self.ruta)

    def funcStop(self):
        self.mostrarAyuda = not self.mostrarAyuda

