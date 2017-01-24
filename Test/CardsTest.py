# -*- coding: utf-8 -*-

import sys
sys.path.append("../Classes/GameRules")
from Cards import Cards, Infantry, Chivalry, Artillery
import unittest

class CardsTest(unittest.TestCase):

    def test_jokercard (self):
        expected = None
        self.assertEqual(expected, Cards(None).name)

    def test_infantrycard (self):
        expected = None
        self.assertEqual(expected, Infantry(None).name)

    def test_chivalrycard (self):
        expected = None
        self.assertEqual(expected, Chivalry(None).name)

    def test_artillerycard (self):
        expected = None
        self.assertEqual(expected, Artillery(None).name)


if __name__ == '__main__':
    unittest.main()
