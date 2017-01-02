import sys
sys.path.append("../Classes/Round/")

from Players import Players,HumanPlayers,IAPlayers,ArrayPlayers
from Countries import Countries
from Game import Game
import unittest

class GameTest(unittest.TestCase):

	global game

	game = Game()

	def test_initgame(self):
		self.assertEqual(None,Game().getcountries())
		self.assertEqual(None,Game().getplayers())


if __name__ == '__main__':
	unittest.main()