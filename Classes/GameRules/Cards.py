# -*- coding: utf-8 -*-

import sys
sys.path.append("../")
from CoreVariables import CoreVariables as CV

class Cards:
    name = "joker"
    total = 2

    def __init__(self,name):
        self.name = name

    def getname(self):
        return self.name

    def gettotal(self):
        return self.total

    def getcardstotal(self):
        return CV().cardsTotalNum

class Infantry(Cards):
    name = "infantery"
    total = 14

class Chivalry(Cards):
    name = "chivalry"
    total = 14

class Artillery(Cards):
    name = "artillery"
    total = 14
