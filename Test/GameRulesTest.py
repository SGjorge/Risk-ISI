import sys
sys.path.append("../Classes/GameRules/")

from GameRules import GameRules
import unittest

class GameRulesTest(unittest.TestCase):

	#Comprueba si el numero de jugadores es correcto (3-6)
    def test_isoneplayerok(self):
        expected = False
        self.assertEqual(expected, GameRules.numberofplayers(1))

    def test_arefiveplayersok(self):
        expected = True
        self.assertEqual(expected, GameRules.numberofplayers(5))

    def test_aresevenplayersok(self):
        expected = False
        self.assertEqual(expected, GameRules.numberofplayers(7))

	#Comprueba el numero de batallones iniciales de cada jugador, segun el numero total de jugadores
    def test_getinitialbattalions(self):
        expected = 35
        self.assertEqual(expected, GameRules.numberofinitialbattalions(3))

    def test_getinitialbattalions(self):
        expected = 35
        self.assertEqual(expected, GameRules.numberofinitialbattalions(4))

    def test_getinitialbattalions(self):
        expected = 35
        self.assertEqual(expected, GameRules.numberofinitialbattalions(5))

    def test_getinitialbattalions(self):
        expected = 35
        self.assertEqual(expected, GameRules.numberofinitialbattalions(6))



if __name__ == '__main__':
    unittest.main()

