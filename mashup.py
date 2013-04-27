import mta
import wav

def make_mashup():
	"""Uses musical qualities determined by the Music module to combine motifs
	from the various songs provided in an audibly pleasing way.
	"""
	ts = [1,2,3,4,5]
	return mta.get_motifs(ts)

make_mashup()