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

class ArrayPlayers:
	def __init__(self,numPlayers):
		if not (GameRules().numberofplayers(numPlayers)):
			arrayPlayer = [range(1,CoreVariables().numMinPlayers)]
			for i in range(1,numPlayers):
				arrayPlayer[i] = None
		else:
			arrayPlayer = [range(1,numPlayers)]
			for i in range(1,len(arrayPlayer)):
				arrayPlayer[i] = None
		return arrayPlayer
