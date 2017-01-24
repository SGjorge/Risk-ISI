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
	__CONQUEREDCOUNTRIES = []

	def __init__(self,name,battalions,color):
		self.__NAME = name
		self.__BATTALIONS = battalions
		self.__COLOURID = color
		self.__CONQUEREDCOUNTRIES = []

	def getname(self):
		return self.__NAME

	def getbattalions(self):
		return self.__BATTALIONS
		
	def getcolourid(self):
		return self.__COLOURID

	def getconqueredcountries(self):
		return self.__CONQUEREDCOUNTRIES

	def getusedbattalions(self):
		countries = self.getconqueredcountries()
		usedbattalion = 0
		for country in countries:
			battalionscountry = country.getbattalions()
			usedbattalion += battalionscountry
		return usedbattalion

	def modifyconquered(self,c):
		self.__CONQUEREDCOUNTRIES = c

	def addconqueredcountry(self,country):
		c = self.__CONQUEREDCOUNTRIES
		c.append(country)
		self.__CONQUEREDCOUNTRIES = c

	def isequal(self,player):
		return ((self.__NAME == player.getname()) and \
			    (self.__BATTALIONS == player.getbattalions()) and \
			    (self.__COLOURID == player.getcolourid()))

	def diceroll(self):
		roll = randint(1,6)
		return roll

	def rolls(self,index):
		rolls = []
		for i in range(1,(index + 1)):
			roll = self.diceroll()
			rolls.append(roll)
		return rolls

<<<<<<< HEAD
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

	# en principio esta pensando para la una IA simple, pero tambien nos sirve para posteriormente simular la fase 1
	def distributebatallions(self):
		unusedbattalions = self.__BATTALIONS - self.getusedbattalions()
		while (unusedbattalions > 0):
			for country in self.__CONQUEREDCOUNTRIES:
				if not (unusedbattalions > 0):
					break
				country.changebattalions(1)
				unusedbattalions -= 1


=======
>>>>>>> d16d37b76ce0538f5457f64048707fcbb3fe6490
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
			if(first.isequal(players[firstPosition-i])):
				break
			newPlayer.append(players[firstPosition-i])
		return newPlayer

	def tostring(self,players):
		string = ''
		for i in players:
			string += i.toString() + ", "
		return string
		

