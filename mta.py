import string
from scipy import stats
import numpy as np
import sys

match_threshold = 2
symbol_list = map(chr, range(97, 105))
PAA_interval = 5

class tracker:
	def __init__(self, word):
		self.word = word
		self.loc = []

def mean (lst) : return sum(lst) / len (lst)

def get_motifs(time_series_data):
	"""Runs MTA on time-series data represented as a list of floats.
	Returns a list of segments-(start, end) tuples-identified as possible motifs.
	"""

	differential, zscores = _convert_time_series(time_series_data)
	symbol_matrix = _generate_symbol_matrix(differential, zscores)
	tracker_list = _initialize_tracker_population()
	mutation_template = tracker_list
	motif_list = []
	max_tracker_len = len(symbol_matrix)/match_threshold
	for i in range(max_tracker_len):
		symbol_matrix = _generate_symbol_stage_matrix(i + 1, symbol_matrix)
		#print len(symbol_matrix)
		tracker_list = _match_trackers(tracker_list, symbol_matrix)
		tracker_list = _eliminate_unmatched_trackers(tracker_list)
		motif_list += tracker_list
		tracker_list = _mutate_trackers(tracker_list, mutation_template)

	motif_list = _streamline_motifs(motif_list)

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
	paired = zip(time_series[:-1], time_series[1:])
	differential = [(latter - former) for former, latter in paired]
	diff_sig = stats.tstd(differential)
	diff_mean = stats.tmean(differential)
	norm_differential = [(diff - diff_mean)/diff_sig for diff in differential]
	ntrackers = len(symbol_list)
	percentiles = [round(x * (100. / ntrackers), 5) for x in range(ntrackers + 1)]
	zscores = [stats.scoreatpercentile(norm_differential, p) for p in percentiles]

	return norm_differential, zscores

def _generate_symbol_matrix(differential, zscores):
	"""Use a sliding window of specified length to calculate all possible
	symbolic representations of the data (since motifs clearly do not have
	to start at any specified point), and store these in a list to later
	initialize our trackers.  Should get passed in differenced data."""

	symbol_matrix = []

	for i in range(len(differential)):
		for idx, (score1, score2) in enumerate(zip(zscores[:-1], zscores[1:])):
			if i + PAA_interval <= len(differential) + 1:
				if score1 <= mean(differential[i:i+PAA_interval]) <= score2:
					symbol_matrix.append((symbol_list[idx], i))
					break

	return symbol_matrix


def _initialize_tracker_population():
	"""Initialize all unique trackers of single symbol length, and set their
	match counts to zero; these will be mutated and updated as they match motifs
	in the data set."""

	tracker_list = []
	for letter in symbol_list:
		tracker_list.append(tracker([letter]))
	return tracker_list


def _generate_symbol_stage_matrix(redundancy_threshold, symbol_matrix):
	"""To eliminate trivial matches (that is, consecutive sequences in the
	symbol matrix that are redundant, since using a sliding window necessarily
	results in overlap of the same motifs), this function generates a new symbol
	stage matrix each time the trackers are mutated, only including those
	symbols that are different than the one included before (to a certain error
	threshold, since long enough consecutive symbol repeats could match actual
	motifs)."""

	count = 0
	new_symbol_matrix = [symbol_matrix[0]]
	for i, s in enumerate(symbol_matrix[1:]):
		s_prev = new_symbol_matrix[-1]
		if s[0] == s_prev[0]:
			count += s[-1] - s_prev[-1]
			if count == redundancy_threshold:
				count = 0
			elif count > redundancy_threshold:
				new_symbol_matrix.append((s[0],s_prev[-1] + redundancy_threshold))
				count -= redundancy_threshold
		else:
			count = 0
			new_symbol_matrix.append(s)
	return new_symbol_matrix


def _match_trackers(tracker_list, symbol_matrix):
	"""Matches the symbols in each tracker to symbols within the symbol matrix;
	if a perfect match exists, the match count of the corresponding tracker is
	incremented by one."""

	for t in tracker_list:
		for i in range(len(symbol_matrix)):
			if i + len(t.word) <= len(symbol_matrix):
				print t.word
				print [tup[0] for tup in symbol_matrix[i:i+len(t.word)]]
				print "---------------"
				match_word = [tup[0] for tup in symbol_matrix[i:i+len(t.word)]]
				if t.word == match_word:
					t.loc.append({'start': symbol_matrix[i][-1],
								  'len': symbol_matrix[i+len(t.word)-1][-1] - symbol_matrix[i][-1] + 1})
	return tracker_list

def _eliminate_unmatched_trackers(tracker_list):
	"""Only those trackers who have a match count of at least two represent
	repeated motifs; as such, only those trackers should be mutated for future
	generations - this function eliminates all others."""

	matched_trackers = []
	for t in tracker_list:
		if len(t.loc) >= match_threshold:
			matched_trackers.append(t)
	return matched_trackers

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

	new_tracker_list = []
	for t in tracker_list:
		for char in mutation_template:
			new_tracker_list.append(tracker(t.word + char.word))
	return new_tracker_list



def _streamline_motifs(motif_list):
	"""At the end of the MTA, we eliminate motifs that can be found within
	larger motifs to streamline the process. We might modify this step, however,
	since musical elements like the beat might be completely encapsulated within
	larger motifs, but we still want to be able to tease smaller motifs out."""

	def remove_submotif(submotif, motif):
		for loc in motif.loc:
			for subloc in submotif.loc:
				if loc['start'] <= subloc['start'] and subloc['start'] + subloc['len'] <= loc['start'] + loc['len']:
					submotif.loc.remove(subloc)

		return motif

	for idx, submotif in enumerate(motif_list):
		for motif in motif_list[idx + 1:]:
			motif = remove_submotif(submotif, motif)

	return filter(lambda t: len(t.loc) >= match_threshold, motif_list)