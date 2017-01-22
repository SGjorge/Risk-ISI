import sys
sys.path.append("../Classes/Round/")

from Players import Players,HumanPlayers,IAPlayers,ArrayPlayers
from Countries import Countries
from Game import Game
from CoreVariables import CoreVariables

import unittest

class GameTest(unittest.TestCase):

	global playersExpected
	global p1
	global p2
	global p3

	p1 = HumanPlayers("Pepe",0,"orange")
	p2 = HumanPlayers("Ana",0,"red")
	p3 = HumanPlayers("Yo",0,"blue")
	playersExpected = [p1,p2,p3]

	def test_initemptygame(self):
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
		game.initplayers(playersExpected)
		players = game.getplayers()
		for (pE,p) in zip(playersExpected,players):
			self.assertEqual(True,pE.isequal(p))

	def test_initphaseplayerswithIA(self):
		playersInitExpected = playersExpected
		game = Game()
		numPlayersExpected = 5 
		game.initphaseplayers(5,playersExpected)
		self.assertEqual(numPlayersExpected,len(game.getplayers()))
		IA1 = IAPlayers("1",0,"green")
		IA2 = IAPlayers("2",0,"white")
		playersInitExpected.append(IA1)
		playersInitExpected.append(IA2)
		players = game.getplayers()
		for (pE,p) in zip(playersInitExpected,players):
			self.assertEqual(True,pE.isequal(p))

	def test_initphaseplayerswithoutIA(self):
		playersInitExpected = playersExpected
		game = Game()
		game.initboard()
		numPlayersExpected = len(playersExpected)
		game.initphaseplayers(3,playersExpected)
		self.assertEqual(numPlayersExpected,len(game.getplayers()))
		players = game.getplayers()
		world = game.getcountries()
		for (pE,p) in zip(playersInitExpected,players):
			self.assertEqual(True,pE.isequal(p))

	def test_initconquer(self):
		game = Game()
		game.initboard()
		game.initphaseplayers(3,playersExpected)
		players = game.getplayers()
		world = game.getcountries()
		for country in world:
			index = world.index(country)
			if( index != 0):
				index = index % len(players)
			player = players[index]
			game.initconquers(country,player)
			self.assertEqual(1,country.getbattalions())
			self.assertEqual(player,country.getconqueror())

	def test_initfirstphasecompletehumanplayers(self):
		game = Game()
		game.initboard()
		game.initphaseplayers(3,playersExpected)
		players = game.getplayers()
		world = game.getcountries()
		for country in world:
			index = world.index(country)
			if( index != 0):
				index = index % len(players)
			player = players[index]
			game.initconquers(country,player)
		self.assertEqual(True,True)

if __name__ == '__main__':
	unittest.main()