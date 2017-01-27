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
		game.initallconquers()
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
		game.initphaseplayers(3,playersExpected)
		game.initallconquers()
		players = game.getplayers()
		world = game.getcountries()
		usedBattalions = int(len(world) / len(players))
		for player in players:
			usedBattalionsAux = player.getusedbattalions()
			self.assertEqual(usedBattalions,usedBattalionsAux)

	def test_initallworldconquered(self):
		p1 = HumanPlayers("Pepe",initBattalions,"orange",[])
		p2 = HumanPlayers("Ana",initBattalions,"red",[])
		p3 = HumanPlayers("Yo",initBattalions,"blue",[])
		playersExpected = [p1,p2,p3]
		tidyrolls = [3,5,2]
		game = Game()
		game.initboard()
		game.initphaseplayers(3,playersExpected)
		game.initallconquers()
		world = game.getcountries()
		players = game.getplayers()
		game.initallworldconquered()
		for player in players:
			usedBeforeBattalions = player.getusedbattalions()
			self.assertEqual(usedBeforeBattalions,35)

	def test_processresult(self):
		p1 = HumanPlayers("Pepe",initBattalions,"orange",[])
		p2 = HumanPlayers("Ana",initBattalions,"red",[])
		c1 = Country('Europa del norte', p1)
		c1.changebattalions(3)
		c2 = Country('América central', p2)
		c2.changebattalions(7)
		p1.addconqueredcountry(c1)
		p2.addconqueredcountry(c2)
		playersExpected = [p1,p2]
		game = Game()
		game.initplayers(playersExpected)
		rollResult = [0,-1]
		result = [rollResult,c1,c2]
		game.processresult(result)
		self.assertEqual(2,c1.getbattalions())
		self.assertEqual(6,c2.getbattalions())
		rollResult = [0,0]
		result = [rollResult,c2,c1]
		game.processresult(result)
		self.assertEqual(1,c1.getbattalions())
		self.assertEqual(p2.isequal(c1.getconqueror()),True)

	def test_reorderbattalions(self):
		p1 = HumanPlayers("Pepe",35,"orange",[])
		c1 = Country('Europa del norte', p1)
		c1.changebattalions(3)
		c2 = Country('América central', p1)
		c2.changebattalions(7)
		p1.addconqueredcountry(c1)
		p2.addconqueredcountry(c1)
		playersExpected = [p1]
		game = Game()
		game.initplayers(playersExpected)
		game.reorderbattalions(p1,c2,c1,5)
		self.assertEqual(8,c1.getbattalions())
		self.assertEqual(2,c2.getbattalions())

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
		game.initallconquers()
		usedBattalions = int(len(world) / len(players))
		for player in players:
			usedBattalionsAux = player.getusedbattalions()
			self.assertEqual(usedBattalions,usedBattalionsAux)
			player.distributebatallions()
			usedBeforeBattalions = player.getusedbattalions()
			self.assertEqual(usedBeforeBattalions,35)

	def test_phasetwocomplete(self):
		p1 = HumanPlayers("Pepe",initBattalions,"orange",[])
		p2 = HumanPlayers("Ana",initBattalions,"red",[])
		p3 = HumanPlayers("Yo",initBattalions,"blue",[])
		playersExpected = [p1,p2,p3]
		game = Game()
		game.initboard()
		game.initphaseplayers(3,playersExpected)
		game.initallconquers()
		game.initallworldconquered()
		players = game.getplayers()
		world = game.getcountries()
		Battalions = 35
		for player in players:
			roundPlayer = game.roundplayerphasetworoll(player)
			if (roundPlayer == None):
				continue
			game.processresult(roundPlayer)
			BeforeBattalions = player.getbattalions()
			roll = roundPlayer[0]
			for r in roll:
				if (r < 0):
					Battalions += -1
			self.assertEqual(Battalions,BeforeBattalions)
			game.reorderbattalions(player,)

if __name__ == '__main__':
	unittest.main()
