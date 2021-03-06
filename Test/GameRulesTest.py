# -*- coding: utf-8 -*-
import sys
import unittest

sys.path.append("../Classes/GameRules/")
sys.path.append("../Classes/Round/")
sys.path.append("../")

from GameRules import GameRules
from Cards import Cards, Infantry, Chivalry, Artillery
from Countries import Countries, Country, Neighbours
from Players import Players, HumanPlayers, IAPlayers
from CoreVariables import CoreVariables as CV



class GameRulesTest(unittest.TestCase):


        #Checks if the number of players is ok (3-6)
    def test_is1playerok(self):
        expected = False
        self.assertEqual(expected, GameRules.numberofplayersok(1))

    def test_are5playersok(self):
        expected = True
        self.assertEqual(expected, GameRules.numberofplayersok(5))

    def test_are7playersok(self):
        expected = False
        self.assertEqual(expected, GameRules.numberofplayersok(7))

        #Checks the number of initial battalions per player, based on the total number of players
    def test_initialbattalionsfor3players(self):
        expected = 35
        self.assertEqual(expected, GameRules.getinitialbattalions(3))

    def test_initialbattalionsfor4players(self):
        expected = 30
        self.assertEqual(expected, GameRules.getinitialbattalions(4))

    def test_initialbattalionsfor5players(self):
        expected = 25
        self.assertEqual(expected, GameRules.getinitialbattalions(5))

    def test_initialbattalionsfor6players(self):
        expected = 20
        self.assertEqual(expected, GameRules.getinitialbattalions(6))

        #Checks the number of extra battalions per each whole conquered continent
    def test_battalionsperamericaN(self):
        expected = 5
        self.assertEqual(expected, GameRules.getbattalionspercontinent("América del norte"))

    def test_battalionsperasia(self):
        expected = 7
        self.assertEqual(expected, GameRules.getbattalionspercontinent("Asia"))

    def test_battalionsperamericaS(self):
        expected = 2
        self.assertEqual(expected, GameRules.getbattalionspercontinent("América del sur"))

    def test_battalionspereuropa(self):
        expected = 5
        self.assertEqual(expected, GameRules.getbattalionspercontinent("Europa"))

    def test_battalionsperafrica(self):
        expected = 3
        self.assertEqual(expected, GameRules.getbattalionspercontinent("África"))

    def test_battalionsperoceania(self):
        expected = 2
        self.assertEqual(expected, GameRules.getbattalionspercontinent("Oceanía"))

        #Checks the number of extra battalions per conquered contries
    def test_battalionsper12countries(self):
        expected = 4
        self.assertEqual(expected, GameRules.getbattalionspercountries(12))

    def test_battalionsper2countries(self):
        expected = 3
        self.assertEqual(expected, GameRules.getbattalionspercountries(2))

    def test_battalionsper37countries(self):
        expected = 12
        self.assertEqual(expected, GameRules.getbattalionspercountries(37))


        #Checks if the number of battalions is ok to attack
    def test_is1battaliontoattackok(self):
        pAux = Players("Pepe",0,"orange",[])
        country = Country("Islandia",pAux)
        country.changebattalions(25) #25 battalions
        expected = True
        self.assertEqual(expected, GameRules.battalionstoattackok(country,1))

    def test_are2battalionstoattackok(self):
        pAux = Players("Pepe",0,"orange",[])
        country = Country("Islandia",pAux)
        country.changebattalions(25) #25 battalions
        expected = True
        self.assertEqual(expected, GameRules.battalionstoattackok(country,2))

    def test_are3battalionstoattackok(self):
        pAux = Players("Pepe",0,"orange",[])
        country = Country("Islandia",pAux)
        country.changebattalions(25) #25 battalions
        expected = True
        self.assertEqual(expected, GameRules.battalionstoattackok(country,3))

    def test_are4battalionstoattackok(self):
        pAux = Players("Pepe",0,"orange",[])
        country = Country("Islandia",pAux)
        country.changebattalions(25) #25 battalions
        expected = False
        self.assertEqual(expected, GameRules.battalionstoattackok(country,4))

    def test_is1battalionoktoattack(self):
        pAux = Players("Pepe",0,"orange",[])
        country = Country("Islandia",pAux)
        country.changebattalions(2) #2 battalions
        expected = True
        self.assertEqual(expected, GameRules.battalionstoattackok(country,1))

    def test_are2battalionsoktoattack(self):
        pAux = Players("Pepe",0,"orange",[])
        country = Country("Islandia",pAux)
        country.changebattalions(2) #2 battalions
        expected = False
        self.assertEqual(expected, GameRules.battalionstoattackok(country,2))

        #Checks if the number of battalions is ok to defend
    def test_is1battaliontodefendok(self):
        pAux = Players("Pepe",0,"orange",[])
        country = Country("Groenlandia",pAux)
        country.changebattalions(4) #4 battalions
        expected = True
        self.assertEqual(expected, GameRules.battalionstodefendok(country,1))

    def test_are2battalionstodefendok(self):
        pAux = Players("Pepe",0,"orange",[])
        country = Country("Groenlandia",pAux)
        country.changebattalions(2) #2 battalions
        expected = True
        self.assertEqual(expected, GameRules.battalionstodefendok(country,2))

    def test_are3battalionstodefendok(self):
        pAux = Players("Pepe",0,"orange",[])
        country = Country("Groenlandia",pAux)
        country.changebattalions(8) #8 battalions
        expected = False
        self.assertEqual(expected, GameRules.battalionstodefendok(country,3))

    def test_are2battalionsoktodefend(self):
        pAux = Players("Pepe",0,"orange",[])
        country = Country("Groenlandia",pAux)
        country.changebattalions(1) #1 battalion
        expected = False
        self.assertEqual(expected, GameRules.battalionstodefendok(country,2))

    def test_are0battalionstodefendok(self):
        pAux = Players("Pepe",0,"orange",[])
        country = Country("Groenlandia",pAux)
        country.changebattalions(1) #1 battalion
        expected = False
        self.assertEqual(expected, GameRules.battalionstodefendok(country,0))


        #Checks if a battle can happen between two countries
    def test_canislandattackgroenland(self):
        pAux1 = Players("Pepe",0,"orange",[])
        pAux2 = Players("Nerea",0,"blue",[])
        countryAtt = Country("Islandia",pAux1)
        countryDef = Country("Groenlandia",pAux2)
        expected = True
        self.assertEqual(expected,GameRules.countriesokforthebattle(countryAtt,countryDef))

    def test_canislandattackbrazil(self):
        pAux1 = Players("Pepe",0,"orange",[])
        pAux2 = Players("Nerea",0,"blue",[])
        countryAtt = Country("Islandia",pAux1)
        countryDef = Country("Brasil",pAux2)
        expected = False
        self.assertEqual(expected,GameRules.countriesokforthebattle(countryAtt,countryDef))

    def test_canredattackred(self):
        pAux1 = Players("Pepe",0,"orange",[])
        countryAtt = Country("Islandia",pAux1)
        countryDef = Country("Groenlandia",pAux1)
        expected = False
        self.assertEqual(expected,GameRules.countriesokforthebattle(countryAtt,countryDef))


        #Checks the number of extra battalions per card exchange
    def test_firstcardexchange(self):
        expected = 4
        self.assertEqual(expected,GameRules.getextrabattalions(1))

    def test_secondcardexchange(self):
        expected = 6
        self.assertEqual(expected,GameRules.getextrabattalions(2))

    def test_thirdcardexchange(self):
        expected = 8
        self.assertEqual(expected,GameRules.getextrabattalions(3))

    def test_fourthcardexchange(self):
        expected = 10
        self.assertEqual(expected,GameRules.getextrabattalions(4))

    def test_ninthcardexchange(self):
        expected = 35
        self.assertEqual(expected,GameRules.getextrabattalions(9))

    def test_14thcardexchange(self):
        expected = 60
        self.assertEqual(expected,GameRules.getextrabattalions(14))

    def test_lastcardexchange(self):
        expected = 60
        self.assertEqual(expected,GameRules.getextrabattalions(37))


        #Checks the number of battalions that loses the attacking player
    def test_firstbattle(self):
        rollsAtt = [5,5]
        rollsDef = [6,6]
        expected = [1,1]
        self.assertEqual(expected,GameRules.getlostbattalions(rollsAtt,rollsDef))

    def test_secondbattle(self):
        rollsAtt = [6,6]
        rollsDef = [5,5]
        expected = [0,0]
        self.assertEqual(expected,GameRules.getlostbattalions(rollsAtt,rollsDef))

    def test_thirdbattle(self):
        rollsAtt = [6,6]
        rollsDef = [5,6]
        expected = [1,0]
        self.assertEqual(expected,GameRules.getlostbattalions(rollsAtt,rollsDef))

    def test_fourthbattle(self):
        rollsAtt = [3,5,4]
        rollsDef = [6,5]
        expected = [1,1]
        self.assertEqual(expected,GameRules.getlostbattalions(rollsAtt,rollsDef))

    def test_fifthbattle(self):
        rollsAtt = [4,4,4]
        rollsDef = [3]
        expected = [0]
        self.assertEqual(expected,GameRules.getlostbattalions(rollsAtt,rollsDef))

    def test_sixthbattle(self):
        rollsAtt = [5,5,5]
        rollsDef = [6]
        expected = [1]
        self.assertEqual(expected,GameRules.getlostbattalions(rollsAtt,rollsDef))

    def test_seventhbattle(self):
        rollsAtt = [2]
        rollsDef = [5,4,3]
        expected = [1]
        self.assertEqual(expected,GameRules.getlostbattalions(rollsAtt,rollsDef))

    def test_eighthbattle(self):
        rollsAtt = [6]
        rollsDef = [5,4,3]
        expected = [0]
        self.assertEqual(expected,GameRules.getlostbattalions(rollsAtt,rollsDef))


        #checks if the number of cards per player is ok (< 5)
        #must be checked right at the very end of the turn.
    def test_zerocardsok(self):
        player = HumanPlayers("Pepe",0,"orange",[])
        expected = True
        self.assertEqual(expected,GameRules.checkcardsnum(player))

    def test_fourcardsok(self):
        cards = [Cards(),Infantry(),Chivalry(),Artillery()]
        player = HumanPlayers("Pepe",0,"orange",cards)
        expected = True
        self.assertEqual(expected,GameRules.checkcardsnum(player))

    def test_sixcardsok(self):
        cards = [Cards(),Infantry(),Chivalry(),Artillery(),Cards(),Infantry()]
        player = IAPlayers("Pepe",0,"orange",cards)
        expected = False
        self.assertEqual(expected,GameRules.checkcardsnum(player))


        #checks if the player has three cards of the type chosen, to exchange per extra battalions
    def test_threeinfantryexchange(self):
        cards = [Cards(),Infantry(),Chivalry(),Artillery(),Cards(),Infantry()]
        player = IAPlayers("Pepe",0,"orange",cards)
        expected = True
        self.assertEqual(expected,GameRules.cardstoexchangeok(player,"infantry"))

    def test_threechivalryexchange(self):
        cards = [Cards(),Infantry(),Chivalry(),Artillery(),Cards(),Infantry()]
        player = IAPlayers("Pepe",0,"orange",cards)
        expected = True
        self.assertEqual(expected,GameRules.cardstoexchangeok(player,"chivalry"))

    def test_threeartilleryexchange(self):
        cards = [Cards(),Infantry(),Chivalry(),Artillery(),Infantry()]
        player = IAPlayers("Pepe",0,"orange",cards)
        expected = False
        self.assertEqual(expected,GameRules.cardstoexchangeok(player,"artillery"))


        #checks if the battalion movement between two counries of a player is ok
    def test_movebattalions1(self):
        player = HumanPlayers("Pepe",10,"Orange",[])
        origCountry = Country("Europa del norte",player)
        origCountry.changebattalions(10)
        player.addconqueredcountry(origCountry)
        destCountry = Country("Europa del sur",player)
        player.addconqueredcountry(destCountry)
        numBattalions = 5
        expected = True #vecinos directos
        self.assertEqual(expected,GameRules.movebattalions(player,origCountry,destCountry,numBattalions))

    def test_movebattalions2(self):
        player = HumanPlayers("Pepe",5,"orange",[])
        origCountry = Country("Europa del norte",player)
        destCountry = Country("Europa del sur",player)
        player.addconqueredcountry(origCountry)
        player.addconqueredcountry(destCountry)
        origCountry.changebattalions(5)
        numBattalions = 5
        expected = False #Numero tropas incorrecto
        self.assertEqual(expected,GameRules.movebattalions(player,origCountry,destCountry,numBattalions))

    def test_movebattalions3(self):
        player = HumanPlayers("Pepe",38,"orange",[])
        origCountry = Country("Europa del norte",player)
        otherCountry = Country("Europa del sur",player)
        player.addconqueredcountry(origCountry)
        player.addconqueredcountry(otherCountry)
        origCountry.changebattalions(5)
        player2 = HumanPlayers("Nerea",38,"red",[])
        destCountry = Country("Islandia",player2)
        numBattalions = 1
        expected = False #no son vecinos ni hay camino
        self.assertEqual(expected,GameRules.movebattalions(player,origCountry,destCountry,numBattalions))

    def test_movebattalions4(self):
        player = HumanPlayers("Pepe",38,"orange",[])
        origCountry = Country("Europa del norte",player)
        otherCountry = Country("Europa del sur",player)
        destCountry = Country("África del norte",player)
        player.addconqueredcountry(origCountry)
        player.addconqueredcountry(otherCountry)
        player.addconqueredcountry(destCountry)
        origCountry.changebattalions(5)
        numBattalions = 1
        expected = True #no vecinos directos pero sí hay camino
        self.assertEqual(expected,GameRules.movebattalions(player,origCountry,destCountry,numBattalions))

    def test_movebattalions5(self):
        player = HumanPlayers("Pepe",38,"orange",[])
        origCountry = Country("Europa del norte",player)
        otherCountry = Country("Europa del sur",player)
        anotherCountry = Country("África del norte",player)
        destCountry = Country("Brasil",player)
        player.addconqueredcountry(origCountry)
        player.addconqueredcountry(otherCountry)
        player.addconqueredcountry(anotherCountry)
        player.addconqueredcountry(destCountry)
        origCountry.changebattalions(5)
        numBattalions = 1
        expected = True #hay camino entre vecinos
        self.assertEqual(expected,GameRules.movebattalions(player,origCountry,destCountry,numBattalions))



if __name__ == '__main__':
    unittest.main()
