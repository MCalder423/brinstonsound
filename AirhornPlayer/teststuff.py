__author__ = 'mcalder'
import mod_playwav
import FileUtils

# Test the TexToSpeech module
#import TextToSpeech
#TextToSpeech.SayThis('Piper down! We have a piper down over here!  No, it\'s okay, he\'s just pissed.')

# Here's a cheaty way to do multi-threading.  USe a seperate subprocess for each thread using this code
# Got it from here: http://www.raspberrypi.org/phpBB3/viewtopic.php?t=23044&p=216151
# import subprocess
#
# def say(something, language='en', voice='f2'):
#     subprocess.call(['espeak', '-v%s+%s' % (language, voice), something])

# import FileUtils
# airhornDrive = FileUtils.FindAirhornSoundDrive()
# print airhornDrive

#mod_playwav.play('sysdefault:CARD=DAC', '/media/marc/18FB-46B0/switch/1/Yard_Diesel_Fueling_Sequence.wav', 100,0)

card = FileUtils.GetConfigValue("audio_ports", "1")
print 'X' + card + 'X'
assert card == 'sysdefault:CARD=DAC'
print 'Card = ' + card
mod_playwav.play(card, '/mnt/sdc1/switch/1/Engine_Bell_A.wav', 100, 0)

