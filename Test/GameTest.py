import sys
sys.path.append("../Classes/Round/")
sys.path.append("../Classes/GameRules/")

from Players import Players,HumanPlayers,IAPlayers,ArrayPlayers
from Countries import Countries,Country
from Game import Game
from GameRules import GameRules
from CoreVariables import CoreVariables

import unittest

class GameTest(unittest.TestCase):

	global playersExpected
	global p1
	global p2
	global p3
	global initBattalions

	initBattalions = GameRules.getinitialbattalions(3)
	p1 = HumanPlayers("Pepe",initBattalions,"orange",[])
	p2 = HumanPlayers("Ana",initBattalions,"red",[])
	p3 = HumanPlayers("Yo",initBattalions,"blue",[])
	playersExpected = [p1,p2,p3]

		#check the number of cards left
	def test_getjockercardsleft(self):
		game = Game()
		expected = 2
		self.assertEqual(expected, game.getjokernum())

	def test_getinfantrycardsleft(self):
		game = Game()
		expected = 14
		self.assertEqual(expected, game.getinfantrynum())

	def test_getchivalrycardsleft(self):
		game = Game()
		expected = 14
		self.assertEqual(expected, game.getchivalrynum())

	def test_getartillerycardsleft(self):
		game = Game()
		expected = 14
		self.assertEqual(expected, game.getartillerynum())

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
		IA1 = IAPlayers("1",0,"green",[])
		IA2 = IAPlayers("2",0,"white",[])
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

	def test_initfirstphasecompletewithoutIA(self):
		p1 = HumanPlayers("Pepe",initBattalions,"orange",[])
		p2 = HumanPlayers("Ana",initBattalions,"red",[])
		p3 = HumanPlayers("Yo",initBattalions,"blue",[])
		playersExpected = [p1,p2,p3]
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
		usedBattalions = int(len(world) / len(players))
		for player in players:
			usedBattalionsAux = player.getusedbattalions()
			self.assertEqual(usedBattalions,usedBattalionsAux)
			player.distributebatallions()
			usedBeforeBattalions = player.getusedbattalions()
			self.assertEqual(usedBeforeBattalions,35)

	def test_orderrolls(self):
		p1 = HumanPlayers("Pepe",initBattalions,"orange",[])
		p2 = HumanPlayers("Ana",initBattalions,"red",[])
		p3 = HumanPlayers("Yo",initBattalions,"blue",[])
		playersExpected = [p1,p2,p3]
		tidyrolls = [3,5,2]
		game = Game()
		game.initboard()
		firstPlayer = game.firstplayer(tidyrolls,playersExpected)
		orderedPlayers = ArrayPlayers().orderplayers(playersExpected,firstPlayer)
		self.assertEqual(orderedPlayers[0].isequal(playersExpected[1]),True)
		self.assertEqual(orderedPlayers[1].isequal(playersExpected[0]),True)
		self.assertEqual(orderedPlayers[2].isequal(playersExpected[2]),True)

	def test_allconquers(self):
		p1 = HumanPlayers("Pepe",initBattalions,"orange",[])
		p2 = HumanPlayers("Ana",initBattalions,"red",[])
		p3 = HumanPlayers("Yo",initBattalions,"blue",[])
		playersExpected = [p1,p2,p3]
		tidyrolls = [3,5,2]
		game = Game()
		game.initboard()
		firstPlayer = game.firstplayer(tidyrolls,playersExpected)
		orderedPlayers = ArrayPlayers().orderplayers(playersExpected,firstPlayer)
		self.assertEqual(orderedPlayers[0].isequal(playersExpected[1]),True)
		self.assertEqual(orderedPlayers[1].isequal(playersExpected[0]),True)
		self.assertEqual(orderedPlayers[2].isequal(playersExpected[2]),True)
		game.initphaseplayers(3,orderedPlayers)
		game.initallconquers()
		players = game.getplayers()
		usedBattalions = int(len(world) / len(players))
		world = game.getcountries()
		for player in players:
			usedBattalionsAux = player.getusedbattalions()
			self.assertEqual(usedBattalions,usedBattalionsAux)

	def test_phaseonecomplete(self):
		p1 = HumanPlayers("Pepe",initBattalions,"orange",[])
		p2 = HumanPlayers("Ana",initBattalions,"red",[])
		p3 = HumanPlayers("Yo",initBattalions,"blue",[])
		playersExpected = [p1,p2,p3]
		tidyrolls = [3,5,2]
		game = Game()
		game.initboard()
		firstPlayer = game.firstplayer(tidyrolls,playersExpected)
		orderedPlayers = ArrayPlayers().orderplayers(playersExpected,firstPlayer)
		self.assertEqual(orderedPlayers[0].isequal(playersExpected[1]),True)
		self.assertEqual(orderedPlayers[1].isequal(playersExpected[0]),True)
		self.assertEqual(orderedPlayers[2].isequal(playersExpected[2]),True)
		game.initphaseplayers(3,orderedPlayers)
		players = game.getplayers()
		world = game.getcountries()
		for country in world:
			index = world.index(country)
			if( index != 0):
				index = index % len(players)
			player = players[index]
			game.initconquers(country,player)
		usedBattalions = int(len(world) / len(players))
		for player in players:
			usedBattalionsAux = player.getusedbattalions()
			self.assertEqual(usedBattalions,usedBattalionsAux)
			player.distributebatallions()
			usedBeforeBattalions = player.getusedbattalions()
			self.assertEqual(usedBeforeBattalions,35)

	def test_phasetwocomplete(self):
		print("vamos a simular todos los ataques")
		p1 = HumanPlayers("Pepe",initBattalions,"orange",[])
		p2 = HumanPlayers("Ana",initBattalions,"red",[])
		p3 = HumanPlayers("Yo",initBattalions,"blue",[])
		playersExpected = [p1,p2,p3]
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
		usedBattalions = int(len(world) / len(players))
		for player in players:
			usedBattalionsAux = player.getusedbattalions()
			self.assertEqual(usedBattalions,usedBattalionsAux)
			player.distributebatallions()
			usedBeforeBattalions = player.getusedbattalions()
			self.assertEqual(usedBeforeBattalions,35)

if __name__ == '__main__':
	unittest.main()
