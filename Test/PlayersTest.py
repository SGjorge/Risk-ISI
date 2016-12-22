import sys
sys.path.append("../Classes/Round/")

from Players import Players,HumanPlayers
import unittest

class PlayersTest(unittest.TestCase):

	# expected values
	global expectedName
	global expectedBattalions
	global expectedColourId
	global expectedSubclasses

	expectedName = None
	expectedBattalions = 0
	expectedColourId = None
	expectedSubclasses = ['HumanPlayers','IAPlayers']

	#testing
	def test_getName(self):
		self.assertEqual(expectedName,Players().getName())

	def test_getBattalion(self):
		self.assertEqual(expectedBattalions,Players().getBattalions())

	def test_getColourId(self):
		self.assertEqual(expectedColourId,Players().getColourId())

	def test_Subclasses(self):
		for (cls,scls) in zip(globals()['Players'].__subclasses__(),expectedSubclasses):
			self.assertEqual(cls.__name__,scls)

	def test_humanPlayerName(self):
		self.assertEqual(expectedName,HumanPlayers().getName())

	def test_humanPlayerBattalions(self):
		self.assertEqual(expectedBattalions,HumanPlayers().getBattalions())

	def test_humanPlayerColourId(self):
		self.assertEqual(expectedColourId,HumanPlayers().getColourId())

if __name__ == '__main__':
	unittest.main()
