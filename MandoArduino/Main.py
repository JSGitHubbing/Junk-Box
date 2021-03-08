from MandoArduino.Support import interpreteSerial
from MandoArduino.Controladores.interfazPrograma import *
from MandoArduino.Support.gestorErrores import GestorErrores
from MandoArduino.Support.gestorRutaInicio import gestorRutaInicio
from MandoArduino.UserInterface.cuadroAyuda import *

# Tamaño de la ventana
ancho = 1000
alto = 770


def main():
    pygame.init()
    pygame.font.init()

    size = ancho, alto
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('M A N D O')
    miRuta = gestorRutaInicio()
    gestorErrores = GestorErrores()
    miControlador = InterfazPrograma(miRuta)
    miInterprete = interpreteSerial.InterpreteSerial(puerto='/dev/ttyUSB0', frecuencia=9600)

    while 1:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        pygame.display.update()
        pygame.display.get_surface().fill((0, 0, 0))

        comando = miInterprete.procesarSignal()
        error = miControlador.ejecutarComando(comando)  # Puede devolver None
        # TODO quiero ejecutar la siguiente línea para que muestre errores por notificaciones del sistema
        gestorErrores.notificar(error)

        miControlador.pintar(screen)


if __name__ == '__main__':
    main()
