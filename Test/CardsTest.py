# -*- coding: utf-8 -*-

import sys
sys.path.append("../Classes/GameRules")
sys.path.append("../")
from Cards import Cards, Infantry, Chivalry, Artillery
from CoreVariables import CoreVariables as CV
import unittest

class CardsTest(unittest.TestCase):

        #checks the number of cards for every type
    def test_totaljokers(self):
        expected = 2
        self.assertEqual(expected, CV().maxJokers)

    def test_totalinfantery(self):
        expected = 14
        self.assertEqual(expected, CV().maxInfantry)

    def test_totalchivalry(self):
        expected = 14
        self.assertEqual(expected, CV().maxChivalry)

    def test_totalartillery(self):
        expected = 14
        self.assertEqual(expected, CV().maxArtillery)


        #checks the name of every type of card
    def test_jokername(self):
        card = Cards()
        expected = "joker"
        self.assertEqual(expected, card.getname())

    def test_infantryname(self):
        card = Infantry()
        expected = "infantry"
        self.assertEqual(expected, card.getname())

    def test_chivalryname(self):
        card = Chivalry()
        expected = "chivalry"
        self.assertEqual(expected, card.getname())

    def test_artilleryname(self):
        card = Artillery()
        expected = "artillery"
        self.assertEqual(expected, card.getname())


        #checks the total number of cards
    def test_totalnumberofcards(self):
        expected = CV().cardsTotalNum
        self.assertEqual(expected, Cards().getcardstotal())




if __name__ == '__main__':
    unittest.main()
