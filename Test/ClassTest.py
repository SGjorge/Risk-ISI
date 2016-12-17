import sys
sys.path.append("../Classes/Game/")

#from Game import Game
#from Countries import Countries
from Players import Players
import unittest

class ClassTest(unittest.TestCase):

	def testplayersclass(self):

		# expected values
		expectedName = None
		expectedBattalions = 0
		expectedColourId = None
		expectedSubclasses = ['HumanPlayer','IAPlayer']

		# checking
		self.assertEqual(expectedName,Players().getName())
		self.assertEqual(expectedBattalions,Players().getBattalions())
		self.assertEqual(expectedColourId,Players().getColourId())
		for (cls,scls) in zip(globals()['Players'].__subclasses__(),expectedSubclasses):
			self.assertEqual(cls.__name__,scls)

	def testcountriesclass(self):
		self.assertEqual(0,0)

	def testgameclass(self):
		self.assertEqual(0,0)
		

if __name__ == '__main__':
    unittest.main()