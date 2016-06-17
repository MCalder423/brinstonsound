__author__ = 'mcalder'
# This is an implementation of pyttsx.
# The docs for pyttsx can be found at http://pyttsx.readthedocs.org/en/latest/engine.html

import pyttsx
import threading
import Queue

# engine = pyttsx.init()
# engine.say('Throw me a frickin bone here.  I\'m the boss.  Need the info.')
# engine.runAndWait()
#
# for voice in engine.getProperty('voices'):
#     print (voice.name)
# print (engine.getProperty('rate'))
# print (engine.getProperty('volume'))

def SayThis (whatToSay):
    q = Queue.Queue

    t = threading.Thread(target=__CallEngine, args=(whatToSay,))
    t.daemon = True
    t.start()
    t.join()

def __CallEngine(whatToSay):
    engine = pyttsx.init()
    #engine.setProperty('voice', 'en-scottish')
    engine.setProperty('voice', 'english-us')
    engine.setProperty('rate', 130)
    engine.say(whatToSay)
    engine.runAndWait()
    return
