from ../Classes/Game/Game import Game
from ../Classes/Game/Game import Players
from ../Classes/Game/Game import Countries
import unittest

class ClassTest(unittest.TestCase):

	def testplayersclass(self):
		# player object
		player = Players.newplayer()

		# expected values
		expectedName = None
		expectedBattalions = 0
		expectedIdColour = None

		# checking
		self.assertEqual(expectedName,player.getName())
		self.assertEqual(expectedBattalions,player.getBattalions())
		self.assertEqual(expectedIdColour,player.getIdColour())

	def testcountriesclass(self):

	def testgameclass(self):
		#game = Game().newgame()
		

if __name__ == '__main__':
    unittest.main()