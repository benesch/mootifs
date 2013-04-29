import sys
from pyechonest import song
import wave

def get_bpm(wav):

	sound_e_buffer = buffer()
	avg_energy = 0
	variance = 0
	beat_list = [] #just want the length of this list, so we can do length/time to get bpm
	C = 0
	w = wav.Wav("tune0.wav")
	chan1, chan2 = w.extract_time_series()
	for idx, data1, data2 in enumerate(zip(chan1,chan2)):
		if idx % 1024 == 0:
			sound_e_buffer_add_to_buffer(0)
		else:
			sound_e_buffer[-1] = sound_e_buffer[-1] + (data1)**2 + (data2)**2
		if idx % 44032 == 0:
			for i in range(43):
				avg_energy = avg_energy + (1/43) * (sound_e_buffer[i])**2			
			for i in sound_e_buffer:
				variance = variance + (sound_e_buffer[i]-avg_energy)**2
		constant = (-0.0025714*variance) + 1.5142857
			shift sound_e_buffer 1 index right to make room for new e value and flush oldest
			add new energy value in at E[0]
			if E[0] > constant*avg_energy:
				beat_list.append(0)
				avg_energy = 0
				variance = 0






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