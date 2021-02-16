import pygame, os

miRuta = '../../Vídeos'
#Tamaño de la ventana
ancho = 1000
alto = 800

tamFuente = 30

def crearLasListas(ruta):
    listaElementos = os.listdir(ruta)
    fileList = []
    directoryList = []
    for elem in listaElementos:
        if os.path.isdir(ruta+"/"+elem):
            directoryList.append(elem)
        else:
            fileList.append(elem)
    return directoryList, fileList


def pintarListas(lista, screen):
    for i in range(len(lista)):
        myfont = pygame.font.SysFont('Comic Sans MS', tamFuente)
        textsurface = myfont.render(('-' + lista[i]), False, (255, 0, 0))
        screen.blit(textsurface, (50, 50 + 35 * i ))



def main():
    pygame.init()
    pygame.font.init()

    size = ancho, alto
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('M A N D O')

    while 1:
        pygame.display.update()
        pygame.display.get_surface().fill((0, 0, 0))

        pintarListas(crearLasListas(miRuta)[1], screen)





        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

if __name__ == '__main__':
    main()
