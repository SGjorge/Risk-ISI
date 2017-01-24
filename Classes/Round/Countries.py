
import sys
sys.path.append("../../")
from CoreVariables import CoreVariables

class Countries():

    def nameok(self, name):
        return None;

class Continent(Countries):
    def __init__(self, name):
        self.nameCont = name
        self.countries = []
        self.countries = CoreVariables().getcontinent(name)
        self.color = CoreVariables().getcontientcolor(name)

class World(Countries):

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
        for i in world:
            print (i.tostring())


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

    def getbattalions(self):
        return self.battalions

    def getconqueror (self):
        return self.conqueror

    def nameok (self):
        if (self.name in absolutes.countries):
            return True;
        else:
            return False;

    def changebattalions(self, numBattalions):
        self.battalions = self.battalions + numBattalions

    def changeconqueror(self, newOne):
        self.conqueror = newOne

    def tostring(self):
        try:
            return (str(self.name) + " "+ str(self.battalions) + ":" + self.conqueror.tostring())
        except:
            return (str(self.name) + " "+ str(self.battalions) + ":" + str(self.conqueror))

    def areneighbours(self, country):
        #return country.name in CoreVariables().getneighbours(self.name)
        return country.name in self.neighbours.getarray()
    def ithasneighbourhood (self):
        if len(self.neighbours.getarray())> 0:
            return True
        else:
            print self.neighbours.getarray()
            return False
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
