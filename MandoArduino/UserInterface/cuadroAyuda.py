import pygame


class CuadroAyuda:
    @staticmethod
    def pintarNota(screen):
        anchoVentana = screen.get_width()
        altoVentana = screen.get_height()

        color = (77, 77, 0)
        rect = pygame.Rect(anchoVentana - 225, altoVentana - 55, 220, 25)
        pygame.draw.rect(screen, color, rect, 2)
        myfont = pygame.font.SysFont('Consolas', 15)

        textsurface = myfont.render('Presiona \"H\" para ayuda', False, color)
        screen.blit(textsurface, (anchoVentana - 220, altoVentana - 50))

    @staticmethod
    def pintarAyuda(screen):
        anchoVentana = screen.get_width()
        altoVentana = screen.get_height()
        color = (179, 179, 0)
        contenidoAyuda = ['Q - Subir en la lista', 'A - Bajar en la lista', 'W - Subir en la lista 5 elementos',
                          'S - Bajar en la lista 5 elementos', 'Z - Retroceder en arbol de archivos',
                          'X - Avanzar en arbol de archivos']

        alturaAyuda = len(contenidoAyuda) * 20

        rect = pygame.Rect(anchoVentana - 355, altoVentana - (30 + alturaAyuda), 350, alturaAyuda)
        pygame.draw.rect(screen, color, rect, 2)
        myfont = pygame.font.SysFont('Consolas', 15)

        for i in range(len(contenidoAyuda)):
            textsurface = myfont.render(contenidoAyuda[i], False, color)
            screen.blit(textsurface, (anchoVentana - 350, altoVentana - (28 + alturaAyuda) + i * 20))
