import sys
sys.path.append("../Classes/GameRules/")

from GameRules import GameRules
import unittest

class GameRulesTest(unittest.TestCase):

	#Comprueba si el numero de jugadores es correcto (3-6)
    def isoneplayerok(self):
        expected = False
        self.assertEqual(expected, GameRules.numberofplayers(1))

    def arefiveplayersok(self):
        expected = True
        self.assertEqual(expected, GameRules.numberofplayers(5))

    def aresevenplayersok(self):
        expected = False
        self.assertEqual(expected, GameRules.numberofplayers(7))


if __name__ == '__main__':
    unittest.main()

