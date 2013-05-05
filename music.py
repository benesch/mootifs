from collections import deque
import numpy as np
from scipy import fftpack
import sys
import wav
import math


def get_bpm(time_series):
	""" calculates the bpm of a given song using the algorithm found here:
	http://archive.gamedev.net/archive/reference/programming/
	features/beatdetection/"""

	inst_energy_buffer, count = deque([], 43), 0
	beat_start = []
	repeat_list = deque([])
	redundancy_threshold = 3
	beat_start_window = 1024

	def _compute_instant_energy(time_series):
		inst_energy = 0

		# prevent int overflow with default dtype
		time_series_long = np.array(time_series, dtype='int64')

		chan1, chan2 = time_series_long.T
		inst_energy = np.sum(chan1[:beat_start_window]**2 + chan2[:beat_start_window]**2)
		return inst_energy

	def _compute_average_energy(inst_energy_buffer):
		return sum(inst_energy_buffer) / len(inst_energy_buffer)


	while time_series.shape[0] > beat_start_window:
		a = _compute_instant_energy(time_series)
		inst_energy_buffer.appendleft(a)
		avg_energy = _compute_average_energy(inst_energy_buffer)
		time_series = time_series[beat_start_window:]
		count += 1

		#print len(inst_energy_buffer)

		if len(inst_energy_buffer) == 43:
			#print 1.3 * avg_energy, inst_energy_buffer[22]
			if inst_energy_buffer[22] > 1.3 * avg_energy and (beat_start == [] or count - beat_start[-1] > redundancy_threshold):
				beat_start.append(count)
				print "haha"
			inst_energy_buffer.pop()
			print "woo"
		

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

def transpose_key(num_semitones, time_series):
	""" transposes the key of a song by the inputted semitones using
	a fourier transform with phase shift """

	if time_series.ndim != 2 or time_series.shape[1] != 2:
		raise MusicError('must be stereo time_series')

	chan1, chan2 = np.hsplit(time_series, 2)
	count = 0
	print "start"
	while chan1.shape[0] > beat_start_window:
		count += beat_start_window
		after_transform = fftpack.fft(chan1[:beat_start_window]), fftpack.fft(chan2[:beat_start_window])
		chan1phase_shift = chan1.dot(2**(num_semitones/12))
		chan2phase_shift = chan2.dot(2**(num_semitones/12))
		chan1, chan2 = chan1[beat_start_window/2:], chan2[beat_start_window/2:]
		chan1_new = fftpack.ifft(chan1phase_shift[:beat_start_window])
		chan2_new = fftpack.ifft(chan2phase_shift[:beat_start_window])

	return np.hstack((chan1_new, chan2_new))

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
