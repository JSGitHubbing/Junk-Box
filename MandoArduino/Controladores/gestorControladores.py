from time import sleep

from MandoArduino.Controladores.controladorVLC import ControladorVLC
from MandoArduino.Controladores.interfazPrograma import InterfazPrograma
from MandoArduino.Support import interpreteSerial
from MandoArduino.Support.gestorErrores import GestorErrores
from MandoArduino.Support.gestorRutaInicio import gestorRutaInicio


class GestorControladores:
    def __init__(self):
        self.gestorErrores = GestorErrores()
        self.miInterprete = interpreteSerial.InterpreteSerial(puerto='/dev/ttyUSB0', frecuencia=9600)
        miRuta = gestorRutaInicio()

        self.diccionarioControladores = {
            'Interfaz': InterfazPrograma(miRuta, self),
            'VLC': ControladorVLC(self)
        }
        self.cargarControladorInterfaz()

    def ejecutar(self, screen):
        comando = self.miInterprete.procesarSignal()
        if comando:
            error = self.controladorActivo.ejecutarComando(comando)  # Puede devolver None
            self.gestorErrores.notificar(error)
        if type(self.controladorActivo) == InterfazPrograma:
            self.controladorActivo.pintar(screen)

    def cargarControlador(self,etiquetaControlador):
        self.controladorActivo = self.diccionarioControladores[etiquetaControlador]
        sleep(1)
        self.miInterprete.arduino.flushInput()


    def cargarControladorInterfaz(self):
        self.cargarControlador('Interfaz')

