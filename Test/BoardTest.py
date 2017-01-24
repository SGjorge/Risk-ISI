#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../")
sys.path.append("../Classes/Round")

from CoreVariables import CoreVariables
from Countries import Countries, Country, Neighbours, World, Continent
import unittest

class BoardTest(unittest.TestCase):

    # @unittest.skip("skip")
    #comprueba que haya 42 paises
    def test_thereare42countries (self):
        expected = 42
        self.assertEqual(expected, CoreVariables().maxCountries)

    def test_thereare42countries2 (self):
        expected = 42
        absolutes = CoreVariables()
        lenght = len(absolutes.countries)
        self.assertEqual(expected, lenght)

    def test_namecountry (self):
        expected = None
        self.assertEqual(expected, Country(None, None).name)

    def test_namevalid (self):
        expected = True
        paisAux = Country('Europa del norte', None)
        self.assertEqual(expected, paisAux.nameok())

    def test_battalion (self):
        expected = 0
        self.assertEqual(expected, Country(None, None).getbattalions())

    def test_existepais(self):
        expectedName = None
        expectedBattalions = 0
        expectedNeighbours = []
        paisAux = Country(None, None)
        self.assertEqual(expectedName, paisAux.name)
        self.assertEqual(expectedBattalions, paisAux.battalions)
        neighbourAux = Neighbours(None)
        self.assertEqual(expectedNeighbours, neighbourAux.getarray())

    def test_neighbourhood_1(self):
        expectedNeighbours = ['Europa del Sur', 'Europa occidental','Ucrania', 'Escandinavia', "Gran Bretaña"]
        self.assertEqual(expectedNeighbours, CoreVariables().neighboursEuropaNorte)

    #@unittest.skip("skip")
    def test_theyallhaveneighbourhood(self):
        expected = True
        absolutes = CoreVariables()
        lenght = len(absolutes.countries)
        for i in range(lenght):
            self.assertEqual(expected, Country(absolutes.countries[i], None).ithasneighbourhood(absolutes.countries[i]))

    def test_filledcountry (self):
        #estan todas las cosas de un pais (pais tonto)
        expectedName = None
        expectedBattalions = 0
        expectedNeighbours = []
        expectedConqueror = None
        paisAux = Country(None, None)
        self.assertEqual(expectedName, paisAux.name)
        self.assertEqual(expectedBattalions, paisAux.battalions)
        self.assertEqual(expectedConqueror, paisAux.conqueror)
        neighbourAux = Neighbours(None)
        self.assertEqual(expectedNeighbours, neighbourAux.getarray())

    def test_getplayer (self):
        expectedConqueror = None
        self.assertEqual(expectedConqueror, Country(None, None).getconqueror())

    def test_getbattalions (self):
        expectedBattalions = 0
        self.assertEqual(expectedBattalions, Country(None, None).getbattalions())

    def test_wholeworld (self):
        absolutes = CoreVariables()
        expectedWorld = World()
        lenght = len(expectedWorld.world)
        for i in range(0,lenght):
            #comparo cada nombre del array absoluto con los que he ido creando en countries
            self.assertEqual(absolutes.countries[i], expectedWorld.world[i].getname())

    def test_changeconqueror(self):
        expectedNew = "Blue"
        countryAux = Country("Islandia", "Red")
        countryAux.changeconqueror("Blue")
        self.assertEqual(expectedNew, countryAux.conqueror)

    def test_createEuropa(self):
        expectedName = 'Europa'
        expectedColor = 'blue'
        expectedCountries = CoreVariables().getcontinent('Europa')
        continentAux = Continent('Europa')
        self.assertEqual(expectedName, continentAux.nameCont)
        self.assertEqual(expectedColor, continentAux.color)
        self.assertEqual(expectedCountries, continentAux.countries)

if __name__ == '__main__':
    unittest.main()
