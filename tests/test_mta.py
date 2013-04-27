from .. import mta
import string
import unittest

class ConvertTimeSeriesTests(unittest.TestCase):
    def setUp(self):
        mta.symbol_list = string.ascii_lowercase[:20]

    def test_simple(self):
        list = [0, 1, 4, 9, 16, 25, 36]
        diff, scores = mta._convert_time_series(list)
        self.assertEqual(diff, [1, 3, 5, 7, 9, 11])
        print diff
        print scores