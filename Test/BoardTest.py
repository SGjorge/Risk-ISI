import sys
sys.path.append("../")

import Absolutos
import unittest

class BoardTest(unittest.TestCase):

    def therearexcountries (self):
        expected = 42
        self.assertEqual(expected, Absolutos().maxcountries)
