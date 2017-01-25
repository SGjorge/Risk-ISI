#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../")
sys.path.append("../Classes/Round")

from CoreVariables import CoreVariables
from Countries import Countries, Country, Neighbours, World, Continent
from Players import IAPlayers
import unittest

class IATest(unittest.TestCase):
    def test_abletoattack(self):
        expected = False
        playerAux = IAPlayers("prueba", 5, "blue")
        self.assertEqual(expected, playerAux.attack("Europa"))


if __name__ == '__main__':
    unittest.main()
