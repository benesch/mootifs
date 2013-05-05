from collections import deque
import numpy as np
from scipy import fftpack
import sys
import wav


def get_bpm(chan1):
	""" calculates the bpm of a given song using the algorithm found here:
	http://archive.gamedev.net/archive/reference/programming/
	features/beatdetection/"""

	constant1, constant2 = -0.0025714, 1.5142857
	inst_energy_buffer, count = deque([], 43), 0
	beat_start = []

	def _compute_instant_energy(chan1):
		inst_energy = 0
		for idx, (data1, data2) in enumerate(chan1):
			if idx < 1024:
				inst_energy += (data1)**2 + (data2)**2
			else:
				return inst_energy

	def _compute_average_energy(inst_energy_buffer):
		return sum(inst_energy_buffer) / len(inst_energy_buffer)

	while chan1.size > 1024:
		inst_energy_buffer.append(_compute_instant_energy(chan1))
		chan1 = chan1[1024:]
		avg_energy = _compute_average_energy(inst_energy_buffer)
		count+= 1
		if len(inst_energy_buffer) > 21:
			print 1.3 * avg_energy, inst_energy_buffer[21]
			if inst_energy_buffer[21] > 1.3 * avg_energy:
				beat_start.append(count)
				print count	
	return len(beat_start)

def extract_instrumentals(time_series):
	"""Attempts to remove vocals by subtracting the channels

	Arguments:
		time_series -- the numpy array of samples. Must be stereo (two channel).

	Relies on vocals being mixed equally between channels. Returns an array of
	the same shape, but the channels will be duplicates of one another.
	"""
	if time_series.ndim != 2 or time_series.shape[1] != 2:
		raise MusicError('must be stereo time_series')

	chan1, chan2 = np.hsplit(time_series, 2)
	extracted = (chan1 - chan2) // 2
	return np.hstack((extracted, np.copy(extracted)))

def transpose_key(num_semitones):
	""" transposes the key of a song by the inputted semitones using
	a fourier transform with phase shift """
	w = wav.Wav("tune0.wav")
	chan1 = w.time_series()
	chan2 = np.copy(chan1)
	count = 0
	while chan1.size > 1024:
		count += 1024
		temp = fftpack.fft(chan1[0][:1024]), fftpack.fft(chan1[1][:1024])
		(end_data1, end_data2) = 2**(num_semitones/12))
		chan1 = chan1[512:]
		chan2[count] = [(fftpack.ifft(end_data1), fftpack.ifft(end_data2))]
	return chan2

def test_extract_instrumentals():
	w = wav.Wav("sail.wav")
	chan1 = w.time_series()
	extract_instrumentals(chan1)

def test_bpm():
	w = wav.Wav("sail.wav")
	chan1 = w.time_series()
	get_bpm(chan1)

class MusicError(Exception):
	pass