import sys
sys.path.append("../Classes/GameRules/")

from random import randint
from GameRules import GameRules
from CoreVariables import CoreVariables

class Game:
	__COUNTRIES = None
	__PLAYERS = None

	def getcountries(self):
		return self.__COUNTRIES

	def getplayers(self):
		return self.__PLAYERS


		