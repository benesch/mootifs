from scipy import io
from scipy import signal
import struct
import wave

class Wav:
	"""Reads in wave files and stores them in a Wav class optimized for use with
	our music characteristic identification module.
	"""

	def __init__(self, filename):
		self.fp = wave.open(filename, 'r')
		self.time_series = None

	def read_frame(self):
		"""Allow for iteration"""
		return self.fp.readframes(1)

	def get_format(self):
		"""Returns a tuple (bytes, fmt) specifying wave file format

		bytes - the width of each channel's sample in bytes
		fmt - a struct-compatible format string specifying integer length
		"""
		nchannels = self.fp.getnchannels()
		bytes = self.fp.getsampwidth()
		fmts = { 1: 'B', 2: 'h', 4: 'i' }
		try:
			fmt = '<' + (fmts[bytes] * nchannels)
		except ValueError:
			raise WavFormatError('unrecognized sample width')
		return fmt

	def extract_time_series(self):
		"""Convert wave file into time series data.

		For simplicity, this function extracts data from only the first channel.
		Returns a list of integer amplitudes.
		"""
		if self.time_series is None:
			self.fp.rewind()
			fmt = self.get_format()
			it = iter(self.read_frame, b'')
			self.time_series = [struct.unpack(fmt, frame) for frame in it]

		return self.time_series

	def test_output(self, filename, time_series=None):
		"""Write time-series data back into wave file for corruption check"""
		if time_series is None:
			time_series = self.extract_time_series()

		fmt = self.get_format()
		data = [struct.pack(fmt, *x) for x in time_series]

		out = wave.open(filename, 'w')
		out.setparams(self.fp.getparams())
		out.writeframes(''.join(data))
		out.close()

class WavFormatError(Exception):
	pass