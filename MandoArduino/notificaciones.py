import subprocess

def sendmessage(message):
    subprocess.Popen(['notify-send', message])
    return

def controladorNoEncontrado():
    sendmessage('Controlador NO encontrado')


