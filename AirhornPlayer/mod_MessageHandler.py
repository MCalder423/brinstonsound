__author__ = 'marc'
import TextToSpeech as tts
import FileUtils


def message(msg):
    print(msg)
    speak = FileUtils.GetConfigValue("general", "messagesound")
    if speak == "on":
        tts.SayThis(msg)

def error(msg):
    print(msg)
    tts.SayThis(msg)
