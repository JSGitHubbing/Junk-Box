import pygame


class CuadroAyuda:
    @staticmethod
    def pintarNota(screen):
        anchoVentana = screen.get_width()
        altoVentana = screen.get_height()

        color = (77, 77, 0)
        rect = pygame.Rect(anchoVentana - 275, altoVentana - 55, 270, 25)
        pygame.draw.rect(screen, color, rect, 2)
        myfont = pygame.font.SysFont('Consolas', 15)

        textsurface = myfont.render('Presiona FUNC/STOP para ayuda', False, color)
        screen.blit(textsurface, (anchoVentana - 270, altoVentana - 50))

    @staticmethod
    def pintarAyuda(screen):
        anchoVentana = screen.get_width()
        altoVentana = screen.get_height()
        color = (179, 179, 0)
        contenidoAyuda = ['VOL+  Subir en la lista', 'VOL-  Bajar en la lista', 'UP    Subir en la lista 5 elementos',
                          'DOWN  Bajar en la lista 5 elementos', '|<<   Retroceder en arbol de archivos',
                          '>>|   Avanzar en arbol de archivos', 'POWER Apagar']

        alturaAyuda = len(contenidoAyuda) * 20

        rect = pygame.Rect(anchoVentana - 355, altoVentana - (30 + alturaAyuda), 350, alturaAyuda)
        pygame.draw.rect(screen, color, rect, 2)
        myfont = pygame.font.SysFont('Consolas', 15)

        for i in range(len(contenidoAyuda)):
            textsurface = myfont.render(contenidoAyuda[i], False, color)
            screen.blit(textsurface, (anchoVentana - 350, altoVentana - (28 + alturaAyuda) + i * 20))
