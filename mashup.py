import mta
import music
import numpy
import random
import struct
import wav
import wave

SEC = 44100

def generate(wavlist):
	base_wav = wavlist[0]

	motifs = []
	for i, w in enumerate(wavlist[1:]):
		print 'finding motifs for wave', i
		motifs.append([w, mta.get_longest_motif(w.resample(100))])

	random.shuffle(motifs)
	segments = [(0, 2 * SEC, (2 + base_wav.duration) * SEC, 0, 1)]
	wavs = [base_wav.time_series]
	for i, m in enumerate(motifs):
		start = (i + 1) / (len(motifs) + 1) * wavlist[0].duration * SEC
		end = start + (m[1][-1] - m[1][0]) * SEC
		offset = m[1][0] * SEC
		segments.append((i + 1, start, end, offset, 0.8))
		wavs.append(w.time_series)

	return construct(wavs, segments)

def construct(wavs, segments):
	"""Constructs mashup from `wavs` specified by `segments`

	Arguments:
		wavs     -- a list of sample data arrays
		segments -- a list of tuples in the following format:
					(idx, start, end, offset, vol)
					idx:    index of wav file in `wavs`
					start:  starting frame in *output* file
					end:    ending frame in *output* file
					offset: frame to start including 
					volume: floating-point amplitude multiplier to adjust volume

	Returns numpy array of mixed samples suitable for output.
	"""
	total_duration = max(end for idx, start, end, offset, vol in segments)
	shape = (total_duration, 2)
	samples = numpy.zeros(shape, dtype=numpy.int64)
	ntracks = numpy.zeros(shape, dtype=numpy.int64)
	for (idx, start, end, offset, vol) in segments:
		segment_duration = end - start
		wav_duration = wavs[idx].shape[0]
		samples[start:end] += wavs[idx][offset:offset+segment_duration] * vol
		ntracks[start:end] += 1
	ntracks[ntracks == 0] = 1
	return (samples // ntracks).astype(numpy.int16)
