import json
from datetime import datetime
import pygame
from MandoArduino.Controladores.controlador import *
from MandoArduino.Support.lectorDeRutas import *


class ControladorLista(Controlador):
    indiceArchivo = 0
    mostrarAyuda = False
    tiempoUltimaEjecucion = datetime.now()
    lapsoParaRepetir = 0.5

    def __init__(self, ruta):
        Controlador.__init__(self)
        self.ruta = ruta if type(ruta) == Path else Path(ruta)
        self.listaArchivos = archivosEnRuta(ruta)
        self.configuracionMando = self.cargarConf()

    def subirVolumen(self):
        self.indiceArchivo = 0 if self.indiceArchivo - 1 < 0 else self.indiceArchivo - 1

    def bajarVolumen(self):
        self.indiceArchivo = len(self.listaArchivos) - 1 if self.indiceArchivo >= len(
            self.listaArchivos) - 1 else self.indiceArchivo + 1

    def flechaArriba(self):
        self.indiceArchivo = 0 if self.indiceArchivo - 5 < 0 else self.indiceArchivo - 5

    def flechaAbajo(self):
        self.indiceArchivo = len(self.listaArchivos) - 1 if self.indiceArchivo >= len(
            self.listaArchivos) - 5 else self.indiceArchivo + 5

    def rebobinar(self):
        if self.ruta == self.ruta.parent:
            return "ERROR_RUTA_TOPE"
        else:
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
            return "ERROR_CONTROLADOR_NO_ENCONTRADO"

    def recargarRuta(self):
        self.listaArchivos = archivosEnRuta(self.ruta)

    def funcStop(self):
        self.mostrarAyuda = not self.mostrarAyuda

    def power(self):
        miEventoCierre = pygame.event.Event(pygame.QUIT)
        pygame.event.post(miEventoCierre)

    def ejecutarComando(self, signal):
        if signal is None:
            return

        if self.debeEjecutarComando(signal):
            try:
                address = str(signal['address'])
                configuracionMandoConcreto = self.configuracionMando[address]

                comandoMando = str(signal['command'])
                instruccion = configuracionMandoConcreto[comandoMando]
                return self.ejecutarComandoMedianteInstruccion(instruccion)

            except KeyError:
                return "MANDO_NO_CONFIGURADO"

    def debeEjecutarComando(self, signal):
        repeticion = signal['raw-data'] == 0
        if repeticion:
            now = datetime.now()
            diferencia = (now - self.tiempoUltimaEjecucion)
            if diferencia.total_seconds() <= self.lapsoParaRepetir:
                return False
        else:
            self.tiempoUltimaEjecucion = datetime.now()

        return True

    @staticmethod
    def cargarConf():
        archivoConfiguracion = open('Data/configuracionMandoArduino.json', 'r')
        datosFichero = archivoConfiguracion.read()
        return json.loads(datosFichero)
