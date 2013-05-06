import itertools
import mta
import music
import numpy
import random
import struct
import wav
import wave

SEC = 44100

def generate(wavlist):
	"""Generates basic mashup from list of waves

	Arguments:
		wavlist -- list of wav.Wav instances. Assumes at least one wav is
				   present and that 44100 Hz is an appropriate sample rate.

	Returns numpy array of mashed-up samples suitable for output
	"""
	base = music.extract_instrumentals(wavlist[0])
	base_segment = (0, 0, base.duration, 0, .7)

	motifs = []
	for i, w in enumerate(wavlist[1:]):
		print 'finding motifs for wave', i
		motif = mta.get_longest_motif(w.resample(100))
		motifs.append([w, motif])
	random.shuffle(motifs)

	segments = [base_segment]
	wavs = [base_wav.time_series]
	for i, (wav, (mstart, mend)) in enumerate(motifs):
		start = 
		end = start + (mend - mstart)
		offset = mstart

		segment = (i + 1, start, end, offset, 1)
		segments.append(segment)
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
