__author__ = 'mcalder'
# http://www.pyglet.org/doc/programming_guide/sound_and_video.html

import pyglet

def play(filename, audioport, volume, balance):
    #music = pyglet.resource.media(filename)
    #music.play()
    source = pyglet.media.load(filename, streaming=False)
    player = pyglet.media.Player()
    player.queue(source)
    #player.volume = volume
    player.play()

    #pyglet.app.run()