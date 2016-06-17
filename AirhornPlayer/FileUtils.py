__author__ = 'mcalder'

import subprocess
import os
import ConfigParser

AirhornDrive = ''

def GetConfigValue(section, key):
    configParser = ConfigParser.RawConfigParser()
    configFilePath = r'airhorn.config'
    configParser.read(configFilePath)
    a_string = configParser.get(section, key)
    a_string.strip()
    assert isinstance(a_string, str)
    return a_string

def SetConfigValue(section, key, value):
    configParser = ConfigParser.ConfigParser()
    configFilePath = r'airhorn.config'
    configParser.read(configFilePath)
    configParser.set(section, key, value)
    with open(configFilePath, 'w') as configfile:
        configParser.write(configfile)
    return

def FindAirhornSoundDrive():

    mounts = {}

    for line in subprocess.check_output(['mount', '-l']).split('\n'):
        parts = line.split(' ')
        if len(parts) > 2:
            mounts[parts[2]] = parts[0]

    #print mounts
    for mountpoint in mounts:
        # if not "/media/" in mountpoint: continue
        # else:
            #print mountpoint
            # Found an externally mounted drive.  Check it for Airhorn sound folders
            for dir in os.listdir(mountpoint):
                if not "ambient" in dir:continue
                else:
                    #print mountpoint
                    AirhornDrive = mountpoint
                    return mountpoint
