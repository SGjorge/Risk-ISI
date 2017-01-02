import sys
sys.path.append("../Classes/Round/")

from Players import Players,HumanPlayers,IAPlayers,ArrayPlayers
from Countries import Countries
from Game import Game
import unittest

class PlayersTest(unittest.TestCase):

	def test_game(self):
		game = Game()
		self.assertEqual(None,Game())


if __name__ == '__main__':
	unittest.main()