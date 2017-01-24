import sys
sys.path.append("../Classes/GameRules/")

from GameRules import GameRules
from CoreVariables import CoreVariables
from Countries import Countries,World,Country
from Players import Players,HumanPlayers,IAPlayers,ArrayPlayers

class Game:
	__COUNTRIES = None
	__PLAYERS = None

	def getcountries(self):
		return self.__COUNTRIES

	def getplayers(self):
		return self.__PLAYERS

	def initboard(self):
		self.__COUNTRIES = World().world

	def initplayers(self,players):
		self.__PLAYERS = players

	def initphaseplayers(self,numPlayers,players):
		self.__PLAYERS = players
		if (GameRules().numberofplayersok(numPlayers)) and (numPlayers > len(players)):
			for i in range(1,(numPlayers-len(players) + 1)):
				IA = IAPlayers(str(i),0,CoreVariables().colorPlayers[len(players)+1])
				self.__PLAYERS.append(IA)

	def initconquers(self,country,player):
		country.changebattalions(1)
		country.changeconqueror(player)
		player.addconqueredcountry(country)




		