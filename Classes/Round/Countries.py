import sys


class Countries(object):

    def __init__(self, arg):
        self.name = None

    paises = ["Europa Occidental", "Europa del sur", "Europa del norte"]

    def nameok (self, name):
        if (name in paises):
            return True;
        else:
            return False;
