from .. import mta
import math
import string
import unittest
import itertools

class ConvertTimeSeriesTests(unittest.TestCase):
	def setUp(self):
		mta.symbol_list = map(chr, range(97, 105))

	def test_simple(self):
		ts = [0, 1, 4, 9, 16, 25, 36]
		ts_diff = [1, 3, 5, 7, 9, 11]
		ts_diff_mean = sum(ts_diff)/len(ts_diff)
		ts_diff_sig = 0
		for elt in ts_diff:
			ts_diff_sig += (elt - ts_diff_mean)**2 
		ts_diff_sig = math.sqrt(ts_diff_sig/(len(ts_diff)-1))
		ts_diff_norm = [(elt - ts_diff_mean)/ts_diff_sig for elt in ts_diff]

		diff, scores = mta._convert_time_series(ts)		

		self.assertEqual(diff, ts_diff_norm)
		print diff
		print scores


class GenerateSymbolMatrixTests(unittest.TestCase):
	def setUp(self):
		mta.symbol_list = map(chr, range(97, 105))
		mta.PAA_interval = 1

	def test_simple(self):
		ts = [1, 1, 1, 1, 1, 1, 2]
		diff, scores = mta._convert_time_series(ts)
		symbol_matrix = mta._generate_symbol_matrix(diff, scores)
		self.assertEqual(symbol_matrix, ['a', 'a', 'a', 'a', 'a', 'h'])

	def test_complex(self):
		ts = [0, 1, 3, 6, 10, 15, 21, 28, 36]
		diff, scores = mta._convert_time_series(ts)
		symbol_matrix = mta._generate_symbol_matrix(diff, scores)
		self.assertEqual(symbol_matrix, mta.symbol_list)


# class GenerateSymbolStageMatrixTests(unittest.TestCase):





class InitializeTrackerPopulationTests(unittest.TestCase):
	def setUp(self):
		mta.symbol_list = map(chr, range(97, 105))
		
	def test_simple(self):
		tracker_list = mta._initialize_tracker_population()
		self.assertEqual(map(lambda t: t.word, tracker_list),map(lambda s: [s],mta.symbol_list))
		self.assertEqual(map(lambda t: t.starts, tracker_list), [[]] * len(mta.symbol_list))


class MatchTrackersTests(unittest.TestCase):
	def setUp(self):
		mta.symbol_list = map(chr, range(97,103))
		mta.PAA_interval = 1

	def test_simple(self):
		ts = [0, 1, 2, 4, 6, 9, 12, 16, 20, 25, 30, 36, 42]
		diff, scores = mta._convert_time_series(ts)
		symbol_matrix = mta._generate_symbol_matrix(diff, scores)
		tracker_list = mta._initialize_tracker_population()
		tracker_list = mta._match_trackers(tracker_list, symbol_matrix)
		self.assertEqual([len(x.starts) for x in tracker_list], [2, 2, 2, 2, 2, 2])


# class EliminateUnmatchedTrackersTests(unittest.TestCase):
	# def setUp(self):
	# 	mta.symbol_list = map(chr, range(97,105))
	# 	mta.PAA_interval = 1
	# def test_simple(self):
	# 	ts = [0, 1, ]
# class VerifyGenuineMotifsTests(unittest.TestCase):

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

		self.assertEqual(map(lambda t: t.word, tracker_list), mutated)

# class StreamlineMotifsTests(unittest.TestCase):
