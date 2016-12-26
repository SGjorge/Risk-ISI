import sys

class CoreVariables():
    def __init__(self):
        self.countries = ["Alaska", "Alberta", "Europa Occidental", "Europa del sur", "Europa del norte"]
        self.maxCountries = 42


    neighboursEuropaNorte = ['Europa del sur', 'Europa occidental']
    tableNeighbours = {'Europa del norte': neighboursEuropaNorte}

    def getneighbours (self, name):
        return self.tableNeighbours[name]
