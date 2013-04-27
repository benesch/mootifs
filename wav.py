import struct
import wave

class Wav:
	"""Reads in wave files and stores them in a Wav class optimized for use with
	our music characteristic identification module.
	"""

	def __init__(self, filename, skip_frames=0):
		self.fp = wave.open(filename, 'r')
		self.skip_frames = skip_frames

	def read_frame(self):
		"""Allow for iteration"""
		if self.skip_frames:
			self.fp.readframes(self.skip_frames)
		return self.fp.readframes(1)

	def get_format(self):
		"""Returns a tuple (bytes, fmt) specifying wave file format

		bytes - the width of each channel's sample in bytes
		fmt - a struct-compatible format string specifying integer length
		"""
		bytes = self.fp.getsampwidth()
		fmts = { 1: 'B', 2: 'h', 4: 'i' }
		try:
			fmt = '<' + fmts[bytes]
		except ValueError:
			raise WavFormatError('unrecognized sample width')
		return (bytes, fmt)

	def extract_time_series(self):
		"""Convert wave file into time series data.

		For simplicity, this function extracts data from only the first channel.
		Returns a list of integer amplitudes.
		"""
		bytes, fmt = self.get_format()

		self.fp.rewind()
		time_series = []
		for frame in iter(self.read_frame, b''):
			time_series.append(struct.unpack(fmt, frame[:bytes])[0])

		return time_series

	def test_output(self, filename, time_series=None):
		"""Write time-series data back into wave file for corruption check"""
		if time_series is None:
			time_series = self.extract_time_series()

		_, fmt = self.get_format()
		data = map(lambda x: struct.pack(fmt, x), time_series)

		out = wave.open(filename, 'w')
		out.setparams(self.fp.getparams())
		out.setnchannels(1)
		out.setframerate(self.fp.getframerate() / self.skip_frames)
		out.writeframes(''.join(data))
		out.close()


class WavFormatError(Exception):
	pass

if __name__ == '__main__':
	w = Wav('songs/i knew you were trouble.wav', skip_frames=32)
	w.test_output('songs/out.wav')