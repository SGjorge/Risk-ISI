import sys
sys.path.append("../")

import Absolutos
import unittest

class BoardTest(unittest.TestCase):

    #comprueba que haya 42 paises
    def thereare42countries (self):
        expected = 42
        self.assertEqual(expected, Absolutos().maxCountries)

    def namecountry (self):
        expected = None
        self.assertEqual(expected, Countries().name)

if __name__ == '__main__':
    unittest.main()