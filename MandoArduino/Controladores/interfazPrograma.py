from MandoArduino.UserInterface.cuadroAyuda import CuadroAyuda
from MandoArduino.Controladores.controladorLista import *
import pygame


class InterfazPrograma(ControladorLista):
    tamFuente = 30
    colorSeleccionado = (255, 150, 150)
    colorPorDefecto = (255, 0, 0)
    espacioCadaLinea = 35

    posListaX = 50
    posListY = 0

    margenY = 0
    primerIndiceEnPantalla = 0
    ultimoIndiceEnPantalla = 21

    def __init__(self, ruta, gestor):
        ControladorLista.__init__(self, ruta, gestor)
        self.myfont = pygame.font.SysFont('Consolas', self.tamFuente)
        self.miCuadroAyuda = CuadroAyuda()

    def pintar(self, screen):
        pygame.display.get_surface().fill((0, 10, 0))
        if self.mostrarAyuda:
            self.miCuadroAyuda.pintarAyuda(screen)
        else:
            self.miCuadroAyuda.pintarNota(screen)

        self.actualizarDesplazamiento()
        self.pintarListaDeArchivos(screen)

    def pintarListaDeArchivos(self, screen):
        for i in range(len(self.listaArchivos)):
            color = self.colorSeleccionado if i == self.indiceArchivo else self.colorPorDefecto
            textsurface = self.myfont.render(('-' + self.listaArchivos[i].name), False, color)
            screen.blit(textsurface, (self.posListaX, self.posListY + self.espacioCadaLinea * i - self.margenY))
            if color == self.colorSeleccionado:
                f = open('Data/GuardarRuta.txt', 'w')
                f.write(str(rutaPadre(self.listaArchivos[i])))
                f.close()

    def actualizarDesplazamiento(self):
        if self.indiceArchivo > self.ultimoIndiceEnPantalla:
            self.recalcularDesplazamientoVertical(self.indiceArchivo - self.ultimoIndiceEnPantalla)
        elif self.indiceArchivo < self.primerIndiceEnPantalla:
            self.recalcularDesplazamientoVertical(self.indiceArchivo - self.primerIndiceEnPantalla)

    def recalcularDesplazamientoVertical(self, incremento):
        self.primerIndiceEnPantalla += incremento
        self.ultimoIndiceEnPantalla += incremento
        self.margenY = self.primerIndiceEnPantalla * self.espacioCadaLinea
