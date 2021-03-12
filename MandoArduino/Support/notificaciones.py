import subprocess


def sendmessage(message):
    subprocess.Popen(['notify-send', message])
    return


def mensajeControladorNoEncontrado():
    sendmessage('Controlador NO encontrado')


def mensajeRutaTope():
    sendmessage("Has llegado a la ruta \"\\\" (root) no puedes volver atrás")


def mensajeMandoNoConfigurado():
    sendmessage("La configuración de ese mando no te permite realizar esa acción")


def mensajeSerialNoConectado():
    sendmessage("Conecta el serial de Arduino. Reintentando en 5 segundos")


def mensajeNoArduino():
    sendmessage("No se ha podido establecer la conexion tras los intentos")


def mensajeNoExtension():
    sendmessage("No se pueden abrir archivos con esta extensión.")
