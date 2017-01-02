# -*- coding: utf-8 -*-

import sys
from Tables import Tables as T
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
        return T.initialBattalions[numPlayers]

    @classmethod
    def getbattalionspercontinent(self,continent):
        return T.battalionsPerContinent[continent]

    @classmethod
    def getbattalionspercountries(self,numCountries):
        numBattalions = numCountries // 3
        if numBattalions < 3:
            numBattalions = 3
        return numBattalions

    @classmethod
    def battalionstoattackok(self,attackingCountry,numBattalions):
        totalBattalions = Country.getbattalions(attackingCountry)
        print ("\n" + "total = " + str(totalBattalions))
        print ("attack = " + str(numBattalions) + "\n")
        if numBattalions <= 3 and (totalBattalions - numBattalions) >= 1:
            return True
        return False
