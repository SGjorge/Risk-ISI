#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

class CoreVariables():
    def __init__(self):
        self.countries = ["Alaska", "Territorio del noroeste", "Groenlandia",
            "Alberta", "Ontario", "Quebec", "Estados Unidos del oeste", "Estados Unidos del este",
            "América central", "Venezuela", "Brasil", "Perú", "Argentina",
            "África del norte", "Egipto", "África oriental", "Congo", "África del sur", "Madagascar",
            "Europa occidental", "Europa del norte", "Europa del sur", "Gran Bretaña",
            "Islandia", "Escandinavia", "Ucrania", "Oriente medio", "India", "Siam",
            "Afganistán", "China", "Ural", "Siberia", "Irkutsk", "Mongolia",
            "Yakutsk", "Kamchatka", "Japón", "Indonesia", "Nueva Guinea",
            "Australia occidental", "Australia oriental"]
        self.cardsTotalNum = 44
        self.maxCountries = 42
        self.minPlayers = 3
        self.maxPlayers = 6
        self.colorPlayers = ["orange","red","blue","green","white","grey"]
    #tabla de colores de los continentes
    tablecontinentcolors = {'América del norte': 'yellow', 'América del sur': 'orange', 'Europa': 'blue', 'África': 'brown', 'Asia': 'green', 'Oceanía': 'grey'}
    #continentes:
    counEuropa = ['Islandia', 'Escandinavia', 'Ucrania', 'Europa del sur', 'Europa del norte', 'Gran Bretaña', 'Europa occidental']
    counAsia = ['Ural', 'Siberia', 'Yakutsk', 'Kamchatka', 'Irkutsk', 'Mongolia', 'Japón', 'China', 'Siam', 'India', 'Oriente medio', 'Afganistán']
    counOceania = ['Indonesia', 'Nueva Guinea', 'Australia oriental', 'Australia occidental']
    counAfrica = ['África del norte', 'Egipto', 'África oriental', 'Congo', 'África del sur', 'Madagascar']
    counASur = ['Venezuela', 'Brasil', 'Perú', 'Argentina']
    counANorte = ['Alaska', 'Territorio del noroeste', 'Groenlandia', 'Alberta', 'Ontario', 'Quebec',
                'Estados Unidos del oeste', 'Estados Unidos del este', 'América central']
    tableContinents = {'Europa': counEuropa, 'Asia': counAsia, 'Oceanía': counOceania, 'África': counAfrica, 'América del sur': counASur, 'América del norte': counANorte}
    #neighbours
    #europa
    neighboursEuropaNorte = ['Europa del Sur', 'Europa occidental','Ucrania', 'Escandinavia', "Gran Bretaña"]
    neighboursEuropaSur = ['Europa del norte', 'Europa occidental', "Ucrania", 'África del norte', 'Egipto', 'Oriente medio']
    neighboursEuropaOcc = ['Gran Bretaña', 'Europa del norte', 'Europa del sur', 'África del norte']
    neighboursGB = ['Islandia', 'Escandinavia', 'Europa del norte', 'Europa occidental']
    neighboursIsl = ['Groenlandia', 'Escandinavia', 'Gran Bretaña']
    neighboursEsca = ['Ucrania', 'Europa del norte', 'Gran Bretaña', 'Islandia']
    neighboursUck = ['Ural', 'Afganistán', 'Oriente medio', 'Europa del sur', 'Europa del norte', 'Escandinavia']
    #america del sur
    neighboursVenz = ['América central', 'Brasil', 'Perú']
    neighboursBra = ['Venezuela', 'Perú', 'Argentina', 'África del norte']
    neighboursPeru = ['Venezuela', 'Brasil', 'Argentina']
    neighboursArg = ['Perú', 'Brasil']
    #africa
    neighboursAN = ['Brasil', 'Europa occidental', 'Europa del sur', 'Egipto', 'África occidental', 'Congo']
    neighboursEgip = ['Europa del sur', 'Oriente medio', 'África del norte', 'África oriental']
    neighboursAO = ['Egipto', 'Oriente medio', 'Madagascar', 'África del sur', 'Congo', 'África del norte']
    neighboursAS = ['Congo', 'África oriental', 'Madagascar']
    neighboursMAD = ['Áfica oriental', 'África del sur']
    neighboursCon = ['África del norte', 'África oriental', 'África del sur']
    #oceania
    neighboursIND = ['Siam', 'Nueva Guinea', 'Australia occidental']
    neighboursNG = ['Indonesia', 'Australia oriental','Australia occidental']
    neighboursAOriental = ['Nueva Guinea', 'Australia occidental']
    neighboursAOcc = ['Indonesia', 'Nueva Guinea', 'Australia oriental']
    #Asia
    neighboursUral = ['Ucrania', 'Siberia', 'China', 'Afganistán']
    neighboursSib = ['Ural', 'Yakutsk', 'Irkutsk', 'Mongolia', 'China']
    neighboursYak = ['Siberia', 'Kamchatka', 'Irkutsk']
    neighboursKam = ['Yakutsk', 'Irkutsk', 'Mongolia', 'Japón', 'Alaska']
    neighboursIrk = ['Siberia', 'Yakutsk', 'Kamchatka', 'Mongolia']
    neighboursJap = ['Mongolia', 'Kamchatka']
    neighboursMong = ['Siberia', 'Irkutsk', 'Kamchatka', 'Japón', 'China']
    neighboursChi = ['Afganistán', 'Ural', 'Siberia', 'Mongolia', 'Siam', 'India']
    neighboursAf = ['Ucrania', 'Ural', 'China', 'India', 'Oriente medio']
    neighboursOM = ['Europa del sur', 'Ucrania', 'Afganistán', 'India', 'África oriental', 'Egipto']
    neighboursInd = ['Oriente medio', 'Afganistán', 'China', 'Siam']
    neighboursSiam = ['India', 'China', 'Indonesia']
    #america del norte
    neighboursAlk = ['Kamchatka', 'Territorio del noroeste', 'Alberta']
    neighboursTNE = ['Alaska', 'Alberta', 'Groenlandia', 'Ontario']
    neighboursGroe = ['Territorio del noroeste', 'Ontario', 'Quebec', 'Islandia']
    neighboursAlb = ['Alaska', 'Territorio del noroeste', 'Ontario', 'Estados Unidos del oeste']
    neighboursOnt = ['Alberta', 'Territorio del noroeste', 'Groenlandia', 'Quebec', 'Estados Unidos del este', 'Estados Unidos del oeste']
    neighboursQue = ['Ontario', 'Groenlandia', 'Estados Unidos del este']
    neighboursEUE = ['Estados Unidos del oeste', 'Ontario', 'Quebec', 'América central']
    neighboursEUO = ['Estados Unidos del este', 'Alberta', 'Ontario', 'América central']
    neighboursAmC = ['Estados Unidos del este', 'Estados Unidos del oeste', 'Venezuela']
    #tabla de vecinos
    tableNeighbours = {'Europa del norte': neighboursEuropaNorte, 'Europa del sur': neighboursEuropaSur,
                        'Europa occidental': neighboursEuropaOcc, 'Gran Bretaña': neighboursGB,
                        'Islandia': neighboursIsl, 'Escandinavia': neighboursEsca, 'Ucrania': neighboursUck,
                        'Venezuela': neighboursVenz, 'Brasil': neighboursBra, 'Perú': neighboursPeru,
                        'Argentina': neighboursArg, 'África del norte' : neighboursAN, 'Egipto': neighboursEgip,
                        'África oriental': neighboursAO, 'Madagascar': neighboursMAD, 'África del sur': neighboursAS,
                        'Congo': neighboursCon, 'Indonesia': neighboursIND, 'Nueva Guinea': neighboursNG,
                        'Australia oriental': neighboursAOriental, 'Australia occidental': neighboursAOcc,
                        'Ural': neighboursUral, 'Siberia': neighboursSib, 'Yakutsk': neighboursYak,
                        'Kamchatka': neighboursKam, 'Irkutsk': neighboursIrk, 'Japón': neighboursJap,
                        'Mongolia': neighboursMong, 'China': neighboursChi, 'Afganistán': neighboursAf,
                        'Oriente medio': neighboursOM, 'India': neighboursInd, 'Siam': neighboursSiam,
                        'Alaska': neighboursAlk, 'Territorio del noroeste': neighboursTNE, 'Groenlandia': neighboursGroe,
                        'Alberta': neighboursAlb, 'Ontario': neighboursOnt, 'Quebec': neighboursQue,
                        'Estados Unidos del este': neighboursEUE, 'Estados Unidos del oeste': neighboursEUO, 'América central': neighboursAmC}
    initialBattalions = {3 : 35, 4 : 30, 5 : 25, 6 : 20}
    battalionsPerContinent = {"América del norte" : 5, "Asia" : 7, "América del sur": 2, "Europa" : 5, "África" : 3, "Oceanía" : 2}
    extraBattalions = {1 : 4, 2 : 6, 3 : 8, 4 : 10, 5 : 15, 6 : 20, 7 : 25, 8 : 30, 9 : 35, 10 : 40, 11 : 45, 12 : 50, 13 : 55, 14 : 60 }

    def getcontientcolor (self, name):
        return self.tablecontinentcolors[name]
    def getcontinent (self, name):
        return self.tableContinents[str(name)]
