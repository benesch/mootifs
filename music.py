from collections import deque
import sys
import wave
import wav

def get_bpm(chan1):
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

	while len(chan1) > 1024:
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

def extract_instrumentals(chan1):
	chan_out = []
	for i, (data1, data2) in enumerate(chan1):
		chan_out.append((data1-data2)/2)
		print chan_out[i]
	return chan_out

def test_extract_instrumentals():
	w = wav.Wav("sail.wav")
	chan1 = w.extract_time_series()
	extract_instrumentals(chan1)

def test_bpm():
	w = wav.Wav("sail.wav")
	chan1 = w.extract_time_series()
	get_bpm(chan1)
