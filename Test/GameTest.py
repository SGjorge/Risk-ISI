import sys
sys.path.append("../Classes/Round/")

from Players import Players,HumanPlayers,IAPlayers,ArrayPlayers
from Countries import Countries
from Game import Game
from CoreVariables import CoreVariables

import unittest

class GameTest(unittest.TestCase):

	global game

	game = Game()

	def test_initgame(self):
		self.assertEqual(None,game.getcountries())
		self.assertEqual(None,game.getplayers())

	def test_initboard(self):
		world = game.getcountries() 
		countries = CoreVariables().countries 
		for (country,wCountry) in zip(countries,world):
			self.assertEqual(country,wCountry)

	def test_initplayers(self):
		p1 = HumanPlayers("Pepe",0,"orange")
		p2 = HumanPlayers("Ana",0,"red")
		p3 = HumanPlayers("Yo",0,"blue")
		playersExpected = [p1,p2,p3]
		game.initplayers(playersExpected)
		players = game.getplayers()
		print(players)
		for (pE,p) in zip(playersExpected,players):
			self.assertEqual(True,pE.isequal(p))

if __name__ == '__main__':
	unittest.main()