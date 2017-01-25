# -*- coding: utf-8 -*-

import sys
sys.path.append("../Classes/GameRules")
sys.path.append("../")
from Cards import Cards, Infantry, Chivalry, Artillery
from CoreVariables import CoreVariables as CV
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

    def test_totalnumberofcards(self):
        expected = CV().cardsTotalNum
        self.assertEqual(expected, Cards(None).getcardstotal())

    def test_totaljokers(self):
        expected = 2
        self.assertEqual(expected, Cards(None).gettotal())

    def test_totalinfantery(self):
        expected = 14
        self.assertEqual(expected, Infantry(None).gettotal())

    def test_totalchivalry(self):
        expected = 14
        self.assertEqual(expected, Chivalry(None).gettotal())

    def test_totalartillery(self):
        expected = 14
        self.assertEqual(expected, Artillery(None).gettotal())

    def test_jokername(self):
        player = Cards("joker")
        expected = "joker"
        self.assertEqual(expected, player.getname())

    def test_infantryname(self):
        player = Infantry("infantry")
        expected = "infantry"
        self.assertEqual(expected, player.getname())

    def test_chivalryname(self):
        player = Chivalry("chivalry")
        expected = "chivalry"
        self.assertEqual(expected, player.getname())

    def test_artilleryname(self):
        player = Artillery("artillery")
        expected = "artillery"
        self.assertEqual(expected, player.getname())



if __name__ == '__main__':
    unittest.main()
