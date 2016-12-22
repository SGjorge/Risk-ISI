import sys
sys.path.append("../")
sys.path.append("../Classes/Round")

from CoreVariables import CoreVariables
from Countries import Country
import unittest

class BoardTest(unittest.TestCase):

    #comprueba que haya 42 paises
    def test_thereare42countries (self):
        expected = 42
        self.assertEqual(expected, CoreVariables().maxCountries)

    def test_namecountry (self):
        expected = None
        self.assertEqual(expected, Country().name)

    def test_namevalid (self):
        expected = True
        self.assertEqual(expected, Country().nameok("Europa del norte"))
    def test_battalion (self):
        expected = 0
        self.assertEqual(expected, Country().countbattalion())


if __name__ == '__main__':
    unittest.main()
