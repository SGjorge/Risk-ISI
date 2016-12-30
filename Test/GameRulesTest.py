import sys
sys.path.append("../Classes/GameRules/")

from GameRules import GameRules
import unittest

class GameRulesTest(unittest.TestCase):

        #Checks if the number of players is ok (3-6)
    def test_isoneplayerok(self):
        expected = False
        self.assertEqual(expected, GameRules.numberofplayers(1))

    def test_arefiveplayersok(self):
        expected = True
        self.assertEqual(expected, GameRules.numberofplayers(5))

    def test_aresevenplayersok(self):
        expected = False
        self.assertEqual(expected, GameRules.numberofplayers(7))

        #Checks the number of initial battalions per player, based on the total number of players
    def test_initialbattalions3(self):
        expected = 35
        self.assertEqual(expected, GameRules.getInitialBattalions(3))

    def test_initialbattalions4(self):
        expected = 30
        self.assertEqual(expected, GameRules.getInitialBattalions(4))

    def test_initialbattalions5(self):
        expected = 25
        self.assertEqual(expected, GameRules.getInitialBattalions(5))

    def test_initialbattalions6(self):
        expected = 20
        self.assertEqual(expected, GameRules.getInitialBattalions(6))

        #Checks the number of extra battalions per each whole conquered continent 
    def test_battalionsperamericaN(self):
        expected = 5
        self.assertEqual(expected, GameRules.getBattalionsPerContinent("América Norte")) 

    def test_battalionsperasia(self):
        expected = 7
        self.assertEqual(expected, GameRules.getBattalionsPerContinent("Asia")) 

    def test_battalionsperamericaS(self):
        expected = 2
        self.assertEqual(expected, GameRules.getBattalionsPerContinent("América Sur")) 

    def test_battalionspereuropa(self):
        expected = 5
        self.assertEqual(expected, GameRules.getBattalionsPerContinent("Europa"))

    def test_battalionsperafrica(self):
        expected = 3
        self.assertEqual(expected, GameRules.getBattalionsPerContinent("África")) 

    def test_battalionsperoceania(self):
        expected = 2
        self.assertEqual(expected, GameRules.getBattalionsPerContinent("Oceanía"))

        #Checks the number of extra battalions per conquered contries
    def test_battalionsper12countries(self):
        expected = 4
        self.assertEqual(expected, GameRules.getBattalionsPerCountries(12)) 

    def test_battalionsper2countries(self):
        expected = 3
        self.assertEqual(expected, GameRules.getBattalionsPerCountries(2)) 

    def test_battalionsper37countries(self):
        expected = 12
        self.assertEqual(expected, GameRules.getBattalionsPerCountries(37)) 



if __name__ == '__main__':
    unittest.main()

