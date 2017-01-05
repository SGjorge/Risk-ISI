#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

class CoreVariables():
    def __init__(self):
        self.countries = ["Alaska", "Territorio del noroeste", "Groenlandia",
            "Alberta", "Ontario", "Quebec", "Estados unidos del oeste", "Estados unidos del este",
            "América central", "Venezuela", "Brasil", "Perú", "Argentina",
            "África del norte", "Egipto", "África oriental", "Congo", "África del sur", "Madagascar"
            "Europa occidental", "Europa del norte", "Europa del sur", "Gran Bretaña",
            "Islandia", "Escandinavia", "Ucrania", "Oriente medio", "India", "Siam",
            "Afganistán", "China", "Ural", "Siberia", "Irkutsk", "Mongolia",
            "Yakutsk", "Kamchatka", "Japón", "Indonesia", "Nueva Guinea",
            "Australia occidental", "Australia oriental"]
        self.maxCountries = 42
        self.minPlayers = 3
        self.maxPlayers = 6
        self.colorPlayers = ["orange","red","blue","green","white","grey"]
    #tabla de colores de los continentes
    tablecontinentcolors = ['América del norte': 'yellow', 'América del sur': 'orange', 'Europa': 'blue', 'África': 'brown',
                        'Asia': 'green', 'Oceanía': 'grey']
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
    tableNeighbours = {'Europa del norte': neighboursEuropaNorte, 'Europa del sur': neighboursEuropaSur,
                        'Europa occidental': neighboursEuropaOcc, 'Gran Bretaña': neighboursGB,
                        'Islandia': neighboursIsl, 'Escandinavia': neighboursEsca, 'Ucrania': neighboursUck,
                        'Venezuela': neighboursVenz, 'Brasil': neighboursBra, 'Perú': neighboursPeru,
                        'Argentina': neighboursArg, 'África del norte' : neighboursAN, 'Egipto': neighboursEgip,
                        'África oriental': neighboursAO, 'Madagascar': neighboursMAD, 'África del sur': neighboursAS,
                        'Congo': neighboursCon, 'Indonesia': neighboursIND, 'Nueva Guinea': neighboursNG,
                        'Australia oriental': neighboursAOriental, 'Australia occidental': neighboursAOcc}

    def getneighbours (self, name):
        return self.tableNeighbours[name]
    def getcontientcolor (self, name):
        return self.tablecontinentcolors[name]
