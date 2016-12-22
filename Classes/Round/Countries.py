import sys
from CoreVariables import CoreVariables

class Countries(object):
    def nameok(self, name):
        return None;
    def countbattalion(self):
        return 0;



        
class Country(Countries):

    global absolutes

    def __init__(self):
        self.name = None
        self.battalion = 0

    absolutes = CoreVariables()

    def nameok (self, name):
        if (name in absolutes.paises):
            return True;
        else:
            return False;

    def countbattalion (self):
        return self.battalion
