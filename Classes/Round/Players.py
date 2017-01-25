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
	__CARDS = []

	def __init__(self,name,battalions,color,cards):
		self.__NAME = name
		self.__BATTALIONS = battalions
		self.__COLOURID = color
		self.__CONQUEREDCOUNTRIES = []
		self.__CARDS = cards

	def getname(self):
		return self.__NAME

	def getbattalions(self):
		return self.__BATTALIONS

	def getcolourid(self):
		return self.__COLOURID

	def getconqueredcountries(self):
		return self.__CONQUEREDCOUNTRIES

	def getcards(self):
		return self.__CARDS

	def getcardsnumber(self):
		cards = self.getcards()
		return  len(cards)

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

	# en principio esta pensando para la una IA simple, pero tambien nos sirve para posteriormente simular la fase 1
	def distributebatallions(self):
		unusedbattalions = self.__BATTALIONS - self.getusedbattalions()
		while (unusedbattalions > 0):
			for country in self.__CONQUEREDCOUNTRIES:
				if not (unusedbattalions > 0):
					break
				country.changebattalions(1)
				unusedbattalions -= 1

	def tostring(self):
		return (self.__NAME + " " + str(self.__BATTALIONS) + " " +self.__COLOURID)

# derivated class HumanPlayers to Players
class HumanPlayers(Players):
	def __init__(self,name,battalions,color,cards):
		super(self.__class__, self).__init__(name,battalions,color,cards)

# derivated class IAPlayers to Players
class IAPlayers(Players):
	def __init__(self,name,battalions,color,cards):
		name = name + "IA"
		super(self.__class__, self).__init__(name,battalions,color,cards)
	def attack (self, country):
		countriesAux = self.getconqueredcountries()
		if (country in countriesAux):
			if (country.battalions > 4):
				return True
		return False
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
