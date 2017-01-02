import sys
sys.path.append("../")
sys.path.append("../Classes/Round")

from CoreVariables import CoreVariables
from Countries import Country, Neighbours
import unittest

class BoardTest(unittest.TestCase):

    #comprueba que haya 42 paises
    def test_thereare42countries (self):
        expected = 42
        self.assertEqual(expected, CoreVariables().maxCountries)

    # @unittest.skip("skip")
    def test_namecountry (self):
        expected = None
        self.assertEqual(expected, Country(None).name)

    def test_namevalid (self):
        expected = True
        paisAux = Country('Europa del norte')
        self.assertEqual(expected, paisAux.nameok())

    def test_battalion (self):
        expected = 0
        self.assertEqual(expected, Country(None).countbattalion())

    def test_existepais(self):
        expectedName = None
        expectedBattalions = 0
        expectedNeighbours = []
        paisAux = Country(None)
        self.assertEqual(expectedName, paisAux.name)
        self.assertEqual(expectedBattalions, paisAux.battalions)
        neighbourAux = Neighbours(None)
        self.assertEqual(expectedNeighbours, neighbourAux.getarray())

    def test_neighbourhood_1(self):
        expectedNeighbours = ['Europa del sur', 'Europa occidental']
        self.assertEqual(expectedNeighbours, CoreVariables().neighboursEuropaNorte)

    def test_neighbourhood_2(self):
        neighbourAux = Neighbours('Europa del norte')
        expectedNeighbours = neighbourAux.getarray()
        self.assertEqual(expectedNeighbours, CoreVariables().getneighbours("Europa del norte"))

    def test_filledcountry (self):
        #están todas las cosas de un país (pais tonto)
        expectedName = None
        expectedBattalions = 0
        expectedNeighbours = []
        expectedConqueror = None
        paisAux = Country(None)
        self.assertEqual(expectedName, paisAux.name)
        self.assertEqual(expectedBattalions, paisAux.battalions)
        self.assertEqual(expectedConqueror, paisAux.conqueror)
        neighbourAux = Neighbours(None)
        self.assertEqual(expectedNeighbours, neighbourAux.getarray())

if __name__ == '__main__':
    unittest.main()
