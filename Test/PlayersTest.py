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

	player = Players(expectedNameEmpty,expectedBattalionsEmpty,expectedColourIdEmpty)
	humanPlayer = HumanPlayers(expectedName,expectedBattalions,expectedColourId)
	iaPlayer = IAPlayers(expectedName,expectedBattalions,expectedColourId)
	arrayPlayer = ArrayPlayers(numPlayers)

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

	def test_arrayPlayerBuilder(self):
		for i in range(1,len(arrayPlayer)):
			self.assertEqual(None,i)

	def test_arrayPlayerLen(self):
		self.assertEqual(numPlayers,len(arrayPlayer))

if __name__ == '__main__':
	unittest.main()
