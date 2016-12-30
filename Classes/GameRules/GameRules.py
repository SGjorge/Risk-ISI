import sys
sys.path.append("../")

from CoreVariables import CoreVariables as CV
from Tables import Tables as T

class GameRules:


    @classmethod
    def numberofplayers(self,numPlayers):
        if  (numPlayers >= CV().minPlayers) and (numPlayers <= CV().maxPlayers):
            return True
        return False

    @classmethod
    def getInitialBattalions(self,numPlayers):
        return T.initialBattalions[numPlayers]

    @classmethod
    def getBattalionsPerContinent(self,continent):
        return T.battalionsPerContinent[continent]

    @classmethod
    def getBattalionsPerCountries(self,numCountries):
        numBattalions = numCountries // 3
        if numBattalions < 3:
            numBattalions = 3
        return numBattalions
