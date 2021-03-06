#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../")
sys.path.append("../Classes/Round")

from CoreVariables import CoreVariables
from Countries import Countries, Country, Neighbours, World, Continent
from Players import Players
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
    def test_allcontinents (self):
        expected = 6
        absolutes = CoreVariables()
        lenght = len(absolutes.tableContinents)
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
        expectedNeighbours = ['Europa del sur', 'Europa occidental','Ucrania', 'Escandinavia', "Gran Bretaña"]
        self.assertEqual(expectedNeighbours, CoreVariables().neighboursEuropaNorte)

    #@unittest.skip("skip")
    def test_theyallhaveneighbourhood(self):
        expected = True
        absolutes = CoreVariables()
        lenght = len(absolutes.countries)
        for i in range(lenght):
            countryAux = Country(absolutes.countries[i], None)
            self.assertEqual(expected, countryAux.ithasneighbourhood())

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
        Aux = Players("Luis", 0, "red", [])
        Aux2 = Players("Pepe", 0, "red", [])
        countryAux = Country("Islandia", Aux)
        countryAux.changeconqueror(Aux2)
        expected = "Pepe"
        self.assertEqual(expected, countryAux.conqueror.getname())

    def test_createEuropa(self):
        expectedName = 'Europa'
        expectedColor = 'blue'
        expectedCountries = CoreVariables().getcontinent('Europa')
        continentAux = Continent('Europa')
        self.assertEqual(expectedName, continentAux.nameCont)
        self.assertEqual(expectedColor, continentAux.color)
        self.assertEqual(expectedCountries, continentAux.countries)

    def test_ithasneigh (self):
        absolutes = CoreVariables()
        playerAux = Players("Pepe",35,"orange",[])
        countryAux = Country("Islandia", playerAux)
        expected = absolutes.neighboursIsl
        self.assertEqual(expected, countryAux.neighbours.getarray())

if __name__ == '__main__':
    unittest.main()
