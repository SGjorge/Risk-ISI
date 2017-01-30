#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../Classes/Round/")
sys.path.append("../Classes/GameRules")

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
		#borra cartas de UN TIPO. Tantas llamadas como tipo de cartas
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

	def modifyconqueredcountries(self,c):
		self.__CONQUEREDCOUNTRIES = c

	def changebattalions(self,battalions):
		self.__BATTALIONS += battalions

	def addconqueredcountry(self,country):
		c = self.__CONQUEREDCOUNTRIES
		c.append(country)
		self.__CONQUEREDCOUNTRIES = c

	def removeconqueredcountry(self,country):
		index = self.__CONQUEREDCOUNTRIES.index(country)
		self.__CONQUEREDCOUNTRIES.pop(index)

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

	def changecards(self):
		arrayCards = self.getcardtypenumber()
		jokCount = arrayCards[0]
		infCount = arrayCards[1]
		chiCount = arrayCards[2]
		artCount = arrayCards[3]
		total = self.getcardsnumber()
		#tres cartas iguales
		if artCount >= 3:
			return self.delcards("artillery", 3)
		if chiCount >= 3:
			return self.delcards("chivalry", 3)
		if infCount >= 3:
			return self.delcards("infantry", 3)
		#una carta de cada
		if infCount >= 1 and chiCount >= 1 and artCount >= 1:
			self.delcards("artillery", 1)
			self.delcards("chivalry", 1)
			return self.delcards("infantry", 1)
		#una carta y dos comodines
		if infCount >= 1 and jokCount >= 2:
			self.delcards("infantry", 1)
			return self.delcards("joker", 2)
		if chiCount >= 1 and jokCount >= 2:
			self.delcards("chivalry", 1)
			return self.delcards("joker", 2)
		if artCount >= 1 and jokCount >= 2:
			self.delcards("artillery", 1)
			return self.delcards("joker", 2)
		#dos cartas y un comodin
		if infCount >= 2 and jokCount >= 1:
			self.delcards("infantry", 2)
			return self.delcards("joker", 1)
		if chiCount >= 2 and jokCount >= 1:
			self.delcards("chivalry", 2)
			return self.delcards("joker", 1)
		if artCount >= 2 and jokCount >= 1:
			self.delcards("artillery", 2)
			return self.delcards("joker", 1)

	def movebattalions(self,origCountry,destCountry,numBattalions):
                origCountry.changebattalions(-numBattalions)
                destCountry.changebattalions(numBattalions)
                return True

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
		#solo devuelve el pais que es a defender y la tirada aleatoria
		deffended = self.rolls(battalions)
		return [country, deffended]
	
	# vamos a definir una pequeña User interface destinada a la shell, según donde se vaya a implantar
	# habría que hacer su propia interface
	def whoattack(self):
		return input("Atacar a: ")

	def howmanyattack(self):
		return input("Batallones de ataque: ")

	def howmanydeffend(self):
		return input("Batallones de defensa: ")

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

	def removeplayer(self,players,remove):
		index = players.index(remove)
		players.pop(index)

	def tostring(self,players):
		string = ''
		for i in players:
			string += i.toString() + ", "
		return string
