import sys
sys.path.append("../Classes/Round/")

from Players import Players,HumanPlayers
import unittest

class PlayersTest(unittest.TestCase):

	# expected values
	global expectedNameEmpty
	global expectedName
	global expectedBattalionsEmpty
	global expectedColourIdEmpty
	global expectedSubclasses

	expectedNameEmpty = None
	expectedName = "Pepe"
	expectedBattalionsEmpty = 0
	expectedColourIdEmpty = None
	expectedSubclasses = ['HumanPlayers','IAPlayers']

	# Players
	global player
	player = Players(expectedNameEmpty)

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

	def test_humanPlayerNameEmpty(self):
		self.assertEqual(expectedNameEmpty,HumanPlayers().getName())

	def test_humanPlayerBattalionsEmpty(self):
		self.assertEqual(expectedBattalionsEmpty,HumanPlayers().getBattalions())

	def test_humanPlayerColourIdEmpty(self):
		self.assertEqual(expectedColourIdEmpty,HumanPlayers().getColourId())

if __name__ == '__main__':
	unittest.main()
