import subprocess


def sendmessage(message):
    subprocess.Popen(['notify-send', message])
    return


def controladorNoEncontrado():
    sendmessage('Controlador NO encontrado')


def mensajeRutaTope():
    sendmessage("Has llegado a la ruta \"\\\" (root) no puedes volver atrás")
