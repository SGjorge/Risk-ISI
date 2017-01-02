#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../")
sys.path.append("../Classes/Round")

from CoreVariables import CoreVariables
from Countries import Countries, Country, Neighbours, World
import unittest

class BoardTest(unittest.TestCase):

    #comprueba que haya 42 paises
    def test_thereare42countries (self):
        expected = 42
        self.assertEqual(expected, CoreVariables().maxCountries)

    @unittest.skip("skip")
    def test_thereare42countries2 (self):
        expected = 42
        absolutes = CoreVariables()
        lenght = len(absolutes.countries)
        self.assertEqual(expected, lenght)

    # @unittest.skip("skip")
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

    def test_neighbourhood_2(self):
        neighbourAux = Neighbours('Europa del norte')
        expectedNeighbours = neighbourAux.getarray()
        self.assertEqual(expectedNeighbours, CoreVariables().getneighbours("Europa del norte"))

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

    def test_changecountry(self):
        expectedNew = "Blue"
        countryAux = Country("Islandia", "Red")
        countryAux.changeconqueror("Blue")
        self.assertEqual(expectedNew, countryAux.conqueror)

if __name__ == '__main__':
    unittest.main()
