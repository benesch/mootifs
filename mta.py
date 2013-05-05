import string
from scipy import stats
import numpy as np
import sys

match_threshold = 2
symbol_list = [map(chr, range(97, 105))]
num_symbols = len(symbol_list)
PAA_interval = 1

class tracker:
	def __init__(self, word):
		self.word = np.array(word)
		self.loc = np.array([],dtype='object')

def mean(lst): 
	return sum(lst) / len(lst)

def get_motifs(time_series):
	"""Runs MTA on time-series data represented as a list of floats.
	Returns a list of segments-(start, end) tuples-identified as possible motifs.
	"""

	params = _convert_time_series(time_series)
	symbol_matrix = _generate_symbol_matrix(*params)
	tracker_list = _initialize_tracker_population()
	mutation_template = tracker_list
	motif_list = np.array([], dtype='object')
	while len(tracker_list) > 0:
		# print len(symbol_matrix)
		# symbol_matrix = _generate_symbol_stage_matrix(len(tracker_list[0].word) + 1, symbol_matrix)
		tracker_list = _match_trackers(tracker_list, symbol_matrix)
		tracker_list = _eliminate_unmatched_trackers(tracker_list)
		motif_list = np.append(motif_list, tracker_list)
		tracker_list = _mutate_trackers(tracker_list, mutation_template)
	# motif_list = _streamline_motifs(motif_list)

	return motif_list


def _convert_time_series(time_series):
	"""Establishes symbolic library and normalizes the time series data, then
	represents the data (represented as a list of floats) with that library
	(i.e., each data point is converted into a symbol to be used in the
	symbolic matrix for motif discovery - allows us to compare similar data
	points by specifying a threshold range of values that each symbol
	represents). This function will average data points over intervals of
	specified length to determine the symbolic representations of those
	intervals.
	"""
	differential = np.subtract(time_series[1:], time_series[:-1])
	std_dev = np.std(differential)
	mean = np.mean(differential)
	norm_differential = (differential - mean) / std_dev
	
	percentiles = np.arange(num_symbols + 1) * (100. / num_symbols)
	zscores = np.array([stats.scoreatpercentile(norm_differential, p) for p in percentiles])

	return norm_differential, zscores

def _generate_symbol_matrix(differential, zscores):
	"""Use a sliding window of specified length to calculate all possible
	symbolic representations of the data (since motifs clearly do not have
	to start at any specified point), and store these in a list to later
	initialize our trackers.  Should get passed in differenced data."""

	symbol_matrix_len = len(differential) - PAA_interval + 1
	symbol_matrix = np.zeros(shape=(symbol_matrix_len, 2), dtype='S1')
	for i in np.arange(symbol_matrix_len):
		for idx in range(len(zscores) - 1):
			if i + PAA_interval <= len(differential):
				lower, upper = zscores[idx:idx+2] 
				if lower <= mean(differential[i:i+PAA_interval]) <= upper:
					symbol_matrix[i] = [symbol_list[idx], i]
	print symbol_matrix
	return symbol_matrix


def _initialize_tracker_population():
	"""Initialize all unique trackers of single symbol length, and set their
	match counts to zero; these will be mutated and updated as they match motifs
	in the data set."""

	tracker_list = np.empty(num_symbols, dtype='object')
	for i in np.arange(num_symbols):
		tracker_list[i] = tracker([symbol_list[i]])
	return tracker_list


def _generate_symbol_stage_matrix(redundancy_threshold, symbol_matrix):
	"""To eliminate trivial matches (that is, consecutive sequences in the
	symbol matrix that are redundant, since using a sliding window necessarily
	results in overlap of the same motifs), this function generates a new symbol
	stage matrix each time the trackers are mutated, only including those
	symbols that are different than the one included before (to a certain error
	threshold, since long enough consecutive symbol repeats could match actual
	motifs)."""

	symbol_matrix_len = len(symbol_matrix)
	count = 0
	new_symbol_matrix = np.zeros(shape=(symbol_matrix_len, 2), dtype='S1')
	new_symbol_matrix[0] = symbol_matrix[0]
	for i in np.arange(symbol_matrix_len - 1):
		s = symbol_matrix[i + 1]
		s_prev = new_symbol_matrix[i]
		if s[0] == s_prev[0]:
			count += int(s[-1]) - int(s_prev[-1])
			if count == redundancy_threshold:
				count = 0
			elif count > redundancy_threshold:
				new_symbol_matrix[i + 1] = [s[0], int(s_prev[-1]) + redundancy_threshold]
				count -= redundancy_threshold
		else:
			count = 0
			new_symbol_matrix[i + 1] = s

	return new_symbol_matrix[~np.all(new_symbol_matrix == '', axis=1)]


def _match_trackers(tracker_list, symbol_matrix):
	"""Matches the symbols in each tracker to symbols within the symbol matrix;
	if a perfect match exists, the match count of the corresponding tracker is
	incremented by one."""

	for t in tracker_list:
		for i in np.arange(len(symbol_matrix)):
			if i + len(t.word) <= len(symbol_matrix):
				print t.word
				print np.array([tup[0] for tup in symbol_matrix[i:i+len(t.word)]])
				print "---------------"
				match_word = symbol_matrix[i:i+len(t.word)].T[0]
				if np.all(t.word == match_word):
					t.loc = np.append(t.loc, {'start': int(symbol_matrix[i][-1]),
											  'len': int(symbol_matrix[i+len(t.word)-1][-1]) - int(symbol_matrix[i][-1]) + 1})
	return tracker_list

def _eliminate_unmatched_trackers(tracker_list):
	"""Only those trackers who have a match count of at least two represent
	repeated motifs; as such, only those trackers should be mutated for future
	generations - this function eliminates all others."""

	matched_trackers = np.zeros(len(tracker_list), dtype='object')
	for i in np.arange(len(tracker_list)):
		t = tracker_list[i]
		if len(t.loc) >= match_threshold:
			matched_trackers[i] = t
	return matched_trackers[matched_trackers != 0]

def _verify_genuine_motifs(tracker_list, deviation_threshold):
	"""Examines purported motif sequences and calculates the Euclidean distance
	between them; if that distance is greater than a given threshold (which
	dynamically increases based on the length of the motif involved), these
	motifs (and thus their corresponding trackers) are discarded. Those that are
	successful are stored in a motif list."""
	pass

	# may not be necessary in phase I of implementation


def _mutate_trackers(tracker_list, mutation_template):
	"""The tracker list from the first generation represents all possible
	symbols in the data set; we use this as a template for further mutation of
	our trackers. Each parent tracker gives birth to trackers one symbol longer
	in length, with this symbol matching each of the possibilities in the
	mutation template. These new, longer trackers will then be used to find
	longer motifs."""

	new_tracker_list = np.zeros(len(tracker_list) * len(mutation_template), dtype='object')
	for i in np.arange(len(tracker_list)):
		for j in np.arange(len(mutation_template)):
			# print np.append(tracker_list[i].word, mutation_template[j].word)
			new_tracker_list[i + j] = tracker(np.append(tracker_list[i].word, mutation_template[j].word))
	return np.trim_zeros(new_tracker_list)


def _streamline_motifs(motif_list):
	"""At the end of the MTA, we eliminate motifs that can be found within
	larger motifs to streamline the process. We might modify this step, however,
	since musical elements like the beat might be completely encapsulated within
	larger motifs, but we still want to be able to tease smaller motifs out."""

	def remove_submotif(submotif, motif):
		for loc in motif.loc:
			sublocs = submotif.loc
			submotif.loc = np.zeros(len(sublocs), dtype='object')
			for i in np.arange(len(sublocs)):
				if not (loc['start'] <= sublocs[i]['start'] and sublocs[i]['start'] + sublocs[i]['len'] <= loc['start'] + loc['len']):
					submotif.loc[i] = sublocs[i]				
			submotif.loc = submotif.loc[submotif.loc != 0]
		return motif

	for i in np.arange(len(motif_list)):
		for j in np.arange(len(motif_list)):
			if i != j:
				motif_list[j] = remove_submotif(motif_list[i], motif_list[j])

	return filter(lambda t: len(t.loc) >= match_threshold, motif_list)