# -*- coding: utf-8 -*-

import sys
sys.path.append("../")

from CoreVariables import CoreVariables as CV
from Tables import Tables as T

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
