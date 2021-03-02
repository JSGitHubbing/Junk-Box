from MandoArduino import notificaciones, interpreteSerial
from interfazPrograma import *
from cuadroAyuda import *
import serial, json


f = open('GuardarRuta.txt', 'r')
miRuta = f.readline()
f.close()

#Tamaño de la ventana
ancho = 1000
alto = 770


def comprobarTeclas(miControlador):
    if pygame.key.get_pressed()[pygame.K_z]:
        miControlador.rebobinar()
    if pygame.key.get_pressed()[pygame.K_x]:
        miControlador.avanzar()

    if pygame.key.get_pressed()[pygame.K_q]:
        miControlador.subirVolumen()
    if pygame.key.get_pressed()[pygame.K_a]:
        miControlador.bajarVolumen()

    if pygame.key.get_pressed()[pygame.K_w]:
        miControlador.flechaArriba()
    if pygame.key.get_pressed()[pygame.K_s]:
        miControlador.flechaAbajo()

    if pygame.key.get_pressed()[pygame.K_h]:
        miControlador.funcStop()

    if pygame.key.get_pressed()[pygame.K_n]:
        notificaciones.controladorNoEncontrado()

def main():
    pygame.init()
    pygame.font.init()

    size = ancho, alto
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('M A N D O')

    miControlador = InterfazPrograma(miRuta)
    miInterprete = interpreteSerial.InterpreteSerial(puerto='/dev/ttyUSB0', frecuencia=9600)

    while 1:
        pygame.display.update()
        pygame.display.get_surface().fill((0, 0, 0))

        comando = miInterprete.procesarSignal()
        miControlador.ejecutarComando(comando)
        miControlador.pintar(screen)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                comprobarTeclas(miControlador)
            if event.type == pygame.QUIT:
                pygame.quit()
                return

if __name__ == '__main__':
    main()
