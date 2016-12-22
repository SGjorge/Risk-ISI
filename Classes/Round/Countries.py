import sys
from CoreVariables import CoreVariables

class Countries(object):

    global absolutes

    def __init__(self):
        self.name = None

    absolutes = CoreVariables()

    def nameok (self, name):
        if (name in absolutes.paises):
            return True;
        else:
            return False;
