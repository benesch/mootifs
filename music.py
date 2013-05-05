from collections import deque
import numpy as np
from scipy import fftpack
import sys
import wav
import math

constant1, constant2 = -0.0025714, 1.5142857
beat_start_window = 1024
buffer_size = 43

def get_bpm(time_series):
	""" calculates the bpm of a given song using the algorithm found here:
	http://archive.gamedev.net/archive/reference/programming/
	features/beatdetection/"""

	inst_energy_buffer, count = deque([], buffer_size), 0
	beat_start = []
	repeat_list = deque([])
	redundancy_threshold = 3

	def _compute_instant_energy(time_series):
		""" gets sum of energy contained in over 1024 parts
		in int64 to prevent overflow """
		time_series_long = np.array(time_series, dtype='int64')
		inst_energy = 0
		chan1, chan2 = time_series_long.T
		inst_energy = np.sum(chan1[:beat_start_window]**2 + chan2[:beat_start_window]**2)
		return inst_energy

	def _compute_average_energy(inst_energy_buffer):
		""" calculates local average energy around an inst_energy """
		return sum(inst_energy_buffer) / len(inst_energy_buffer)

	while time_series.shape[0] > beat_start_window:
		a = _compute_instant_energy(time_series)
		inst_energy_buffer.appendleft(a)
		avg_energy = _compute_average_energy(inst_energy_buffer)
		time_series = time_series[beat_start_window:]
		count += 1
		if len(inst_energy_buffer) == buffer_size:
			if inst_energy_buffer[22] > 1.3 * avg_energy and (beat_start == [] or count - beat_start[-1] > redundancy_threshold):
				print "beat found at " + count
				beat_start.append(count)
			inst_energy_buffer.pop()

	return len(beat_start) / 2

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
