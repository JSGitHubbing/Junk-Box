import json, serial

class InterpreteSerial:
    def __init__(self, puerto, frecuencia):
        self.arduino = serial.Serial(port=puerto, baudrate=frecuencia, timeout=.1)

    def procesarSignal(self):
        signal = self.leerSignal()
        if signal == None:
            return None

        try:
            print(signal)
            # Convertir signal a JSON
            dict = json.loads(signal)
            return dict['command']
        except:
            pass
        return None

    def leerSignal(self):
        signalActual = str(self.arduino.readline().strip())
        if signalActual == "b''":
            return None

        signalActual = signalActual.replace('b', '')
        signalActual = signalActual.replace('\'', '')
        return signalActual

    def transformarSignalComando(self, datosSignal):
        pass
