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

