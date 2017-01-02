
import sys
sys.path.append("../../")
from CoreVariables import CoreVariables

class Countries():
    global absolutes
    absolutes = CoreVariables()


    def __init__(self):
        self.world = []
        lenght = len(absolutes.countries)
        for i in range(0, lenght):
            countryAux = Country(absolutes.countries[i], None)
            self.world.append(countryAux)

    def printworld(self):
        lenght = len(self.world)
        for i in range(0,lenght):
            print (self.world[i].tostring())

    def nameok(self, name):
        return None;

#####clase padre#####

class Country(Countries):

    global absolutes

    def __init__(self, name, conqueror):
        self.name = name
        self.battalions = 0
        self.neighbours = Neighbours(name)
        self.conqueror = conqueror

    absolutes = CoreVariables()

    def getname(self):
        return self.name

    def getbatallions(self):
        return self.battalions

    def getconqueror (self):
        return self.conqueror

    def nameok (self):
        if (self.name in absolutes.countries):
            return True;
        else:
            return False;

    def changebattalions(self,numBattalions):
        self.battalions = self.battalions + numBattalions

    def tostring(self):
        return (str(self.name) + str(self.battalions) + str(self.conqueror))


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
