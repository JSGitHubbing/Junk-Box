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
