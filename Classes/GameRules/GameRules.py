import sys
sys.path.append("../")

from CoreVariables import CoreVariables as CV
from Tables import Tables as T

class GameRules:


    @classmethod
    def numberofplayers(self,num):
        if  (num >= CV().minPlayers) and (num <= CV().maxPlayers):
            return True
        return False

    @classmethod
    def getInitialBattalions(self,num):
        return T.initialBattalions[num]

    @classmethod
    def getBattalionsPerContinent(self,continent):
        return T.battallionsPerContinent[continent]
