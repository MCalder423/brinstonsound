__author__ = 'marc'

import alsaaudio

idx = 0
for card in alsaaudio.cards():
    print card
    print alsaaudio.mixers(idx)
    idx += 1
