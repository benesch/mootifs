from collections import deque
import numpy as np
from scipy import fftpack
import sys
import wav


def get_bpm(time_series):
	""" calculates the bpm of a given song using the algorithm found here:
	http://archive.gamedev.net/archive/reference/programming/
	features/beatdetection/"""

	inst_energy_buffer, count = deque([], 43), 0
	beat_start = []

	def _compute_instant_energy(time_series):
		inst_energy = 0
		chan1, chan2 = np.hsplit(time_series, 2)
		inst_energy = chan1[:1024]**2 + chan2[:1024]**2

	def _compute_average_energy(inst_energy_buffer):
		return sum(inst_energy_buffer) / len(inst_energy_buffer)

	while time_series.shape[0] > 1024:
		inst_energy_buffer.append(_compute_instant_energy(time_series))
		time_series = time_series[1024:]
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

def transpose_key(shift, time_series):
	""" transposes the key of a song by the inputted semitones using
	a fourier transform with phase shift """
	chan1, chan2 = np.hsplit(time_series, 2)
	chan1_out, chan2_out = np.zeros_like(chan1), np.zeros_like(chan2)
	for i in range(512, chan1.shape[0] - 512, 512):
		shift1, shift2 = fftpack.rfft(chan1[i:i+1024]), fftpack.rfft(chan2[i:i+1024])
		shift1[200:] = 0
		shift2[200:] = 0
		chan1_out[i:i+1024] = fftpack.irfft(shift1)
		chan2_out[i:i+1024] = fftpack.irfft(shift2)
	return np.hstack((chan1_out, chan2_out)).astype(np.int16)

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
