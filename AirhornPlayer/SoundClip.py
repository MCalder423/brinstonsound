__author__ = 'mcalder'
import os.path
from lxml import etree
import mod_MessageHandler

class SoundClip:
    def Load(self, airhornDrive, clipType, clipNumber):
        if int(clipNumber) < 1 or int(clipNumber) > 16:
            mod_MessageHandler.message("Invalid clip number " + clipNumber + ".  Must be a number between 1 and 16.")
            return

        if clipType == 'A':
            ctPath = '/ambient/'
        elif clipType == 'S':
            ctPath = '/switch/'
        else:
            mod_MessageHandler.message("Invalid clip type " + clipType + ". Must be S or A.")
            return

        conf = airhornDrive + ctPath + clipNumber + '/sound.conf'
        if not os.path.exists(conf):
            # print "Could not find sound config file " + conf
            return

        #print "Found the config file"
        doc = etree.parse(conf)
        self.switchNumber = doc.find('//switchNumber').text
        self.fileSpec = airhornDrive + ctPath + clipNumber + '/' + doc.find('//fileName').text
        self.audioPort = doc.find('//audioPort').text
        self.volume = doc.find('//volume').text
        if self.volume != "":
                self.volume = int(self.volume)
        self.balance = doc.find('//balance').text
        if self.balance != "":
                self.balance = int(self.balance)
        self.minInterval = doc.find('//minInterval').text
        if self.minInterval != "":
                self.minInterval = int(self.minInterval)
        self.maxInterval = doc.find('//maxInterval').text
        if self.maxInterval != "":
                self.maxInterval = int(self.maxInterval)

        #print self.switchNumber, self.fileSpec
        return

    switchNumber = ""
    fileSpec = ""
    audioPort = 1
    volume = 1
    balance = 0
    minInterval = 0
    maxInterval = 0