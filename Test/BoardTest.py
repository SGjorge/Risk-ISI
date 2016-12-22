import sys
sys.path.append("../")
sys.path.append("../Classes/Round")

from Absolutos import Absolutos
from Countries import Countries
import unittest

class BoardTest(unittest.TestCase):

    #comprueba que haya 42 paises
    def test_thereare42countries (self):
        expected = 42
        self.assertEqual(expected, Absolutos().maxCountries)

    def test_namecountry (self):
        expected = None
        self.assertEqual(expected, Countries().name)

    def test_namevalid (self):
        expected = True
        self.assertEqual(expected, Countries().nameok("Europa del norte"))

if __name__ == '__main__':
    unittest.main()
