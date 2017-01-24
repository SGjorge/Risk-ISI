# -*- coding: utf-8 -*-

import sys
sys.path.append("../")
sys.path.append("../Clases/Round/")
from CoreVariables import CoreVariables as CV
from Countries import Countries, Country

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
