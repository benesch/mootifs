import struct
import wave
scipy.io.wavfile.read(somefile)
class Wav:
	"""Reads in wave files and stores them in a Wav class optimized for use with
	our music characteristic identification module (see next)."""

	def __init__(self, filename):
		self.fp = wave.open(filename, 'r')

	def read_frame(self):
		return self.fp.readframes(1)

	def get_format(self):
		bytes = self.fp.getsampwidth()
		fmts = { 1: 'B', 2: 'h', 4: 'i' }
		try:
			fmt = '<' + fmts[bytes]
		except ValueError:
			raise WavFormatError('unrecognized sample width')
		return (bytes, fmt)

	def extract_time_series(self):
		"""Converts a waveform into time series data - that is, a list of
		amplitudes as ints.

		For simplicity, this function extracts only the first channel.

		"""
		bytes, fmt = self.get_format()

		self.fp.rewind()
		time_series = []
		for frame in iter(self.read_frame, b''):
			time_series.append(struct.unpack(fmt, frame[:bytes])[0])

		return time_series

	def test_output(self, filename):
		_, fmt = self.get_format()
		data = self.extract_time_series()
		data = map(lambda x: struct.pack(fmt, x), data)

		out = wave.open(filename, 'w')
		out.setparams(self.fp.getparams())
		out.setnchannels(1)
		out.writeframes(''.join(data))


class WavFormatError(Exception):
	pass

if __name__ == '__main__':
	w = Wav('songs/i knew you were trouble.wav')
	w.test_output('songs/out.wav')