import sys
sys.path.append("../Classes/GameRules/")
sys.path.append("../../")

from random import randint
from Cards import Cards, Infantry, Chivalry, Artillery
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

	def getcardtypenumber(self):
		infCount = 0
		chiCount = 0
		artCount = 0
		jokCount = 0
		cards = self.getcards()
		for card in cards:
			if card.getname() == "infantry":
				infCount = infCount + 1
			elif card.getname() == "chivalry":
				chiCount = chiCount + 1
			elif card.getname() == "artillery":
				artCount = artCount + 1
			elif card.getname() == "joker":
				jokCount = jokCount + 1
		return (jokCount,infCount,chiCount,artCount)

	def addcards(self,newCards):
		for card in newCards:
			if card.getname() == "infantry":
				self.__CARDS.append(Infantry())
			elif card.getname() == "chivalry":
				self.__CARDS.append(Chivalry())
			elif card.getname() == "artillery":
				self.__CARDS.append(Artillery())
			elif card.getname() == "joker":
				self.__CARDS.append(Cards())
		return self.getcardsnumber()

	def delcards(self,nameCard,num):
		[jokCount,infCount,chiCount,artCount] = self.getcardtypenumber()
		if nameCard == "infantry":
			infCount = infCount - num
		elif nameCard == "chivalry":
			chiCount = chiCount - num
		elif nameCard == "artillery":
			artCount = artCount - num
		elif nameCard == "joker":
			jokCount = jokCount - num

		self.__CARDS = [] #vaciamos la lista
		for i in range(1,infCount+1):
			self.__CARDS.append(Infantry())
		for i in range(1,chiCount+1):
			self.__CARDS.append(Chivalry())
		for i in range(1,artCount+1):
			self.__CARDS.append(Artillery())
		for i in range(1,jokCount+1):
			self.__CARDS.append(Cards())
		return self.getcardsnumber()


	def picacard(self):
		type = randint(1,4)
		if type == 1:
			self.__CARDS.append(Cards())
		elif type == 2:
			self.__CARDS.append(Infantry())
		if type == 3:
			self.__CARDS.append(Chivalry())
		if type == 4:
			self.__CARDS.append(Artillery())
		return self.getcardsnumber()

	def getusedbattalions(self):
		countries = self.getconqueredcountries()
		usedbattalion = 0
		for country in countries:
			battalionscountry = country.getbattalions()
			usedbattalion += battalionscountry
		return usedbattalion

	def modifyconquered(self,c):
		self.__CONQUEREDCOUNTRIES = c

	def changebattalions(self,battalions):
		self.__BATTALIONS += battalions

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

	def attack (self):
		pass
	def deffend (self):
		pass

# derivated class HumanPlayers to Players
class HumanPlayers(Players):
	def __init__(self,name,battalions,color,cards):
		super(self.__class__, self).__init__(name,battalions,color,cards)


	def attack (self, origin, destiny, battalions):
		#devuelve un array de tres cosas: el pais DESDE el que ataca, el pais AL que ataca
		#y su tirada entera (con los battallones con lo que queria atacar)
		attacked = self.rolls(battalions)
		return [origin, destiny, attacked]

	def deffend (self, country, battalions):
		deffended = self.rolls(battalions)
		return [country, deffended]
# derivated class IAPlayers to Players
class IAPlayers(Players):
	def __init__(self,name,battalions,color,cards):
		name = name + "IA"
		super(self.__class__, self).__init__(name,battalions,color,cards)

	#siempre supongo que el pais con el que quiero atacar o defender es mio porque se comprueba antes
	def attack (self, origin, destiny):
		#solo va a atacar si tiene mas de cinco batallones en el pais origen, y devolvera
		#los mismos valores que el attack de human. Si no los tiene, devuelve todos nulos
		#devuelve el NOMBRE del pais
		conquered = self.getconqueredcountries()
		for i in range(len(conquered)):
			if (conquered[i].name == origin):
				countrOrigin = conquered[i]
				if countrOrigin.battalions >= 5:
					attacked = self.rolls(3)
					return [origin, destiny, attacked]
		return [None, None, None]

	def deffend (self, country):
		#devuelve el NOMBRE del pais y la tirada, siempre va a atacar con los maximos que pueda
		conquered = self.getconqueredcountries()
		for i in range(len(conquered)):
			if (conquered[i].name == country):
				countryDeffended = conquered[i]
				if countryDeffended.battalions >= 2:
					deffended = self.rolls(2)

					return [country, deffended]
				else:
					deffended = self.rolls(countryDeffended.battalions)
					return [country, deffended]
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
