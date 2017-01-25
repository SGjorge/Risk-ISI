#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../")
sys.path.append("../Classes/Round")

from CoreVariables import CoreVariables
from Countries import Countries, Country, Neighbours, World, Continent
import unittest

class IATest(unittest.TestCase):
    def test_abletoattack(self):
        expected = True
        playerAux = IAPlayers("prueba", 5, "blue")
        self.assertEqual(expected, playerAux.attack())
