# -*- coding: utf-8 -*-

import sys
sys.path.append("../Classes/GameRules/")

from GameRules import GameRules
import unittest

class GameRulesTest(unittest.TestCase):

        #Checks if the number of players is ok (3-6)
    def test_isoneplayerok(self):
        expected = False
        self.assertEqual(expected, GameRules.numberofplayersok(1))

    def test_arefiveplayersok(self):
        expected = True
        self.assertEqual(expected, GameRules.numberofplayersok(5))

    def test_aresevenplayersok(self):
        expected = False
        self.assertEqual(expected, GameRules.numberofplayersok(7))

        #Checks the number of initial battalions per player, based on the total number of players
    def test_initialbattalions3(self):
        expected = 35
        self.assertEqual(expected, GameRules.getinitialbattalions(3))

    def test_initialbattalions4(self):
        expected = 30
        self.assertEqual(expected, GameRules.getinitialbattalions(4))

    def test_initialbattalions5(self):
        expected = 25
        self.assertEqual(expected, GameRules.getinitialbattalions(5))

    def test_initialbattalions6(self):
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



if __name__ == '__main__':
    unittest.main()

