from .. import mta
import math
import string
import numpy as np
import unittest
import itertools

class ConvertTimeSeriesTests(unittest.TestCase):
	def setUp(self):
		mta.symbol_list = map(chr, range(97, 103))

	def test_simple(self):
		ts = np.array([0, 1, 4, 9, 16, 25, 36])
		ts_diff = np.array([1, 3, 5, 7, 9, 11])
		ts_diff_mean = sum(ts_diff)/len(ts_diff)
		ts_diff_sig = 0
		for elt in ts_diff:
			ts_diff_sig += (elt - ts_diff_mean)**2 
		ts_diff_sig = math.sqrt(ts_diff_sig/(len(ts_diff)-1))
		ts_diff_norm = (ts_diff - ts_diff_mean)/ts_diff_sig

		diff, scores = mta._convert_time_series(ts)		

		self.assertTrue(np.all(diff == ts_diff_norm))
		print diff
		print scores


class GenerateSymbolMatrixTests(unittest.TestCase):
	def setUp(self):
		mta.symbol_list = map(chr, range(97, 105))
		mta.PAA_interval = 1

	def test_simple(self):
		ts = np.array([1, 1, 1, 1, 1, 1, 2])
		params = mta._convert_time_series(ts)
		symbol_matrix = mta._generate_symbol_matrix(*params)
		putative = np.array([['a', '0'], ['a', '1'], ['a', '2'], ['a', '3'], ['a', '4'], ['h', '5']], dtype='S8')
		self.assertTrue(np.all(symbol_matrix.flatten() == putative.flatten()))

	def test_complex(self):
		ts = np.array([0, 1, 3, 6, 10, 15, 21, 28, 36])
		params = mta._convert_time_series(ts)
		symbol_matrix = mta._generate_symbol_matrix(*params)
		nats = [i for i in np.arange(len(mta.symbol_list))]
		putative = np.array([mta.symbol_list, nats], dtype='S8').T
		self.assertTrue(np.all(symbol_matrix.flatten() == putative.flatten()))


# class GenerateSymbolStageMatrixTests(unittest.TestCase):

# class InitializeTrackerPopulationTests(unittest.TestCase):
# 	def setUp(self):
# 		mta.symbol_list = map(chr, range(97, 105))
		
# 	def test_simple(self):
# 		tracker_list = mta._initialize_tracker_population()
# 		self.assertEqual(map(lambda t: t.word, tracker_list),map(lambda s: [s],mta.symbol_list))
# 		self.assertEqual(map(lambda t: t.starts, tracker_list), [[]] * len(mta.symbol_list))


class MatchTrackersTests(unittest.TestCase):
	def setUp(self):
		mta.symbol_list = map(chr, range(97,103))
		mta.PAA_interval = 1

	def test_simple(self):
		ts = np.array([0, 1, 2, 4, 6, 9, 12, 16, 20, 25, 30, 36, 42])
		params = mta._convert_time_series(ts)
		symbol_matrix = mta._generate_symbol_matrix(*params)
		tracker_list = mta._initialize_tracker_population()
		tracker_list = mta._match_trackers(tracker_list, symbol_matrix)
		self.assertEqual([len(x.loc) for x in tracker_list], [2, 2, 2, 2, 2, 2])


class EliminateUnmatchedTrackersTests(unittest.TestCase):
	def setUp(self):
		mta.symbol_list = map(chr, range(97,103))
		mta.PAA_interval = 1
		
	def test_simple(self):
		ts = [0, 1, 2, 4, 6, 9, 13]
		diff, scores = mta._convert_time_series(ts)
		symbol_matrix = mta._generate_symbol_matrix(diff, scores)
		tracker_list = mta._initialize_tracker_population()
		tracker_list = mta._match_trackers(tracker_list, symbol_matrix)
		tracker_list = mta._eliminate_unmatched_trackers(tracker_list)
		self.assertEqual([len(x.loc) for x in tracker_list], [2, 2])


class MutateTrackersTests(unittest.TestCase):
	def setUp(self):
		mta.symbol_list = map(chr, range(97,105))

	def test_simple(self):
		mutation_template = mta._initialize_tracker_population()
		tracker_list = mta._mutate_trackers(mutation_template, mutation_template)
		permutations = list(sorted(itertools.product(map(lambda t: t.word, mutation_template), repeat=2)))
		mutated = []
		for perm in permutations:
			mutant = []
			for elt in perm:
				mutant += elt
			mutated.append(mutant)

		self.assertTrue(np.all(map(lambda t: t.word, tracker_list) == np.array(mutated)))

# class StreamlineMotifsTests(unittest.TestCase):
