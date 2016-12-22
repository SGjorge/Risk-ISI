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

    def test_existepais(self):
        expectedName = None
        expectedBattalions = 0
        expectedVecinos = []
        paisAux = Country()
        self.assertEqual(expectedName, paisAux.name)
        self.assertEqual(expectedBattalions, paisAux.battalions)
        self.assertEqual(expectedVecinos, paisAux.vecinos)


if __name__ == '__main__':
    unittest.main()
