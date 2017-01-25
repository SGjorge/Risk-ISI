import sys
sys.path.append("../Classes/Round/")
sys.path.append("../Classes/GameRules")

from Players import Players,HumanPlayers,IAPlayers,ArrayPlayers
from Countries import Country
from Cards import Cards, Infantry, Chivalry, Artillery
import unittest

class PlayersTest(unittest.TestCase):

	# expected values
	global expectedNameEmpty
	global expectedName
	global expectedBattalionsEmpty
	global expectedBattalions
	global expectedColourIdEmpty
	global expectedColourId
	global expectedCardsEmpty
	global expectedCards
	global expectedCardsEmptyNum
	global expectedCardsNum
	global expectedSubclasses
	global numPlayers

	expectedNameEmpty = None
	expectedName = "Pepe"
	expectedBattalionsEmpty = 0
	expectedBattalions = 7
	expectedColourIdEmpty = None
	expectedColourId = "Orange"
	expectedCardsEmpty = []
	expectedCards = [Cards(),Infantry(),Chivalry(),Artillery()]
	expectedCardsEmptyNum = 0
	expectedCardsNum = 4
	expectedSubclasses = ['HumanPlayers','IAPlayers']
	numPlayers = 3

	# Players
	global player
	global humanPlayer
	global iaPlayer
	global arrayPlayer
	global p1
	global p2
	global p3

	player = Players(expectedNameEmpty,expectedBattalionsEmpty,expectedColourIdEmpty,expectedCardsEmpty)
	humanPlayer = HumanPlayers(expectedName,expectedBattalions,expectedColourId,expectedCards)
	iaPlayer = IAPlayers(expectedName,expectedBattalions,expectedColourId,expectedCards)
	arrayPlayer = ArrayPlayers()
	p1 = HumanPlayers("Pepe",0,"orange",[])
	p2 = HumanPlayers("Ana",0,"red",[])
	p3 = HumanPlayers("Yo",0,"blue",[])

	#testing
	def test_getname(self):
		self.assertEqual(expectedNameEmpty,player.getname())

	def test_getbattalion(self):
		self.assertEqual(expectedBattalionsEmpty,player.getbattalions())

	def test_getcolourid(self):
		self.assertEqual(expectedColourIdEmpty,player.getcolourid())

	def test_getcards(self):
		self.assertEqual(expectedCardsEmpty,player.getcards())

	def test_getcardsnumber(self):
		self.assertEqual(expectedCardsEmptyNum,player.getcardsnumber())

	def test_subclasses(self):
		for (cls,scls) in zip(globals()['Players'].__subclasses__(),expectedSubclasses):
			self.assertEqual(cls.__name__,scls)

	def test_humanplayername(self):
		self.assertEqual(expectedName,humanPlayer.getname())

	def test_humanplayerbattalions(self):
		self.assertEqual(expectedBattalions,humanPlayer.getbattalions())

	def test_humanplayercolourid(self):
		self.assertEqual(expectedColourId,humanPlayer.getcolourid())

	def test_humanplayercards(self):
		self.assertEqual(expectedCards,humanPlayer.getcards())

	def test_humancardsnumber(self):
		self.assertEqual(expectedCardsNum,humanPlayer.getcardsnumber())

	def test_iaplayername(self):
		iaName = expectedName+"IA"
		self.assertEqual(iaName,iaPlayer.getname())

	def test_iaplayerbattalions(self):
		self.assertEqual(expectedBattalions,iaPlayer.getbattalions())

	def test_iaplayercolourid(self):
		self.assertEqual(expectedColourId,iaPlayer.getcolourid())

	def test_iaplayercards(self):
		self.assertEqual(expectedCards,iaPlayer.getcards())

	def test_compareplayers(self):
		self.assertEqual(True,humanPlayer.isequal(humanPlayer))
		self.assertEqual(False,humanPlayer.isequal(iaPlayer))

	def test_arrayplayerorderfisrt(self):
		players = [p1,p2,p3]
		nplayers = ArrayPlayers().orderplayers(players,p1)
		self.assertEqual(True,nplayers[0].isequal(p1))
		self.assertEqual(True,nplayers[1].isequal(p2))
		self.assertEqual(True,nplayers[2].isequal(p3))

	def test_arrayplayerorderlast(self):
		players = [p1,p2,p3]
		nplayers = ArrayPlayers().orderplayers(players,p3)
		self.assertEqual(True,nplayers[0].isequal(p3))
		self.assertEqual(True,nplayers[1].isequal(p2))
		self.assertEqual(True,nplayers[2].isequal(p1))

	def test_arrayplayerordermiddle(self):
		players = [p1,p2,p3]
		nplayers = ArrayPlayers().orderplayers(players,p2)
		self.assertEqual(True,nplayers[0].isequal(p2))
		self.assertEqual(True,nplayers[1].isequal(p1))
		self.assertEqual(True,nplayers[2].isequal(p3))

	def test_turndiceroll(self):
		roll = p1.diceroll()
		self.assertIn(roll,range(1,7))

	def test_agroupofrolls(self):
		rolls = p1.rolls(2)
		for roll in rolls:
			self.assertIn(roll,range(1,7))

	def test_addconqueredcountry(self):
		country = Country("España",p1.getname())
		p1.addconqueredcountry(country)
		conqueredCountries = p1.getconqueredcountries()
		for c in conqueredCountries:
			self.assertEqual(c.getname(),country.getname())

	def test_usedbattalions(self):
		paux = HumanPlayers("Pepe",35,"orange",[])
		country1 = Country("España",paux.getname())
		country2 = Country("Francia",paux.getname())
		country3 = Country("Italia",paux.getname())
		country1.changebattalions(7)
		country2.changebattalions(1)
		country3.changebattalions(5)
		paux.addconqueredcountry(country1)
		paux.addconqueredcountry(country2)
		paux.addconqueredcountry(country3)
		self.assertEqual(paux.getusedbattalions(),13)

	def test_distributebattalions(self):
		paux = HumanPlayers("Pepe",35,"orange",[])
		country1 = Country("España",paux.getname())
		country2 = Country("Francia",paux.getname())
		country3 = Country("Italia",paux.getname())
		country1.changebattalions(7)
		country2.changebattalions(1)
		country3.changebattalions(5)
		paux.addconqueredcountry(country1)
		paux.addconqueredcountry(country2)
		paux.addconqueredcountry(country3)
		paux.distributebatallions()
		self.assertEqual(paux.getusedbattalions(),35)
		conqueredCountries = paux.getconqueredcountries()
		self.assertEqual(conqueredCountries[0].tostring(),"España 15:Pepe")
		self.assertEqual(conqueredCountries[1].tostring(),"Francia 8:Pepe")
		self.assertEqual(conqueredCountries[2].tostring(),"Italia 12:Pepe")




if __name__ == '__main__':
	unittest.main()
