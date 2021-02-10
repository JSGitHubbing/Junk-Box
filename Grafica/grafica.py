import pygame, os, sys
class opciones:
    espaciado = 10
    anchoBarra = 50

class Grafica:
    conjuntoBarras = []

    def __init__(self, screen, valores):
        self.screen = screen
        self.x = len(valores)
        self.miEscala = Escala(screen, 50, 550)
        self.valores = valores

        for i in range(self.x):
            posX = self.miEscala.x+opciones.espaciado+i*(opciones.espaciado+opciones.anchoBarra)
            posY = self.miEscala.y-(self.valores[i]/self.calcValorMax()*500)
            alto = 500 * (self.valores[i]/self.calcValorMax())
            anchor = opciones.anchoBarra

            miBarra = Barra(screen, posX, posY, alto, anchor)

            self.conjuntoBarras.append(miBarra)

    def calcValorMax(self):
        maximo = 0
        for i in self.valores:
            if i > maximo:
                maximo = i
        return maximo

    def pintar(self):
        for c in self.conjuntoBarras:
            c.pintar()
        self.miEscala.pintar()


class Barra:

    color = (9, 165, 171)

    def __init__(self, screen, x, y, valor, ancho):
        self.screen = screen
        self.x = x
        self.y = y
        self.z = valor
        self.ancho = ancho

    def pintar(self):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x, self.y, self.ancho, self.z), 2)

class Escala:
    color = (255, 0, 0)
    def __init__(self,screen, x, y):
        self.x = x
        self.y = y
        self.screen = screen

    def pintar(self):
        pygame.draw.line(self.screen, self.color, (self.x, self.y), (self.x, self.y-500), 3)
        pygame.draw.line(self.screen, self.color, (self.x, self.y), (self.x+700, self.y), 3)




def main():
    pygame.init()

    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Gráfica de barras')
    pygame.mouse.set_visible(0)


    miGrafica = Grafica(screen, (100, 150, 75, 800, 125, 250))

    while 1:
        pygame.display.update()
        pygame.display.get_surface().fill((0, 0, 0))

        miGrafica.pintar()



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

if __name__ == '__main__':
    main()