import json
from json import JSONDecodeError

import serial


class InterpreteSerial:
    def __init__(self, puerto, frecuencia):
        self.arduino = serial.Serial(port=puerto, baudrate=frecuencia, timeout=.1)

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
