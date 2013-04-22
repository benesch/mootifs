import string

import scipy as stats
import numpy as np

alphabet_size_a = 0 #global so we have access in other functions
match_threshold_r = 0
length_symbol_s = 0
symbol_list = string.ascii_lowercase[:20]

class tracker_class:
	#consists of a word and time start

def mean (lst) : return sum(lst) / len (lst)

def get_motifs(data, interval):
	"""Runs MTA on time-series data represented as a list of floats.
	Returns a list of segments-(start, end) tuples-identified as possible motifs.
	"""
	pass


def _convert_time_series (data, interval):
	"""Establishes symbolic library and normalizes the time series data, then
	represents the data (represented as a list of floats) with that library
	(i.e., each data point is converted into a symbol to be used in the
	symbolic matrix for motif discovery - allows us to compare similar data
	points by specifying a threshold range of values that each symbol
	represents). This function will average data points over intervals of
	specified length to determine the symbolic representations of those
	intervals.
	"""
	stdev, mean_difs, lst_len = 0, 0, len(Differences)

	# #Differencing
	# #Differences = [latter-former for former, latter in zip(time_series_data[:-1], time_series_data[1:])]
	# mean_difs = mean (lst)
	# 	for elt in Differences:
	# 		stdev = stdev + (elt - mean_difs)**2
	# 		stdev = sqrt(stdev / float(lst_len-1))
	# #Normalization
	# normalized = list ((x - mean) / stdev) for x in Differences)

	# #Symbolization
	# alphabet_size_a = a
	# min_norm, max_norm = min (normalized), max (normalized)
	# interval = (min_norm - max_norm) / alphabet_size_a
	# mean_norm = mean (normalized)

	intervals = [(stats.scoreatpercentile(array_time_series, 100/len(symbol_list)) for x in range(len(symbol_list)))]


def _generate_symbol_matrix(time_series_data, interval, percentile_list):
	"""Use a sliding window of specified length to calculate all possible
	symbolic representations of the data (since motifs clearly do not have
	to start at any specified point), and store these in a list to later
	initialize our trackers."""
	
	symbol_matrix = []

	for i in range(len(time_series_data)):
		for idx, score1, score2 in enumerate(zip(percentile_list[1:], percentile_list[-1])):
			if i + interval < len(time_series_data):
				if score1 < mean(time_series_data[i:i+interval]) < score2 :
					symbol_matrix.append(symbol_list[idx])


def initialize_tracker_population():
	"""Initialize all unique trackers of single symbol length, and set their
	match counts to zero; these will be mutated and updated as they match motifs
	in the data set."""
	pass

def _generate_symbol_stage_matrix(symbols, threshold):
	"""To eliminate trivial matches (that is, consecutive sequences in the
	symbol matrix that are redundant, since using a sliding window necessarily
	results in overlap of the same motifs), this function generates a new symbol
	stage matrix each time the trackers are mutated, only including those
	symbols that are different than the one included before (to a certain error
	threshold, since long enough consecutive symbol repeats could match actual
	motifs)."""
	pass


def _match_trackers(trackers, symbols):
	"""Matches the symbols in each tracker to symbols within the symbol matrix;
	if a perfect match exists, the match count of the corresponding tracker is
	incremented by one."""
	pass


def _eliminate_unmatched_trackers(trackers, threshold):
	"""Only those trackers who have a match count of at least two represent
	repeated motifs; as such, only those trackers should be mutated for future
	generations - this function eliminates all others."""
	pass


def _verify_genuine_motifs(trackers, threshold):
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

	for tracker in tracker_list:
		for char in mutation_template:
			tracker_list.append(tracker + char)
		tracker_list.remove(tracker)


def _streamline_motifs(motif_list):
	"""At the end of the MTA, we eliminate motifs that can be found within
	larger motifs to streamline the process. We might modify this step, however,
	since musical elements like the beat might be completely encapsulated within
	larger motifs, but we still want to be able to tease smaller motifs out."""


	motif_list = sorted(motif_list, key=lambda motif: len(motif.word))

	def remove_submotif(submotif, motif):

		for start in motif.starts:
			for substart in submotif.starts:
				if start <= substart and substart + len(submotif.word) <= motif.start + len(motif.word):
					submotif.starts.remove(substart)

	for idx, submotif in enumerate(motif_list):
		for motif in motif_list[idx + 1:]:
			remove_submotif(submotif, motif)

