import threading
import logging
import time
logging.basicConfig( level=logging.DEBUG,
    format='[%(levelname)s] - %(threadName)-10s : %(message)s')


def daemon():
    time.sleep(2)
    a=2^10
    print (a)
    #logging.debug('Deteniendo')


    
d = threading.Thread(target=daemon, name='Daemon')
d.setDaemon(True)
d.run()
print(d.getName())

