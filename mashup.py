import mta
import wav

def make_mashup():
	"""Uses musical qualities determined by the Music module to combine motifs
	from the various songs provided in an audibly pleasing way.
	"""
	w = wav.Wav("tune0.wav")
	ts = w.extract_time_series()
	m = mta.get_motifs(ts)