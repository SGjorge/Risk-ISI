import sys
sys.path.append("../Classes/Round/")

from Players import Players,HumanPlayers,IAPlayers,ArrayPlayers
from Countries import Countries
from Game import Game
from CoreVariables import CoreVariables

import unittest

class GameTest(unittest.TestCase):

	def test_initgame(self):
		g1 = Game()
		self.assertEqual(None,g1.getcountries())
		self.assertEqual(None,g1.getplayers())

	def test_initboard(self):
		game = Game()
		game.initboard()
		world = game.getcountries()
		countries = CoreVariables().countries
		for (country,wCountry) in zip(countries,world):
			self.assertEqual(country,wCountry.getname())

	def test_initplayers(self):
		game = Game()
		p1 = HumanPlayers("Pepe",0,"orange")
		p2 = HumanPlayers("Ana",0,"red")
		p3 = HumanPlayers("Yo",0,"blue")
		playersExpected = [p1,p2,p3]
		game.initplayers(playersExpected)
		players = game.getplayers()
		for (pE,p) in zip(playersExpected,players):
			self.assertEqual(True,pE.isequal(p))

if __name__ == '__main__':
	unittest.main()