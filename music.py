import sys
from pyechonest import song
import wave

def get_tempo(artist, title):
	"""Gets the BPM from a audio waveform
	"""
    "gets the tempo for a song"
    results = song.search(artist=artist, title=title, results=1, buckets=['audio_summary'])
    if len(results) > 0:
        return results[0].audio_summary['tempo']
    else:
        return None
source: (https://github.com/echonest/pyechonest/blob/master/examples/tempo.py)

class Wav:

def get_bpm(wav):

	





def extract_instrumentals():
	chan_out = []
	w = wav.Wav("tune0.wav")
	chan1, chan2 = w.extract_time_series() #returns the 2 treams
	for data1, data2 in chan1, chan2
		chan_out.append((data1-data2)/2)
	return chan_out

# 	def test_output(self, filename):
# 		_, fmt = self.get_format()
# 		data = self.extract_time_series()
# 		data = map(lambda x: struct.pack(fmt, x), data)

# 		out = wave.open(filename, 'w')
# 		out.setparams(self.fp.getparams())
# 		out.setnchannels(1)
# 		out.writeframes(''.join(data))


# def get_key(wav):
# 	"""Gets the key of an audio waveform
# 	"""
# 	pass

# def extract_instrumentals(wav):
# 	"""Removes the vocals from an audio waveform and returns the instrumentals
# 	"""
# 	pass