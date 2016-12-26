import sys
sys.path.append("../Classes/Round/")

from Players import Players,HumanPlayers,IAPlayers,ArrayPlayers
import unittest

class PlayersTest(unittest.TestCase):

	# expected values
	global expectedNameEmpty
	global expectedName
	global expectedBattalionsEmpty
	global expectedBattalions
	global expectedColourIdEmpty
	global expectedColourId
	global expectedSubclasses
	global numPlayers

	expectedNameEmpty = None
	expectedName = "Pepe"
	expectedBattalionsEmpty = 0
	expectedBattalions = 7
	expectedColourIdEmpty = None
	expectedColourId = "Orange"
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

	player = Players(expectedNameEmpty,expectedBattalionsEmpty,expectedColourIdEmpty)
	humanPlayer = HumanPlayers(expectedName,expectedBattalions,expectedColourId)
	iaPlayer = IAPlayers(expectedName,expectedBattalions,expectedColourId)
	arrayPlayer = ArrayPlayers()
	p1 = HumanPlayers("Pepe",0,"orange")
	p2 = HumanPlayers("Ana",0,"red")
	p3 = HumanPlayers("Yo",0,"blue")

	#testing
	def test_getName(self):
		self.assertEqual(expectedNameEmpty,player.getName())

	def test_getBattalion(self):
		self.assertEqual(expectedBattalionsEmpty,player.getBattalions())

	def test_getColourId(self):
		self.assertEqual(expectedColourIdEmpty,player.getColourId())

	def test_Subclasses(self):
		for (cls,scls) in zip(globals()['Players'].__subclasses__(),expectedSubclasses):
			self.assertEqual(cls.__name__,scls)

	def test_humanPlayerName(self):
		self.assertEqual(expectedName,humanPlayer.getName())

	def test_humanPlayerBattalions(self):
		self.assertEqual(expectedBattalions,humanPlayer.getBattalions())

	def test_humanPlayerColourId(self):
		self.assertEqual(expectedColourId,humanPlayer.getColourId())

	def test_iaPlayerName(self):
		iaName = expectedName+"IA"
		self.assertEqual(iaName,iaPlayer.getName())

	def test_iaPlayerBattalions(self):
		self.assertEqual(expectedBattalions,iaPlayer.getBattalions())

	def test_iaPlayerColourId(self):
		self.assertEqual(expectedColourId,iaPlayer.getColourId())

	def test_comparePlayers(self):
		self.assertEqual(True,humanPlayer.isEqual(humanPlayer))
		self.assertEqual(False,humanPlayer.isEqual(iaPlayer))

	def test_arrayPlayerorderFisrt(self):
		players = [p1,p2,p3]
		nplayers = ArrayPlayers().orderPlayers(players,p1)
		self.assertEqual(True,nplayers[0].isEqual(p1))
		self.assertEqual(True,nplayers[1].isEqual(p2))
		self.assertEqual(True,nplayers[2].isEqual(p3))

	def test_arrayPlayerorderLast(self):
		players = [p1,p2,p3]
		nplayers = ArrayPlayers().orderPlayers(players,p3)
		self.assertEqual(True,nplayers[0].isEqual(p3))
		self.assertEqual(True,nplayers[1].isEqual(p2))
		self.assertEqual(True,nplayers[2].isEqual(p1))

	def test_arrayPlayerorderMiddle(self):
		players = [p1,p2,p3]
		nplayers = ArrayPlayers().orderPlayers(players,p2)
		self.assertEqual(True,nplayers[0].isEqual(p2))
		self.assertEqual(True,nplayers[1].isEqual(p1))
		self.assertEqual(True,nplayers[2].isEqual(p3))

	def test_turnCubeRoll(self):
		roll = p1.cubeRoll()
		self.assertIn(roll,range(1,7))

	def test_assaultRoll(self):
		self.assertEqual(True,True)

	def test_defendRoll(self):
		defendRoll = p1.defendRoll(2)
		for i in defendRoll:
			self.assertIn(i,range(1,7))

if __name__ == '__main__':
	unittest.main()
