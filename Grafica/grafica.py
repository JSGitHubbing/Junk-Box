import pygame, os
from Cuentapalabras import CuentapalabrasLector
class opciones:
    espaciado = 10
    anchoBarra = 50
    intervalo = 500
    anchoVentana = 800
    altoVentana = 600
    margenX = 100
    margenY = 100
    tamanyoEscalaX = anchoVentana-margenX
    tamanyoEscalaY = altoVentana-margenY

class Colores:
    azulClarito = (9, 165, 171)
    rojo = (255, 0, 0)
    verde = (0, 255, 0)
    azul = (0, 0, 255)
    blanco = (255, 255, 255)
    negro = (0, 0, 0)

class Posicion:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Grafica:
    conjuntoBarras = []

    def __init__(self, screen, valores, posicion):
        self.screen = screen
        self.x = len(valores)

        self.valores = valores
        self.posicion = posicion

        valorMaximo = self.calcValorMax()
        self.miEscala = Escala(screen, posicion, valorMaximo)
        if self.x < 12:
            for i in range(self.x):
                alto = self.calcularAlturaBarra(opciones.tamanyoEscalaY, valorMaximo, self.valores[i])
                posX = self.posicion.x + opciones.espaciado + i * (opciones.espaciado + opciones.anchoBarra)
                posY = self.posicion.y - alto
                anchor = opciones.anchoBarra
                miBarra = Barra(screen, posX, posY, alto, anchor)
                self.conjuntoBarras.append(miBarra)

        else:
            for i in range(self.x):
                alto = self.calcularAlturaBarra(opciones.tamanyoEscalaY, valorMaximo, self.valores[i])
                posX = self.posicion.x + i * opciones.tamanyoEscalaX/self.x
                posY = self.posicion.y - alto
                anchor = opciones.tamanyoEscalaX/self.x
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
    grosor = 2

    def __init__(self, screen, x, y, valor, ancho):
        self.screen = screen
        self.x = x
        self.y = y
        self.z = valor
        self.ancho = ancho

    def pintar(self):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x+3, self.y, self.ancho, self.z), self.grosor)

class Escala:
    color = Colores.rojo
    grosor = 3
    def __init__(self,screen, posicion, valorMaximo):
        self.posicion = posicion
        self.screen = screen
        self.valorMaximo = valorMaximo
        self.numIntervalos = int(valorMaximo/opciones.intervalo)
        self.valorIntervalo = valorMaximo/self.numIntervalos

    def pintar(self):
        pygame.draw.line(self.screen, self.color, (self.posicion.x, self.posicion.y),
                         (self.posicion.x, self.posicion.y-opciones.tamanyoEscalaY), self.grosor)
        pygame.draw.line(self.screen, self.color, (self.posicion.x, self.posicion.y),
                         (self.posicion.x+opciones.tamanyoEscalaX, self.posicion.y), self.grosor)

        distanciaEntreIntervalos = opciones.tamanyoEscalaY/self.numIntervalos

        for i in range(self.numIntervalos + 1):
            pygame.draw.line(self.screen, self.color, (self.posicion.x - 5, self.posicion.y - distanciaEntreIntervalos*i),
                             (self.posicion.x + 5, self.posicion.y - distanciaEntreIntervalos*i), self.grosor)
            myfont = pygame.font.SysFont('Comic Sans MS', 10)
            textsurface = myfont.render(str(int(i*self.valorIntervalo)), False, Colores.verde)
            self.screen.blit(textsurface, (35, self.posicion.y - distanciaEntreIntervalos*i - 5))

def main():
    pygame.init()
    pygame.font.init()

    size = opciones.anchoVentana, opciones.altoVentana
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Gráfica de barras')
    # pygame.mouse.set_visible(0)

    posicion = Posicion(75, opciones.altoVentana - 50)

    valores = CuentapalabrasLector.crearListas('el_quijoteBis.csv')
    valores = CuentapalabrasLector.filtrarPorValor(valores, 20)
    valores = CuentapalabrasLector.limitarA(valores, 40)

    miGrafica = Grafica(screen, valores, posicion)

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