from interfazPrograma import *


miRuta = '/home/platonium/Vídeos'
#Tamaño de la ventana
ancho = 1000
alto = 800

def main():
    pygame.init()
    pygame.font.init()

    size = ancho, alto
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('M A N D O')

    miControlador = InterfazPrograma(miRuta)


    while 1:
        pygame.display.update()
        pygame.display.get_surface().fill((0, 0, 0))


        miControlador.pintar(screen)




        for event in pygame.event.get():
            if pygame.key.get_pressed()[pygame.K_z]:
                miControlador.rebobinar()

            if pygame.key.get_pressed()[pygame.K_q]:
                miControlador.subirVolumen()
            if pygame.key.get_pressed()[pygame.K_a]:
                miControlador.bajarVolumen()

            if event.type == pygame.QUIT:
                pygame.quit()
                return

if __name__ == '__main__':
    main()
