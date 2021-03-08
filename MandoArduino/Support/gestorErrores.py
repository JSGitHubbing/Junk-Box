from MandoArduino.Support import notificaciones


class GestorErrores:
    @staticmethod
    def notificar(error):

        if error:
            if error == "MANDO_NO_CONFIGURADO":
                notificaciones.mensajeMandoNoConfigurado()
            elif error == "ERROR_CONTROLADOR_NO_ENCONTRADO":
                notificaciones.mensajeControladorNoEncontrado()
            elif error == "ERROR_RUTA_TOPE":
                notificaciones.mensajeRutaTope()
