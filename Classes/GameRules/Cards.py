# -*- coding: utf-8 -*-

import sys
sys.path.append("../")
from CoreVariables import CoreVariables as CV

class Cards:
    total = 2

    def __init__(self):
        self.name = "joker"

    def getname(self):
        return self.name

    def gettotal(self):
        return self.total

    def getcardstotal(self):
        return CV().cardsTotalNum


class Infantry(Cards):
    total = 14

    def __init__(self):
        self.name = "infantry"


class Chivalry(Cards):
    total = 14

    def __init__(self):
        self.name = "chivalry"


class Artillery(Cards):
    total = 14

    def __init__(self):
        self.name = "artillery"
