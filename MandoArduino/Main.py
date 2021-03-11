from MandoArduino.Controladores.gestorControladores import GestorControladores
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
    elGestor = GestorControladores()

    while 1:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        pygame.display.update()

        elGestor.ejecutar(screen)


if __name__ == '__main__':
    main()
