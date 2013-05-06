from collections import deque
import numpy as np
from scipy import fftpack
import sys
import wav
import math

constant = 1.3
beat_start_window = 1024
buffer_size = 43

def get_bpm(waveform):
	""" calculates the bpm of a given song using the algorithm found here:
	http://archive.gamedev.net/archive/reference/programming/
	features/beatdetection/"""
	time_series = waveform.time_series

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
		inst_energy = np.sum(chan1[:beat_start_window]**2 +
						chan2[:beat_start_window]**2)
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
			if inst_energy_buffer[22] > constant * avg_energy and
			(beat_start == [] or count - beat_start[-1] > redundancy_threshold):
				beat_start.append(count)
			inst_energy_buffer.pop()

	return len(beat_start) / 2

def extract_instrumentals(time_series):
	"""	Relies on vocals being mixed equally between channels. Returns an array of
	the same shape, but the channels will be duplicates of one another.

	Arguments:
		time_series -- the numpy array of samples. Must be stereo (two channel).
	"""
	if time_series.ndim != 2 or time_series.shape[1] != 2:
		raise MusicError('must be stereo time_series')

	chan1, chan2 = np.hsplit(time_series, 2)
	extracted = (chan1 - chan2) // 2
	return np.hstack((extracted, np.copy(extracted)))

class MusicError(Exception):
	pass
