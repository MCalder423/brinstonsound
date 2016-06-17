import wave
import alsaaudio

def play(filename):
	wavfile = wave.open(filename, 'r')
	output = alsaaudio.PCM(alsaaudio.PCM_PLAYBACK)
	output.setchannels(wavfile.getnchannels())
	output.setrate(wavfile.getframerate())
	output.setformat(alsaaudio.PCM_FORMAT_U16_LE)
#	output.setformat(alsaaudio.PCM_NORMAL)
	output.setperiodsize(320)
	counter = wavfile.getnframes() /320
	while counter != 0:
		counter -= 1
		output.write(wavfile.readframes(320))
	wavfile.close()
	
#player(sys.argv[1])
#player('SystemSounds/needinfo.wav')
