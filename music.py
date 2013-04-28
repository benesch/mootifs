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
	





def extract_instrumentals (time_series):

# 	def get_format(self):
# 		bytes = self.fp.getsampwidth()
# 		fmts = { 1: 'B', 2: 'h', 4: 'i' }
# 		try:
# 			fmt = '<' + fmts[bytes]
# 		except ValueError:
# 			raise WavFormatError('unrecognized sample width')
# 		return (bytes, fmt)


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