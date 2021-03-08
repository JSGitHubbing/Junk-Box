import pygame
from MandoArduino.Controladores.interfazPrograma import InterfazPrograma, Path

class InterfazTest:
    def test_inicializarControlador(self):
        self.miControlador = InterfazPrograma("/")
        ruta = Path("/")
        assert self.miControlador.ruta == ruta, "La ruta debería ser / (root)"

    def test_MovertePorLasCarpetas(self):
        self.miControlador.bajarVolumen()
        assert self.miControlador.indiceArchivo == 1, "El índice debería incrementar en 1"

        self.miControlador.subirVolumen()
        assert self.miControlador.indiceArchivo == 0, "El índice debería decrementar en 1"

        self.miControlador.flechaAbajo()
        assert self.miControlador.indiceArchivo == 5, "El índice debería incrementar en 5"

        self.miControlador.flechaArriba()
        assert self.miControlador.indiceArchivo == 0, "El índice debería decrementar en 5"

        self.miControlador.avanzar()
        ruta = Path("/srv")
        assert self.miControlador.ruta == ruta, "La ruta debería ser /srv"

        self.miControlador.rebobinar()
        ruta = Path("/")
        assert self.miControlador.ruta == ruta, "La ruta debería ser / (root)"

    def test_RecibirSeñales(self):
        signal = {}
        signal["raw-data"] = 1

        signal['command'] = 21
        self.miControlador.ejecutarComando(signal)
        assert self.miControlador.indiceArchivo == 1, "El índice debería incrementar en 1"

        signal["command"] = 70
        self.miControlador.ejecutarComando(signal)
        assert self.miControlador.indiceArchivo == 0, "El índice debería decrementar en 1"

        signal["command"] = 7
        self.miControlador.ejecutarComando(signal)
        assert self.miControlador.indiceArchivo == 5, "El índice debería incrementar en 5"

        signal["command"] = 9
        self.miControlador.ejecutarComando(signal)
        assert self.miControlador.indiceArchivo == 0, "El índice debería decrementar en 5"

        signal["command"] = 67
        self.miControlador.ejecutarComando(signal)
        ruta = Path("/srv")
        assert self.miControlador.ruta == ruta, "La ruta debería ser /srv"

        signal["command"] = 68
        self.miControlador.ejecutarComando(signal)
        ruta = Path("/")
        assert self.miControlador.ruta == ruta, "La ruta debería ser / (root)"



    def lanzarTodosLosTests(self):
        self.test_inicializarControlador()
        self.test_MovertePorLasCarpetas()
        self.test_RecibirSeñales()
        print()
        print("***********************************************")
        print("\tTest de interfaz finalizados con éxito")
        print("***********************************************")

def initTestEnvironment():
    pygame.init()
    pygame.font.init()

    size = 200, 200
    pygame.display.set_mode(size)
    pygame.display.set_caption('M A N D O')


if __name__ == '__main__':
    initTestEnvironment()

    testDeInterfaz = InterfazTest()
    testDeInterfaz.lanzarTodosLosTests()
