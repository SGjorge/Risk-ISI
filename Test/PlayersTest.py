import sys
sys.path.append("../Classes/Round/")

from Players import Players,HumanPlayers
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

	expectedNameEmpty = None
	expectedName = "Pepe"
	expectedBattalionsEmpty = 0
	expectedBattalions = 7
	expectedColourIdEmpty = None
	expectedColourId = "Orange"
	expectedSubclasses = ['HumanPlayers','IAPlayers']

	# Players
	global player
	global humanPlayer
	player = Players(expectedNameEmpty,expectedBattalionsEmpty,expectedColourIdEmpty)
	humanPlayer = HumanPlayers(expectedName,expectedBattalions,expectedColourId)

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

if __name__ == '__main__':
	unittest.main()
