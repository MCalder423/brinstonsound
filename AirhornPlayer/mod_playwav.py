#!/usr/bin/env python

import sys
import wave
import getopt
import alsaaudio

def play(card, file, volume, balance):

    f = wave.open(file)
    device = alsaaudio.PCM(card=card)
#    device = alsaaudio.PCM(card='sysdefault:CARD=DAC')
    #sys.stdout.write('%d channels, %d sampling rate\n' % (f.getnchannels(), f.getframerate()))

    # Set attributes
    device.setchannels(f.getnchannels())
    device.setrate(f.getframerate())

    # Get the correct mixer object
    cardidx = 0
    for c in alsaaudio.cards():
        #print 'Comparing sysdefault:CARD=' + c + ' to ' + card
        if ('sysdefault:CARD=' + c) in card:
            break
        cardidx += 1
    mixer = alsaaudio.Mixer(control='PCM', id=0, cardindex=cardidx)


    # Set Balance
    # Balance parameter should be an integer -100 to 100
    # Positive value indicates a reduction in volume of the left channel
    # Negative value indicates a reduction in volume of the right channel
    #print mixer.getvolume()
    # Initialize volume on both channels to 100%
    mixer.setvolume(long(100))
    if balance < 0:
        mixer.setvolume(long(100 - (balance * -1)), 1)
    elif balance > 0:
        mixer.setvolume(long(100 - balance), 0)

    # Set Volume
    # Volume parameter is an integer 0 to 100
    chan = 0
    for vols in mixer.getvolume():
        #newvol = long((float(volume) / float(vols)) * 100)
        newvol = long(float(vols) * (float(volume) / 100))
        mixer.setvolume(newvol, chan)
        chan += 1
    #print mixer.getvolume()

    # 8bit is unsigned in wav files
    if f.getsampwidth() == 1:
        device.setformat(alsaaudio.PCM_FORMAT_U8)
    # Otherwise we assume signed data, little endian
    elif f.getsampwidth() == 2:
        device.setformat(alsaaudio.PCM_FORMAT_S16_LE)
    elif f.getsampwidth() == 3:
        device.setformat(alsaaudio.PCM_FORMAT_S24_LE)
    elif f.getsampwidth() == 4:
        device.setformat(alsaaudio.PCM_FORMAT_S32_LE)
    else:
        print 'sample width: ' + f.getsampwidth()
        raise ValueError('Unsupported format')

    device.setperiodsize(320)
    
    data = f.readframes(320)
    while data:
        # Read data from stdin
        device.write(data)
        data = f.readframes(320)

    f.close()