# -*- coding: utf-8 -*-

import sys
sys.path.append("../")
from CoreVariables import CoreVariables as CV
sys.path.append("../Classes/Round")
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
        return CV.extraBattalions[cardExchangeNum]





