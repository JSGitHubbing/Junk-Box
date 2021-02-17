import pygame
class PintarLista:
    def __init__(self, screen, lista, tamFuente):
        self.screen = screen
        self.lista = lista
        self.tamFuente = tamFuente

    def pintar(self):
        for i in range(len(self.lista)):
            myfont = pygame.font.SysFont('Comic Sans MS', self.tamFuente)
            textsurface = myfont.render(('-' + self.lista[i]), False, (255, 0, 0))
            self.screen.blit(textsurface, (50, 50 + 35 * i))