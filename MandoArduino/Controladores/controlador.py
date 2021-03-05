class Controlador:

    def __init__(self):
        self.comandos = {
             'flechaArriba': lambda: self.flechaArriba(),
             'flechaAbajo': lambda: self.flechaAbajo(),
             'rebobinar': lambda: self.rebobinar(),
             'avanzar': lambda: self.avanzar(),
             'subirVolumen': lambda: self.subirVolumen(),
             'bajarVolumen': lambda: self.bajarVolumen(),
             'funcStop': lambda: self.funcStop(),
             'power': lambda: self.power(),
             'EQ': lambda: self.botonEQ(),
             'Boton_0': lambda: self.boton0(),
             'Boton_1': lambda: self.boton1(),
             'Boton_2': lambda: self.boton2(),
             'Boton_3': lambda: self.boton3(),
             'Boton_4': lambda: self.boton4(),
             'Boton_5': lambda: self.boton5(),
             'Boton_6': lambda: self.boton6(),
             'Boton_7': lambda: self.boton7(),
             'Boton_8': lambda: self.boton8(),
             'Boton_9': lambda: self.boton9(),
             'REPT': lambda: self.stRept()
        }

    @staticmethod
    def botonNoImplementado(nombreBoton):
        print('El botón ' + nombreBoton + ' no está implementado')

    def flechaArriba(self):
        self.botonNoImplementado("Flecha Arriba")

    def flechaAbajo(self):
        self.botonNoImplementado('Flecha Abajo')

    def avanzar(self):
        self.botonNoImplementado('Avanzar')

    def rebobinar(self):
        self.botonNoImplementado('Rebobinar')

    def subirVolumen(self):
        self.botonNoImplementado('Subir volumen')

    def bajarVolumen(self):
        self.botonNoImplementado('Bajar Volumen')

    def playPause(self):
        self.botonNoImplementado('Play/Pausa')

    def botonEQ(self):
        self.botonNoImplementado('EQ')

    def reset(self):
        self.botonNoImplementado('Reset')

    def boton0(self):
        self.botonNoImplementado('0')

    def boton1(self):
        self.botonNoImplementado('1')

    def boton2(self):
        self.botonNoImplementado('2')

    def boton3(self):
        self.botonNoImplementado('3')

    def boton4(self):
        self.botonNoImplementado('4')

    def boton5(self):
        self.botonNoImplementado('5')

    def boton6(self):
        self.botonNoImplementado('6')

    def boton7(self):
        self.botonNoImplementado('7')

    def boton8(self):
        self.botonNoImplementado('8')

    def boton9(self):
        self.botonNoImplementado('9')

    def funcStop(self):
        self.botonNoImplementado('Func/Stop')

    def power(self):
        self.botonNoImplementado('Power')

    def stRept(self):
        self.botonNoImplementado('St/Rept')

    def ejecutarComando(self, comando):
        pass

    def ejecutarComandoMedianteInstruccion(self, instruccion):
        return self.comandos[instruccion]()

