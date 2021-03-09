from MandoArduino.Controladores.controlador import Controlador


class ControladorVLC(Controlador):
    def __init__(self, gestor):
        Controlador.__init__(self, gestor)

    def power(self):
        self.miGestor.cargarControladorInterfaz()

