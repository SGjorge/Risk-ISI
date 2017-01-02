# -*- coding: utf-8 -*-

import sys
sys.path.append("../Classes/GameRules/")
from GameRules import GameRules
sys.path.append("../Classes/Round/")
from Countries import Countries, Country
import unittest

class GameRulesTest(unittest.TestCase):

    
        #Checks if the number of players is ok (3-6)
    def test_is1playerok(self):
        expected = False
        self.assertEqual(expected, GameRules.numberofplayersok(1))

    def test_are5playersok(self):
        expected = True
        self.assertEqual(expected, GameRules.numberofplayersok(5))

    def test_are7playersok(self):
        expected = False
        self.assertEqual(expected, GameRules.numberofplayersok(7))

        #Checks the number of initial battalions per player, based on the total number of players
    def test_initialbattalionsfor3players(self):
        expected = 35
        self.assertEqual(expected, GameRules.getinitialbattalions(3))

    def test_initialbattalionsfor4players(self):
        expected = 30
        self.assertEqual(expected, GameRules.getinitialbattalions(4))

    def test_initialbattalionsfor5players(self):
        expected = 25
        self.assertEqual(expected, GameRules.getinitialbattalions(5))

    def test_initialbattalionsfor6players(self):
        expected = 20
        self.assertEqual(expected, GameRules.getinitialbattalions(6))

        #Checks the number of extra battalions per each whole conquered continent 
    def test_battalionsperamericaN(self):
        expected = 5
        self.assertEqual(expected, GameRules.getbattalionspercontinent("América Norte")) 

    def test_battalionsperasia(self):
        expected = 7
        self.assertEqual(expected, GameRules.getbattalionspercontinent("Asia")) 

    def test_battalionsperamericaS(self):
        expected = 2
        self.assertEqual(expected, GameRules.getbattalionspercontinent("América Sur")) 

    def test_battalionspereuropa(self):
        expected = 5
        self.assertEqual(expected, GameRules.getbattalionspercontinent("Europa"))

    def test_battalionsperafrica(self):
        expected = 3
        self.assertEqual(expected, GameRules.getbattalionspercontinent("África")) 

    def test_battalionsperoceania(self):
        expected = 2
        self.assertEqual(expected, GameRules.getbattalionspercontinent("Oceanía"))

        #Checks the number of extra battalions per conquered contries
    def test_battalionsper12countries(self):
        expected = 4
        self.assertEqual(expected, GameRules.getbattalionspercountries(12)) 

    def test_battalionsper2countries(self):
        expected = 3
        self.assertEqual(expected, GameRules.getbattalionspercountries(2)) 

    def test_battalionsper37countries(self):
        expected = 12
        self.assertEqual(expected, GameRules.getbattalionspercountries(37)) 


        #Checks if the number of battalions is ok to attack
    def test_is1battaliontoattackok(self):
        country = Country("Islandia","red")
        country.changebattalions(25) #25 battalions
        expected = True
        self.assertEqual(expected, GameRules.battalionstoattackok(country,1))

    def test_are2battalionstoattackok(self):
        country = Country("Islandia","red")
        country.changebattalions(25) #25 battalions
        expected = True
        self.assertEqual(expected, GameRules.battalionstoattackok(country,2))

    def test_are3battalionstoattackok(self):
        country = Country("Islandia","red")
        country.changebattalions(25) #25 battalions
        expected = True
        self.assertEqual(expected, GameRules.battalionstoattackok(country,3))

    def test_are4battalionstoattackok(self):
        country = Country("Islandia","red")
        country.changebattalions(25) #25 battalions
        expected = False
        self.assertEqual(expected, GameRules.battalionstoattackok(country,4))

    def test_is1battalionoktoattack(self):
        country = Country("Islandia","red")
        country.changebattalions(2) #2 battalions
        expected = True
        self.assertEqual(expected, GameRules.battalionstoattackok(country,1))

    def test_are2battalionsoktoattack(self):
        country = Country("Islandia","red")
        country.changebattalions(2) #2 battalions
        expected = False
        self.assertEqual(expected, GameRules.battalionstoattackok(country,2))

        #Checks if the number of battalions is ok to defend
    def test_is1battaliontodefendok(self):
        country = Country("Groenlandia","blue")
        country.changebattalions(4) #4 battalions
        expected = True
        self.assertEqual(expected, GameRules.battalionstodefendok(country,1))

    def test_are2battalionstodefendok(self):
        country = Country("Groenlandia","blue")
        country.changebattalions(2) #2 battalions
        expected = True
        self.assertEqual(expected, GameRules.battalionstodefendok(country,2))

    def test_are3battalionstodefendok(self):
        country = Country("Groenlandia","blue")
        country.changebattalions(8) #8 battalions
        expected = False
        self.assertEqual(expected, GameRules.battalionstodefendok(country,3))

    def test_are2battalionsoktodefend(self):
        country = Country("Groenlandia","blue")
        country.changebattalions(1) #1 battalion
        expected = False
        self.assertEqual(expected, GameRules.battalionstodefendok(country,2))

    def test_are0battalionstodefendok(self):
        country = Country("Groenlandia","blue")
        country.changebattalions(1) #1 battalion
        expected = False
        self.assertEqual(expected, GameRules.battalionstodefendok(country,0))




if __name__ == '__main__':
    unittest.main()

