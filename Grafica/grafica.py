import pygame, os, sys
class opciones:
    espaciado = 10
    anchoBarra = 50
    intervalo = 100
    anchoVentana = 1000
    altoVentana = 800
    tamanyoEscalaX = anchoVentana-100
    tamanyoEscalaY = altoVentana-100

class Colores:
    azulClarito = (9, 165, 171)
    rojo = (255,0,0)
    verde = (0,255,0)
    azul = (0,0,255)
    blanco = (255,255,255)
    negro = (0,0,0)

class Grafica:
    conjuntoBarras = []

    def __init__(self, screen, valores):
        self.screen = screen
        self.x = len(valores)

        self.valores = valores

        valorMaximo = self.calcValorMax()
        numIntervalos = int(valorMaximo/opciones.intervalo)
        self.miEscala = Escala(screen, 50, opciones.altoVentana-50, numIntervalos)

        for i in range(self.x):
            alto = self.calcularAlturaBarra(opciones.tamanyoEscalaY, valorMaximo, self.valores[i])
            posX = self.miEscala.x + opciones.espaciado + i * (opciones.espaciado + opciones.anchoBarra)
            posY = self.miEscala.y - alto
            anchor = opciones.anchoBarra

            miBarra = Barra(screen, posX, posY, alto, anchor)

            self.conjuntoBarras.append(miBarra)

    def calcValorMax(self):
        maximo = 0
        for i in self.valores:
            if i > maximo:
                maximo = i
        return (int(maximo / opciones.intervalo) + 1) * opciones.intervalo

    def calcularAlturaBarra(self, pixelsEscala, valorMaximo, valorBarra):
        return valorBarra / valorMaximo * pixelsEscala

    def pintar(self):
        for c in self.conjuntoBarras:
            c.pintar()
        self.miEscala.pintar()


class Barra:

    color = Colores.azulClarito

    def __init__(self, screen, x, y, valor, ancho):
        self.screen = screen
        self.x = x
        self.y = y
        self.z = valor
        self.ancho = ancho

    def pintar(self):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x, self.y, self.ancho, self.z), 2)

class Escala:
    color = Colores.rojo
    def __init__(self,screen, x, y, numIntervalos):
        self.x = x
        self.y = y
        self.screen = screen
        self.numIntervalos = numIntervalos

    def pintar(self):
        pygame.draw.line(self.screen, self.color, (self.x, self.y), (self.x, self.y-opciones.tamanyoEscalaY), 3)
        pygame.draw.line(self.screen, self.color, (self.x, self.y), (self.x+opciones.tamanyoEscalaX, self.y), 3)
        for i in range(self.numIntervalos + 1):
            pygame.draw.line(self.screen, self.color, (self.x - 5, self.y - opciones.intervalo*i), (self.x + 5, self.y - opciones.intervalo*i), 3)

def main():
    pygame.init()

    size = opciones.anchoVentana, opciones.altoVentana
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Gráfica de barras')
    # pygame.mouse.set_visible(0)


    miGrafica = Grafica(screen, (100, 150, 75, 125, 20, 400, 1200))

    while 1:
        pygame.display.update()
        pygame.display.get_surface().fill(Colores.negro)

        miGrafica.pintar()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

if __name__ == '__main__':
    main()