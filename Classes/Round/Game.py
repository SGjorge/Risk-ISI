import sys
sys.path.append("../Classes/GameRules/")

from GameRules import GameRules
from CoreVariables import CoreVariables
from Countries import Countries,World,Country
from Players import Players,HumanPlayers,IAPlayers,ArrayPlayers

class Game:
	__COUNTRIES = None
	__PLAYERS = None
	__JOKERS = 2
	__INFANTRY = 14
	__CHIVALRY = 14
	__ARTYLLERY = 14

	def getcountries(self):
		return self.__COUNTRIES

	def getplayers(self):
		return self.__PLAYERS

	def getjokernum(self):
		return self.__JOKERS

	def getinfantrynum(self):
		return self.__INFANTRY

	def getchivalrynum(self):
		return self.__CHIVALRY

	def getartillerynum(self):
		return self.__ARTYLLERY

	def initboard(self):
		self.__COUNTRIES = World().world

	def initplayers(self,players):
		self.__PLAYERS = players

	def initphaseplayers(self,numPlayers,players):
		self.__PLAYERS = players
		if (GameRules().numberofplayersok(numPlayers)) and (numPlayers > len(players)):
			for i in range(1,(numPlayers-len(players) + 1)):
				IA = IAPlayers(str(i),0,CoreVariables().colorPlayers[len(players)+1],[])
				self.__PLAYERS.append(IA)

	def initallconquers(self):
		for country in self.__COUNTRIES:
			index = self.__COUNTRIES.index(country)
			if( index != 0):
				index = index % len(self.__PLAYERS)
			player = self.__PLAYERS[index]
			self.initconquers(country,player)

	def initconquers(self,country,player):
		country.changebattalions(1)
		country.changeconqueror(player)
		player.addconqueredcountry(country)

	def firstplayer(self,rolls,players):
		first = rolls[0]
		for roll in rolls:
			if (roll >= first):
				first = roll
			if (rolls.index(roll) == len(rolls)):
				break
		return players[rolls.index(first)]

	def initallworldconquered(self):
		for player in self.__PLAYERS:
			player.distributebatallions()