# -*- coding: utf-8 -*-

import sys
sys.path.append("../")

class Cards:
    name = "joker"

    def __init__(self,name):
        self.name = name

    def getname(self):
        return self.name

class Infantry(Cards):
    name = "infantery"

class Chivalry(Cards):
    name = "chivalry"

class Artillery(Cards):
    name = "artillery"
