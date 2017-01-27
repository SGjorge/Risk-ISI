import sys
sys.path.append("../Classes/GameRules/")

from random import randint
from GameRules import GameRules
from CoreVariables import CoreVariables
from Countries import Countries,World,Country
from Players import Players,HumanPlayers,IAPlayers,ArrayPlayers

class Game:
	__COUNTRIES = None
	__PLAYERS = None
	__JOKERS = 2
	__INFANTRY = 14
	__CHIVALRY = 14
	__ARTYLLERY = 14

	def getcountries(self):
		return self.__COUNTRIES

	def getplayers(self):
		return self.__PLAYERS

	def getjokernum(self):
		return self.__JOKERS

	def getinfantrynum(self):
		return self.__INFANTRY

	def getchivalrynum(self):
		return self.__CHIVALRY

	def getartillerynum(self):
		return self.__ARTYLLERY

	def initboard(self):
		self.__COUNTRIES = World().world

	def initplayers(self,players):
		self.__PLAYERS = players

	def initphaseplayers(self,numPlayers,players):
		self.__PLAYERS = players
		if (GameRules().numberofplayersok(numPlayers)) and (numPlayers > len(players)):
			for i in range(1,(numPlayers-len(players) + 1)):
				IA = IAPlayers(str(i),0,CoreVariables().colorPlayers[len(players)+1],[])
				self.__PLAYERS.append(IA)

	def initallconquers(self):
		for country in self.__COUNTRIES:
			index = self.__COUNTRIES.index(country)
			if( index != 0):
				index = index % len(self.__PLAYERS)
			player = self.__PLAYERS[index]
			self.initconquers(country,player)

	def initconquers(self,country,player):
		country.changebattalions(1)
		country.changeconqueror(player)
		player.addconqueredcountry(country)

	def firstplayer(self,rolls,players):
		first = rolls[0]
		for roll in rolls:
			if (roll >= first):
				first = roll
			if (rolls.index(roll) == len(rolls)):
				break
		return players[rolls.index(first)]

	def initallworldconquered(self):
		for player in self.__PLAYERS:
			player.distributebatallions()

	def lostconqueredcountry(self,player,countryLost,winner):
		destinyBattalions = countryLost.getbattalions()
		if(destinyBattalions == 0):
			conqueredCountries = player.getconqueredcountries()
			player.removeconqueredcountry(countryLost)
			winner.addconqueredcountry(countryLost)
			countryLost.changebattalions(1)

	def processresult(self,result):
		if result == None:
			return None
		battalions = result[0]
		origin = result[1]
		destiny = result[2]
		for roll in battalions:
			if(roll == 0):
				loser = destiny.getconqueror()
				country = destiny
			else:
				loser = origin.getconqueror()
				country = origin
			conqueredCountries = loser.getconqueredcountries()
			loser.changebattalions(roll)
			auxIndex = conqueredCountries.index(country)
			loserCountry = conqueredCountries[auxIndex]
			loserCountry.changebattalions(-1)
		playerDestiny = destiny.getconqueror()
		playerOrigin = origin.getconqueror()
		self.lostconqueredcountry(playerDestiny,destiny,playerOrigin)
		return True


	# simula el ataque al azar de un jugador a un pais no conquistado
	def roundplayerphasetworoll(self,player):
		if player == None:
			return None
		conqueredCountries = player.getconqueredcountries()
		index = -1
		while(index == -1):
			rndIndex = randint(0,len(self.__COUNTRIES)-1)
			w = self.__COUNTRIES[rndIndex]
			try:
				auxIndex = conqueredCountries.index(w)
				index = auxIndex
			except:
				continue
		rndIndex = randint(0,len(conqueredCountries)-1)
		origin = conqueredCountries[rndIndex]
		destiny = self.__COUNTRIES[index]
		battalions = randint(1,3)
		if(GameRules().battalionstoattackok(origin,battalions)) and (GameRules().countriesokforthebattle(origin,destiny)):
			attackRolls = player.attack(origin,destiny,battalions)
			deffendPlayer = destiny.getconqueror()
			battalions = randint(1,2)
			deffendRolls = deffendPlayer.defence(destiny,battalions)
			result = GameRules().getlostbattalions(attackRolls,deffendRolls)
			return [result,origin,destiny]
		else:
			return None

	def reorderbattalions(self,player):
		print("vamos a reordenar")
