<<<<<<< HEAD
import string

import scipy as stats
import numpy as np

alphabet_size_a = 0 #global so we have access in other functions
match_threshold_r = 0
length_symbol_s = 0
alphabet_list = string.ascii_lowercase[:20]
paa_division = 5

def mean (lst) : return sum(lst) / len (lst)
def convert_times_series (time_series_data) (a) :
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
intervals = []
intervals = [(stats.scoreatpercentile(array_time_series, 100/len(alphabet_list)) for x in range(len(alphabet_list)))]



#intervals =
#letters = (stats.scoreatpercentile(array_time_series, 100/len(alphabet_list)) for x, letters in range(len(alphabet_list), alphabet_list)
#subsequences which are of length 1 to n.  subsequence is symbol string with w symbols






#Motifs in T consist of subsequences of lengths from 1 to n. A subsequence will be represented
#by a symbol string containing w symbols. By specifying the length of a symbol s, we can reduce
#the subsequence from size n to size w, where w=n/s.
#This simplification is achieved by a Piecewise Aggregate Approximation (PAA)[9] .
#The n consecutive data points representing the motif are divided into w equal sized frames where
#w = n/s. The mean value of the data within each frame is calculated and represents the PAA
#of that frame. The motif now consists of a sequence of w averages corresponding to each frame.
#These averages are converted into the symbol alphabet as part of the second stage of the SAX.

#find min and max.  then divide the area between that into 20 blocks and take the average every
#five data points and assign a letter value to them in that list.
#The parameters required in the MTA include the length of a symbol s,
#the match threshold r, and the alphabet size a.

l = [1,2,3]
#l[:-1]     everything up until the -1th element (not the last one)
#l[1:]      everything after the index 1th element



def initialize_tracker_pop

=======
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
	pass

def _generate_symbol_matrix(interval):
	"""Use a sliding window of specified length to calculate all possible
	symbolic representations of the data (since motifs clearly do not have
	to start at any specified point), and store these in a list to later
	initialize our trackers."""
	pass

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

def _mutate_trackers(trackers, mutations):
	"""The tracker list from the first generation represents all possible
	symbols in the data set; we use this as a template for further mutation of
	our trackers. Each parent tracker gives birth to trackers one symbol longer
	in length, with this symbol matching each of the possibilities in the
	mutation template. These new, longer trackers will then be used to find
	longer motifs."""
	pass

def _streamline_motifs(motifs):
	"""At the end of the MTA, we eliminate motifs that can be found within
	larger motifs to streamline the process. We might modify this step, however,
	since musical elements like the beat might be completely encapsulated within
	larger motifs, but we still want to be able to tease smaller motifs out."""
	pass
>>>>>>> 3be9f2d3e28274899cab2f36271fdbca5430e059
