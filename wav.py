class Wav:
	"""Reads in wave files and stores them in a Wav class optimized for use with
	our music characteristic identification module (see next)."""

	def extract_time_series(self, filename):
		"""Converts a waveform into time series data - that is, a list of
		amplitudes as floats at a regular time interval (might be passed in as a
		parameter for added functionality, to determine the specificity of the
		MTA)."""
		pass