# -*- coding: utf-8 -*-

import sys
sys.path.append("../")
from CoreVariables import CoreVariables as CV

class Cards:
    def __init__(self):
        self.name = "joker"

    def getname(self):
        return self.name

    def gettotal(self):
        return self.total

    def getcardstotal(self):
        return CV().cardsTotalNum


class Infantry(Cards):
    def __init__(self):
        self.name = "infantry"


class Chivalry(Cards):
    def __init__(self):
        self.name = "chivalry"


class Artillery(Cards):
    def __init__(self):
        self.name = "artillery"
