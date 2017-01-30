# -*- coding: utf-8 -*-

import sys
sys.path.append("../")
sys.path.append("../Clases/Round/")

from Cards import Cards, Infantry, Chivalry, Artillery
from CoreVariables import CoreVariables as CV
from Countries import Countries, Country
from Players import Players, HumanPlayers, IAPlayers


class GameRules:

    @classmethod
    def numberofplayersok(self,numPlayers):
        if  (numPlayers >= CV().minPlayers) and (numPlayers <= CV().maxPlayers):
            return True
        return False

    @classmethod
    def getinitialbattalions(self,numPlayers):
        return CV.initialBattalions[numPlayers]

    @classmethod
    def getbattalionspercontinent(self,continent):
        return CV.battalionsPerContinent[continent]

    @classmethod
    def getbattalionspercountries(self,numCountries):
        numBattalions = numCountries // 3
        if numBattalions < 3:
            numBattalions = 3
        return numBattalions

    @classmethod
    def battalionstoattackok(self,attackingCountry,numBattalions):
        totalBattalions = Country.getbattalions(attackingCountry)
        if numBattalions > 0 and numBattalions <= 3 and (totalBattalions - numBattalions) >= 1:
            return True
        return False

    @classmethod
    def battalionstodefendok(self,defendingCountry,numBattalions):
        totalBattalions = Country.getbattalions(defendingCountry)
        if numBattalions > 0 and numBattalions <= 2 and (totalBattalions - numBattalions) >= 0:
            return True
        return False

    @classmethod
    def countriesokforthebattle(self,countryAtt,countryDef):
        if (countryAtt.conqueror != countryDef.conqueror):
       	    return Country.areneighbours(countryAtt,countryDef)
        return False

    @classmethod
    def getextrabattalions(self,cardExchangeNum):
        if cardExchangeNum > 14:
            cardExchangeNum = 14
        return CV.extraBattalions[cardExchangeNum]

    @classmethod
    def gettheresultsordered(self,rolls):
        if len(rolls) > 1:
            if rolls[1] > rolls[0]:
                rollAux = rolls[1]
                rolls[1] = rolls[0]
                rolls[0] = rollAux
        if len(rolls) == 3:
            if rolls[2] > rolls[1]:
                if rolls[2] > rolls[0]:
                    rollAux = rolls[0]
                    rolls[0] = rolls[2]
                rolls[2] = rolls[1]
                rolls[1] = rollAux
        return rolls

    @classmethod
    def getlostbattalions(self,rollsAtt,rollsDef):
        #Returns the number of lost battalions of the ATTACKING player
        rollsAtt = self.gettheresultsordered(rollsAtt)
        rollsDef = self.gettheresultsordered(rollsDef)
        if len(rollsDef) <= len(rollsAtt):
            lostAttBattalions = [0 for i in range(len(rollsDef))] #Variable a retornar
            for i in range(len(rollsDef)): #comienza en cero
                if rollsAtt[i] > rollsDef[i]:
                    lostAttBattalions[i] = 0
                else:
                    lostAttBattalions[i] = 1
        else:
            lostAttBattalions = [1]#Variable a retornar
            if rollsAtt[0] > rollsDef[0]:
                lostAttBattalions[0] = 0
        return  lostAttBattalions

    @classmethod
    def checkcardsnum(self, player):
        if (player.getcardsnumber() < 5):
            return True
        return False

    @classmethod
    def cardstoexchangeok(self, player, cardname):
        cards = player.getcards()
        count = 0
        for card in cards:
            if card.getname() == cardname or card.getname() == "joker":
                count = count + 1
        if count >= 3:
            return True
        return False

    @classmethod
    def movebattalions(self,player,origCountry,destCountry,numBattalions):
        #mismo jugador
        if origCountry.getconqueror() != destCountry.getconqueror():
            return False

        #tropas correctas
        totalBattalions = origCountry.getbattalions()
        if totalBattalions - numBattalions < 1 :
            return False

        #vecinos directos
        if (destCountry.getname() in origCountry.neighbours.getarray()):
            return True

	#buscamos camino por los paises del jugador
        path = []
	#cogemos todos los vecinos directos de pais ORIGEN
        directOrigNeighbours = origCountry.neighbours.getarray() # == strings

	#cogemos todos los paises del jugador (son objetos Country)
        conqueredCountries = player.getconqueredcountries() # == objetos
        playerCountries = []
        for conqueredCountry in conqueredCountries:
            playerCountries.append(conqueredCountry.name) # cogemos todos los paises del jugador como strings
       
        for directOrigNeighbour in directOrigNeighbours:
            if directOrigNeighbour in playerCountries:
                #creamos array solo con los vecinos directos de ORIGEN que pertenecen al JUGADOR.
                path.append (directOrigNeighbour)

        #para cada pais vecino de origen que es del jugador = country,
        for country in path:
            # miramos si es vecino directo de DESTINO
            if (destCountry.getname() in CV.tableNeighbours[country]): #country.neighbours.getarray():
                return True
            #si no, miramos los vecinos del "country"
            #para cada vecino de country = countryNeigh,
            for countryNeigh in CV.tableNeighbours[country]: #country.neighbours.getarray():
                #miramos si pertenece al jugador, si no está en el path, y si no es origen
                if (countryNeigh in playerCountries) & (countryNeigh not in path) & (not (countryNeigh is origCountry.getname())):
                    #entonces se añade al path y se vuelve a empezar
                    path.append(countryNeigh)
        return False






