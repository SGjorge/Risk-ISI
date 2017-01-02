import sys
sys.path.append("../Classes/GameRules/")

from GameRules import GameRules
from CoreVariables import CoreVariables
from Countries import Countries

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


		