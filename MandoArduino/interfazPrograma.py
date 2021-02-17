from controladorLista import *
import pygame
class InterfazPrograma(ControladorLista):
    tamFuente = 30
    colorSeleccionado =(255, 150, 150)
    colorPorDefecto = (255, 0, 0)

    def __init__(self, ruta):
        ControladorLista.__init__(self, ruta)
        self.myfont = pygame.font.SysFont('Comic Sans MS', self.tamFuente)

    def pintar(self, screen):
        for i in range(len(self.listaArchivos)):
            color = self.colorSeleccionado if i == self.indiceArchivo else self.colorPorDefecto
            textsurface = self.myfont.render(('-' + self.listaArchivos[i].name), False, color)
            screen.blit(textsurface, (50, 50 + 35 * i))