import mod_Ambient

__author__ = 'mcalder'

# this is the Airhorn Player bootstrap script.
# It also allows for console input to simulate switch events.

import FileUtils
import TextToSpeech as tts
import mod_MessageHandler
from threading import Thread
import SoundClip
import mod_playwav
import socketserver
from socketserver import BaseRequestHandler, UDPServer


class UDPMessageHandler(BaseRequestHandler):
    def handle(self):
        mod_MessageHandler.message('Got connection from', self.client_address)
        # Get message and client socket
        msg, sock = self.request
        mod_MessageHandler.message('Received ' + msg + ' from client.')
        # resp = time.ctime()
        # sock.sendto(resp.encode('ascii'), self.client_address)
        if msg == 'q':
            mod_MessageHandler.message("Received shutdown signal from network.")
            # FileUtils.SetConfigValue("general", "ambientsound", "off")
            # # Wait until all ambient threads have exited
            # tts.SayThis('Waiting ' + str(maxThreadWaitTime + 2) + ' seconds for ambient sounds to drain.')
            # time.sleep(maxThreadWaitTime + 2)
            # tts.SayThis("Tah tah for now.")
            #
            # exit()

        elif msg == 'm':
            # Mute all sounds
            FileUtils.SetConfigValue("general", "switchsound", "off")
            FileUtils.SetConfigValue("general", "ambientsound", "off")
        elif msg == 'u':
            # Unmute all sounds
            FileUtils.SetConfigValue("general", "switchsound", "on")
            FileUtils.SetConfigValue("general", "ambientsound", "on")
            LoadAmbientSounds()
        else:
            try:
                ProcessSwitch(msg)
            except:
                mod_MessageHandler.error('Got invalid data from the switch processor.')

class Switchplayerthread (Thread):
    def __init__(self, card, f, vol, bal):
        Thread.__init__(self)
        self.card = card
        self.file = f
        self.volume = vol
        self.balance = bal
    def run(self):
       mod_playwav.play(self.card, self.file, self.volume, self.balance)

class Ambientplayerthread (Thread):
    def __init__(self, soundClip):
        Thread.__init__(self)
        self.soundClip = soundClip
    def run(self):
       mod_Ambient.play(self.soundClip)

def LoadAmbientSounds():
    # Load up all the ambient sounds and spin them up, each on its own thread.
    for ambientClip in range(1, 17, 1):
        soundClip = SoundClip.SoundClip()
        soundClip.Load(AirhornSoundDrive, 'A', str(ambientClip))
        # Check that we have a sound config loaded
        if soundClip.fileSpec != "":
            t = Ambientplayerthread(soundClip)
            t.start()
            # Since we found at least one ambient sound clip, turn on ambient sound by updating the config file.
            FileUtils.SetConfigValue("general", "ambientsound", "on")

def ProcessSwitch(switch):
        # Check that switch sounds are on
        switchsound = FileUtils.GetConfigValue("general", "ambientsound")
        if switchsound == 'on':
            soundClip = SoundClip.SoundClip()
            soundClip.Load(AirhornSoundDrive, 'S', switch)
            # Check that we have a sound config loaded
            if soundClip.fileSpec == "":
                tts.SayThis("No sound configured for switch " + switch)
            else:
                try:
                    card = FileUtils.GetConfigValue("audio_ports", soundClip.audioPort)
                    # Play the clip on a separate thread
                    t = Switchplayerthread(card, soundClip.fileSpec, soundClip.volume, soundClip.balance)
                    t.start()
                except:
                    mod_MessageHandler.error("Oops!  Something went boom in AirhornPlayer ProcessSwitch.")

###############################################################################
# MAINLINE CODE
###############################################################################

#  Check to see if we have a valid Airhorn Sound drive connected.
AirhornSoundDrive = FileUtils.FindAirhornSoundDrive()
if AirhornSoundDrive == None:
    #wavplayer_alsaaudio.play('SystemSounds/needinfo.wav')
    mod_MessageHandler.error("No valid Airhorn sound drive found.")
    mod_MessageHandler.error("Please initiate an Airhorn U.S.B. drive on your computer using the Airhorn Sound Manager utility.")
    quit()

# Load up all the ambient sounds and spin them up, each on its own thread.
LoadAmbientSounds()

# Default switch sounds to On
FileUtils.SetConfigValue("general", "switchsound", "on")

# Let the user know that we are up and ready for action
mod_playwav.play(FileUtils.GetConfigValue("audio_ports", "1"), 'SystemSounds/gnarly.wav', 70, 0)
#mod_MessageHandler.message("Airhorn audio environment controller is ready.")

# Read the config to determine where we are getting our commands from
if FileUtils.GetConfigValue("general", "consoleinput") == "on":
    while True:
        console_input = raw_input('Enter a switch number to play, n to listen to the network, or q to quit:  ')
        if console_input == 'q' or console_input == 'Q':
            # turn off ambient sound processing.
            FileUtils.SetConfigValue("general", "ambientsound", "off")
            mod_MessageHandler.message("Ta Tah for now.")
            quit()
        #elif console_input == 'n' or console_input == 'N':
        else:
            ### Process switch numbers from console input.
            if 'sys' in console_input:
                x=1
                #wavplayer_pyglet.play('/home/mcalder/PycharmProjects/AirhornPlayer/SystemSounds/needinfo.wav', 1, 1, 0)
            else:
                ProcessSwitch(console_input)
else:
    #Accept TCP socket AND console input until the letter q is entered.
    # Fire up the UDP Server
    port = FileUtils.GetConfigValue("network", "udpport")
    mod_MessageHandler.message("Now listening to UDP port " + port + " for input.  Console input is disabled.")
    serv = UDPServer(('', int(port)), UDPMessageHandler)
    serv.serve_forever()