import json
from datetime import datetime
import pygame
from MandoArduino.Controladores.controlador import *
from MandoArduino.Support.lectorDeRutas import *
from MandoArduino.Support.notificaciones import *


class ControladorLista(Controlador):
    indiceArchivo = 0
    mostrarAyuda = False
    tiempoUltimaEjecucion = datetime.now()
    lapsoParaRepetir = 0.5

    def __init__(self, ruta):
        self.ruta = ruta if type(ruta) == Path else Path(ruta)
        self.listaArchivos = archivosEnRuta(ruta)

        # TODO llamar a la función de carga de la configuración para asignarlo a una variable diccionario

        # self.configuracionMando = self.cargarConf()

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
            mensajeRutaTope()
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
            controladorNoEncontrado()

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
            self.llamarFuncionComando(signal['command'])

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

    def llamarFuncionComando(self, comando):

        # TODO comprobar el commando en el archivo de configuracion e imprimir por pantalla el nombre

        # print(self.configuracionMando['70'])
        # print(self.configuracionMando['21'])

        if comando == 68:
            self.rebobinar()
        elif comando == 67:
            self.avanzar()
        elif comando == 70:
            self.subirVolumen()
        elif comando == 21:
            self.bajarVolumen()
        elif comando == 9:
            self.flechaArriba()
        elif comando == 7:
            self.flechaAbajo()
        elif comando == 71:
            self.funcStop()
        elif comando == 69:
            self.power()

    @staticmethod
    def cargarConf():
        archivoConfiguracion = open('Data/configuracionMandoArduino.json', 'r')
        datosFichero = archivoConfiguracion.read()
        return json.loads(datosFichero)
