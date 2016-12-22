import sys
sys.path.append("../")

from CoreVariables import CoreVariables as CV


class GameRules:


    @classmethod
    def numberofplayers(self,num):
        if  (num >= CV().minPlayers) and (num <= CV().maxPlayers):
            return True
        return False
