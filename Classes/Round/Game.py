import sys
sys.path.append("../Classes/GameRules/")

from GameRules import GameRules
from CoreVariables import CoreVariables
from Countries import Countries
from Players import Players,HumanPlayers,IAPlayers,ArrayPlayers

class Game:
	__COUNTRIES = None
	__PLAYERS = None

	def getcountries(self):
		return self.__COUNTRIES

	def getplayers(self):
		return self.__PLAYERS

	def initboard(self):
		self.__COUNTRIES = Countries().world

	def initplayers(self,players):
		self.__PLAYERS = players

	def firstphase(self,numPlayers,players):
		self.__PLAYERS = players
		if(numPlayers > len(players)):
			for i in range(1,(numPlayers-len(players) + 1)):
				IA = IAPlayers(str(i),0,CoreVariables().colorPlayers[len(players)+1])
				self.__PLAYERS.append(IA)


		