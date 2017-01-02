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

	def getname(self):
		return self.__NAME

	def getbattalions(self):
		return self.__BATTALIONS

	def getcolourid(self):
		return self.__COLOURID

	def isequal(self,player):
		return ((self.__NAME == player.getName()) and \
			    (self.__BATTALIONS == player.getBattalions()) and \
			    (self.__COLOURID == player.getColourId()))

	def cuberoll(self):
		roll = randint(1,6)
		return roll

	def rolls(self,index):
		rolls = []
		for i in range(1,(index + 1)):
			roll = self.cubeRoll()
			rolls.append(roll)
		return rolls

	#return -1 if batallions'll be incorrect
	def defendroll(self,defendBattalions):
		if (defendBattalions < 1) or (defendBattalions > 2): #aqui tendremos que llamar a la regla cuando esté implementada
			return -1

		defendRoll = self.rolls(defendBattalions)
		return defendRoll

	def assaultroll(self,assaultBattalions):
		if (assaultBattalions < 1) or (assaultBattalions > 3): #aqui tendremos que llamar a la regla cuando esté implementada
			return -1

		assaultRoll = self.rolls(assaultBattalions)
		return assaultRoll

	def tostring(self):
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
	def orderplayers(self,players,first):
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

	def tostring(self,players):
		string = ''
		for i in players:
			string += i.toString() + ", "
		return string
		

