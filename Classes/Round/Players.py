import sys
sys.path.append("../Classes/GameRules/")
sys.path.append("../../")

from GameRules import GameRules
from CoreVariables import CoreVariables

class Players:
	__NAME = None
	__BATTALIONS = 0
	__COLOURID = None

	def __init__(self,name,battalions,color):
		self.__NAME = name
		self.__BATTALIONS = battalions
		self.__COLOURID = color

	def getName(self):
		return self.__NAME

	def getBattalions(self):
		return self.__BATTALIONS

	def getColourId(self):
		return self.__COLOURID

	def isEqual(self,player):
		return ((self.__NAME == player.getName()) and \
			    (self.__BATTALIONS == player.getBattalions()) and \
			    (self.__COLOURID == player.getColourId()))

	def toString(self):
		return (self.__NAME + " " + str(self.__BATTALIONS) + " " +self.__COLOURID)

# derivated class HumanPlayers to Players
class HumanPlayers(Players):
	def __init__(self,name,battalions,color):
		super(self.__class__, self).__init__(name,battalions,color)

# derivated class IAPlayers to Players
class IAPlayers(Players):
	def __init__(self,name,battalions,color):
		name = name + "IA"
		super(self.__class__, self).__init__(name,battalions,color)

# this class is an API to work about Players' array 
class ArrayPlayers:
	# put first in first position array and the other to the left hand in order in new right hand array
	def orderPlayers(self,players,first):
		newPlayer = []
		newPlayer.append(first)
		try:
			firstPosition = players.index(first)
		except ValueError:
			print (ValueError)
			return players
		for i in range(firstPosition,(1-firstPosition)):
			newPlayer.append(players[i])
		return newPlayer
		

