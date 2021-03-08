import json
from json import JSONDecodeError

from serial import *

from MandoArduino.Support.notificaciones import mensajeSerialNoConectado, mensajeNoArduino


class InterpreteSerial:
    def __init__(self, puerto, frecuencia):
        intentosMaximos = 3
        intentos = 0
        while intentos < intentosMaximos:
            try:
                self.arduino = Serial(port=puerto, baudrate=frecuencia, timeout=.1)
                break
            except SerialException:
                intentos += 1
                mensajeSerialNoConectado()
                time.sleep(5)

            if intentos >= intentosMaximos:
                mensajeNoArduino()
                exit()

    def procesarSignal(self):
        signal = self.leerSignal()
        if signal is None:
            return None

        try:
            # TODO recordar quitar esto
            print(signal)
            # Convertir signal a JSON
            return json.loads(signal)
        except JSONDecodeError:
            pass
        return None

    def leerSignal(self):
        signalActual = str(self.arduino.readline().strip())
        if signalActual == "b''":
            return None

        signalActual = signalActual.replace('b', '')
        signalActual = signalActual.replace('\'', '')
        return signalActual
