import mta
import numpy
import struct
import utils
import wav
import wave

def make_mashup():
	"""Uses musical qualities determined by the Music module to combine motifs
	from the various songs provided in an audibly pleasing way.
	"""

	# w = wav.Wav("tune0.wav", skip_frames=200)

	# ts = w.extract_time_series()
	# ts = [1,200,3,1,200,3,1,200,3,1,200,3,121,232,5555,121,232,5555]
	ts = [25.56,26,53.26,25.85,25.87,26.03,25.65,25.08,24.97,25.18,23.98,23.63,21.33,20.61,20.25,19.93,19.45,20.87,19.45,19.61,19.58,18.95,17.42,15.58,16.28,16.6,17.7,16.78,16.28,15.74,16.43,16.03,14.7,15.08,14.13,13.63,14.68,14.68,14.62,14.05,13.23,11.98,11.98,12.03,13.13,12.24,12.94,13.23,14.05,12.6,12.55,13.28,14.03,13.25,12.75,13.95,12.2,12.43,12.03,11.35,10.25,11.13,11.35,11.7,12.75,14.39,12.83,13,13.45,13.63,12.94,12.72,11.5,11.75,11.88,12.48,13.13,13.7,13.65,14.23,13.34,13.63,13.38,13.8,14.65,14.32,14.43,15.13,15.7,15.83,15.75,15.65,15.53,15.68,16.08,17.13,16.18,15.53,16.04,16.95,15.1,14.65,14.5,14.3,13.8,13.35,13.15,13.21,12.73,12.61,12.38,13.52,13.69,13.83,13.65,13.65,13.62,13.73,14.44,14.05,13.98,13.23,13.14,13.38,12.8,12.39,12.04,11.7,11.18,11.19,11,11.13,11.13,11.23,11.85,12.68,12.3,12.8,13.07,10.88,10.83,10.95,10.83,11.09,11.63,11.73,11.23,11.56,14,14.35,14.8,15.18,14.83,14.92,15.5,15.28,15.43,15.83,15.58,14.98,15.23,15.23,15.48,15.48,15.78,15.83,15.83,15.93,16.43,16.03,16.18,15.63,15.63,15,14.9,15.05,15.06,14.31,13.8,14.03,14.55,14.47,13.94,14.3,14.55,14.28,14.43,14.93,14.7,15.23,15.38,14.86,14.83,15.6,15.35,15.05,14.98,14.55,14.83,14.53,14.85,15.17,15.22,14.85,14.88,14.93,14.4,14.18,13.73,15.08,15.25,14.7,15.05,14.93,15.08,15.15,15.3,15.39,15.33,15.55,15.68,15.62,15.65,15.52,15.1,15.13,14.98,15.05,15,15,15.29,15.22,15.13,15.2,15.14,15.01,14.93,15.12,15.49,16.13,16.38,16.11,15.83,16.28,16.55,16.95,16.93,17.26,17.65,17.73,17.93,18.13,17.98,18.21,18.28,18.63,18.78,19,18.86,19.13,19.09,19.13,18.7,18.73,18.6,18.76,18.59,18.63,18.48,18.56,18.68,18.73,18.59,18.38,18.26,18.56,18.44,18.37,18.43,18.03,18.05,17.83,17.78,17.44,17.48,17.83,17.15,16.75,16.43,16.98,16.45,16.43,17.4,17.4,18,18.13,18.13,18.27,18.33,18.42,18.39,18.61,18.94,18.75,18.61,18.7,18.6,18.48,18.63,18.65,18.67,18.82,18.78,18.9,18.68,18.71,18.69,18.68,18.64,18.26,18.07,18.09,18.46,18.58,18.66,18.97,19.03,19.03,19.01,18.83,18.73,18.66,18.76,18.84,18.93,19.18,19.22,19.08,19.28,19.43,19.37,19.39,19.56,19.84,19.91,19.97,19.75,19.95,19.68,19.35,19.38,19.28,19.36,19.55,19.7,19.87,19.75,19.79,19.94,19.84,19.83,19.85,19.93,20.07,20.27,20.41,20.5,20.65,20.49,19.95,20.13,20.15,20.34,20.38,20.22,20.47,20.61,20.61,20.92,20.76,20.94,21.32,21.34,21.38,21.65,22.23,22.44,22.44,22.23,21.75,21.73,21.23,20.58,20.5,21.35,21.49,21.47,21.43,22.21,21.82,21.37,21.17,21.01,20.7,21.07,20.96,20.76,20.53,19.85,19.84,19.71,19.47,19.2,19.18,19.3,19.49,19.69,19.44,19.76,19.61,19.62,19.48,19.34,19.34,18.99,19.43,19.72,19.42,19.64,19.66,19.71,19.58,19.58,19.77,19.35,19.66,19.61,19.47,19.48,19.58,19.62,19.62,19.88,19.81,19.33,19.68,19.77,19.67,19.67,19.66,19.79,19.77,20.23,19.79,19.79,19.93,20.19,20.18,20,20.15,20.1,19.93,19.96,19.64,19.39,19.09,19.02,18.73,18.66,18.98,18.92,18.93,18.89,18.69,18.28,18.62,18.55,18.87,19.31,18.73,18.63,18.63,18.52,18.44,18.59,18.87,18.68,18.3,18.06,18.53,18.51,18.31,17.47,16.75,15.97,15.97,15.57,15.12,16.6,16.64,16.54,16.46,16.95,16.97,16.74,17.77,17.89,17.73,17.3,17.33,16.63,16.76,16.56,17.1,16.92,17.28,17.3,17.2,17.21,16.99,17.11,16.96,16.64,16.94,16.97,16.83,16.92,17.12,17.17,17.34,17.7,17.38,17.12,17.17,16.84,16.84,16.8,16.62,16.5,16.73,16.64,16.8,16.58,15.86,15.77,15.98,15.57,15.69,15.35,15.63,15.35,15.58,15.52,16.04,16.2,15.57,15.81,16.03,16.39,16.61,16.52,16.02,16.58,16.73,17.07,17.05,17.08,17.06,17.09,16.99,16.72,16.8,17.05,16.87,17.87,18.06,18.12,18.4,18.32,18.5,17.92,17.93,18.34,18.13,18.36,18.54,18.32,17.91,18.1,17.12,17.3,17.23,17.41,17.63,17.56,17.5,17.48,17.49,17.53,17.7,17.72,17.39,17.43,17.41,17.01,17.04,17.39,17.54,17.45,17.45,17.54,17.6,17.67,17.51,17.28,17.32,17.35,17.09,16.7,16.43,16.85,16.56,16.62,16.43,16.02,15.82,16.03,15.86,16.03,15.86,16.01,15.37,15.2,14.92,15.11,15.44,15.83,15.42,14.56,14.61,14.35,14.84,14.85,15.84,15.16,15.76,16.28,16.27,16.09,15.99,16.18,16.08,16.37,16.07,15.57,15.2,15.12,15.31,15.84,15.56,15.65,15.75,15.54,15.59,15.51,15.46,15.59,15.77,15.75,15.71,15.55,15.33,15.35,15.24,15.39,15.19,15.05,14.79,14.79,14.25,14.29,14.51,14.14,14.48,14.55,15.38,14.86,14.5,14.72,15.08,15.19,15.25,14.26,14.16,14.22,14.07,13.91,13.33,13.03,13.03,12.58,12.62,12.99,13.59,13.63,14.02,14.26,14.9,15.16,14.63,15.33,14.44,14.22,12.94,13.36,13.45,13.67,13.79,13.54,13.52,13.78,13.89,14.04,14.08,13.7,13.88,13.99,13.99,14.25,14.03,13.68,13.3,13.47,13.73,14.78,14.11,14.11,15.43,14.93,15,15.42,15.63,15.69,15.36,15.51,15.8,15.48,15.9,16.08,15.93,16.33,16.39,16.81,16.24,17.68,17.27,17.36,16.63,16.98,17.03,16.81,17.12,17.38,16.99,17.45,17.56,17.74,17.8,18.16,18.11,18.49,18.88,19.03,19.2,19.28,18.85,17.66,17.96,18.23,17.68,17.74,17.32,17,17.5,17.72,17.51,17.38,17.55,17.49,17.42,17.11,17.61,17.6,18.23,18.35,18.6,18.6,18.64,18.5,18.49,18.06,18.16,18.21,18.3,18.68,18.67,18.73,18.12,18.57,18.53,18.53,19.05,19.47,19.84,19.86,20.34,19.53,20.08,20.21,20.16,20.55,19.93,20.2,21.03,20.27,20.03,20.59,20.07,19.85,20.03,20.65,20.56,20.66,20.26,20.68,21.23,21.74,22.66,24.62,23.38,20.64,21.32,21.2,20.83,20.38,20.66,19.73,20.13,20.57,20.08,19.41,19.54,19.56,20.13,20.12,20.53,20.58,20.15,20.25,20.58,20.92,21.77,19.68,19.46,19.55,19.55,19.96,19.93,19.83,20.18,20.5,20.38,19.7,19.94,19.87,19.3,19.5,20.37,20.56,19.98,20.88,19.88,19.74,19.53,19.71,20.28,20.38,20.04,20.27,20.29,20.55,20.29,20.98,20.35,20.78,20.38,20.75,20.2,20.42,20.36,20.49,20.21,19.83,19.92,19.86,18.76,18.52,18.32,18.15,17.96,18.33,17.91,18.28,18.18,18.05,17.91,18.06,18.23,18.58,18.46,18.6,18.78,18.99,18.67,18.82,19.1,19.01,19.15,19.02,18.53,18.69,18.59,18.85,18.83,18.88,18.88,19.08,19.41,19.4,19.77,19.77,19.68,19.87,19.73,19.96,19.87,19.68,19.68,19.69,19.21,19.49,19.62,19.61,19.99,20.15,19.99,20.15,20.17,19.95,19.89,20.04,20.21,20.18,20.49,20.91,20.64,20.68,20.58,20.37,20.04,19.67,19.7,19.6,19.48,19.79,19.74,19.88,20.09,20.01,20.23,20.06,19.97,19.97,19.62,19.84,19.62,19.58,19.69,19.88,19.93,20.13,20.52,19.8,19.8,19.84,19.65,19.33,19.4,19.87,20.26,20.24,20.22,20.46,20.45,20.41,20.69,20.8,20.75,20.67,21.13,22.2,22.17,21.58,21.53,21.31,21.91,21.78,21.6,21.84,22.88]
	# ts = [0,1,3,6,10,15,21,28,36,45,55,0,1,3,6,10,15,21,28,36,45,55,0,1,3,6,10,15,21,28,36,45,55,0,1,3,6,10,15,21,28,36,45,55]
	#ts = [0,1,3,6,10,15,21,28,36,45,55,0,1,3,6,10,15,21,28,36,45,55]

	return mta.get_motifs(ts)

def construct(wavs, segments):
	total_duration = max(end for idx, start, end, offset in segments)

	if not utils.same(wav.nchannels for wav in wavs):
		raise MashupError('wav files have different numbers of channels')
	nchannels = wavs[0].nchannels

	sample_rates = [wav.sample_rate for wav in wavs]
	if not utils.same(sample_rates):
		sample_rate = max(sample_rates)
		wavs = [wav.resample(max_rate) for wav in wavs]
	else:
		wavs = [wav.time_series for wav in wavs]

	shape = (total_duration, nchannels)
	samples = numpy.zeros(shape, dtype=numpy.int64)
	ntracks = numpy.zeros(shape, dtype=numpy.int64)
	for (idx, start, end, offset) in segments:
		segment_duration = end - start
		wav_duration = wavs[idx].shape[0]

		if start > end:
			raise MashupError('segment start index must be less than end index')
		if offset > wav_duration or (offset + segment_duration) > wav_duration:
			raise MashupError('segment index out of range')

		samples[start:end] += wavs[idx][offset:offset+segment_duration]
		ntracks[start:end] += 1
	ntracks[ntracks == 0] = 1
	return (samples // ntracks).astype(numpy.int16)

def test():
	wav1 = wav.Wav('songs/for the first time.wav')
	wav2 = wav.Wav('songs/i knew you were trouble.wav')
	wav3 = wav.Wav('songs/all i need.wav')
	wavs = [wav1, wav2, wav3]

	SEC = 44100

	segments = [
		(0, 2 * SEC, 25 * SEC, 17 * SEC),
		(1, 7 * SEC, 25 * SEC, 1 * SEC),
		(2, 19 * SEC, 25 * SEC, 33 * SEC)
	]
	wav.write('out.wav', construct(wavs, segments), SEC)

class MashupError(Exception):
	pass

if __name__ == '__main__':
	test()