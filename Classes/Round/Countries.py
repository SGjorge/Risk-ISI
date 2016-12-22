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
        self.battalions = 0
        self.neighbours = Neighbours()

    absolutes = CoreVariables()

    def nameok (self, name):
        if (name in absolutes.paises):
            return True;
        else:
            return False;

    def countbattalion (self):
        return self.battalions

class Neighbours(Countries):

    def __init__(self):
        self.array = []

    def getneighbours (self):
        if self.array == None:
            return []
        else:
            return self.array
