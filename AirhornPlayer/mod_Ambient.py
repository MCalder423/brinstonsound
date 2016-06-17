
__author__ = 'marc'

import mod_playwav
import FileUtils
from threading import Thread
import TextToSpeech as tts
import random
import time

class Mythread (Thread):
    def __init__(self, card, f, vol, bal):
        Thread.__init__(self)
        self.card = card
        self.file = f
        self.volume = vol
        self.balance = bal
    def run(self):
       mod_playwav.play(self.card, self.file, self.volume, self.balance)

def play(soundClip):
        # Read the Ambientsounds configuration item
        ambientsound = FileUtils.GetConfigValue("general", "ambientsound")
        # Begin a loop
        while ambientsound == "on":
            # Calculate the amount of time to sleep this thread
            sleepTime = random.randrange(soundClip.minInterval, soundClip.maxInterval)

            # Sleep this thread
            time.sleep(sleepTime)

            # Play the configured Ambient sound
            try:
                card = FileUtils.GetConfigValue("audio_ports", soundClip.audioPort)
                # Play the clip on a separate thread
                t = Mythread(card, soundClip.fileSpec, soundClip.volume, soundClip.balance)
                t.start()
            except:
                tts.SayThis("Oops!  Something went boom.")

            # Check to see if ambient sounds are still on
            ambientsound = FileUtils.GetConfigValue("general", "ambientsound")

        print ("Ambient sound " + str(soundClip.switchNumber) + " - finishing thread.")