from MandoArduino.Controladores.controlador import Controlador
import pyautogui as bot
import keyboard


class ControladorVLC(Controlador):
    def __init__(self, gestor):
        Controlador.__init__(self, gestor)
        keyboard.press_and_release(' ')
        bot.press('')

    def power(self):
        # TODO cerrar VLC
        keyboard.press_and_release('ctrl+q')
        self.miGestor.cargarControladorInterfaz()

    def funcStop(self):
        bot.press('f')
