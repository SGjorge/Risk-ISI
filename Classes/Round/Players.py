import sys
sys.path.append("../Classes/GameRules/")
sys.path.append("../../")

from random import randint
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

	def cubeRoll(self):
		roll = randint(1,6)
		return roll

	#return -1 if batallions'll be incorrect
	def defendRoll(self,defendBattalions):
		if (defendBattalions < 1) or (defendBattalions > 2): #aqui tendremos que llamar a la regla cuando esté implementada
			return -1

		defendRoll = []
		for i in range(1,(defendBattalions + 1)):
			roll = self.cubeRoll()
			defendRoll.append(roll)

		return defendRoll

	def assaultRoll(self,assaultBattalions):
		if (assaultBattalions < 1) or (assaultBattalions > 3): #aqui tendremos que llamar a la regla cuando esté implementada
			return -1

		assaultRoll = []
		for i in range(1,(assaultBattalions + 1)):
			roll = self.cubeRoll()
			assaultRoll.append(roll)

		return assaultRoll

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
		firstPosition = 0
		try:
			firstPosition = players.index(first)
		except ValueError:
			print (ValueError)
			return players

		if(firstPosition == (len(players)-1)):
			players.reverse()
			return players
		elif (firstPosition == 0):
			return players
		
		newPlayer = []
		newPlayer.append(first)
		for i in range(1,(len(players)*2)):
			if(first.isEqual(players[firstPosition-i])):
				break
			newPlayer.append(players[firstPosition-i])
		return newPlayer

	def toString(self,players):
		string = ''
		for i in players:
			string += i.toString() + ", "
		return string
		

