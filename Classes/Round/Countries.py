import sys
sys.path.append("../../")
from CoreVariables import CoreVariables

class Countries():
    def nameok(self, name):
        return None;
    def countbattalion(self):
        return 0;
#####clase padre#####

class Country(Countries):

    global absolutes

    def __init__(self, name):
        self.name = name
        self.battalions = 0
        self.neighbours = Neighbours(name)

    absolutes = CoreVariables()

    def nameok (self):
        if (self.name in absolutes.countries):
            return True;
        else:
            return False;

    def countbattalion (self):
        return self.battalions

class Neighbours(Countries):

    global absolutes
    absolutes = CoreVariables()

    def __init__(self, country):
        try:
            self.array = absolutes.tableNeighbours[country];
        except (KeyError):
            self.array = []

    def getarray (self):
        if self.array == None:
            return []
        else:
            return self.array
