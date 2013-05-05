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
	return len(beat_start)

def extract_instrumentals(time_series):
	""" returns a song without its vocals by subtracting the channels """
	chan1, chan2 = np.hsplit(time_series, 2)
	extracted = (chan1 - chan2) // 2
	return np.hstack(extracted, np.copy(extracted))

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
