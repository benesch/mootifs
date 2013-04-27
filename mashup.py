import mta
import wav

def make_mashup():
	"""Uses musical qualities determined by the Music module to combine motifs
	from the various songs provided in an audibly pleasing way.
	"""

	w = wav.Wav("Korg-DS-8-Rotary-Organ-C6.wav")
	ts = w.extract_time_series()
	#ts = [1,2,6,5,4,2,1,2,6,5,4,2,1,2]
	return mta.get_motifs(ts)