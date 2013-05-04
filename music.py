import sys
import wave
import Queue

def get_bpm(wav):
constant1, constant2 = -0.0025714, 1.5142857
inst_energy_buffer, count = Queue.Queue(), 0
beats, beat_start = 0, []

	def _compute_instant_energy():
		inst_energy = 0
		for idx, data1, data2 in enumerate(zip(chan1,chan2)):
			if idx < 1024:
				inst_energy += (data1)**2 + (data2)**2
			else:
				chan1, chan2 = chan1[1024:], chan2[1024:]
				return inst_energy

	def _compute_average_energy(inst_energy_buffer):
		return sum(inst_energy_buffer) / len(inst_energy_buffer)

while len(chan1) > 1024:
	if len(inst_energy_buffer) > 43:
		avg_energy = _compute_average_energy(inst_energy_buffer)
		variance = 0
		variance += (inst_energy_buffer[i]-avg_energy)**2
		count++
		if (inst_energy_buffer[21] > (constant1*variance + constant2) * avg_energy):
			beats++
			beat_start.append[count]
			inst_energy_buffer.get()
			inst_energy_buffer.put(_compute_instant_energy())

def extract_instrumentals():
	chan_out = []
	w = wav.Wav("tune0.wav")
	chan1, chan2 = w.extract_time_series() #returns the 2 streams
	for data1, data2 in chan1, chan2
		chan_out.append((data1-data2)/2)
	return chan_out