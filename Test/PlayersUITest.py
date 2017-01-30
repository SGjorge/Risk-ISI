import sys
sys.path.append("../Classes/Round/")

from Players import HumanPlayers
import unittest

class PlayersUITest(unittest.TestCase):

	def test_whoattack(self):
		p1 = HumanPlayers("Pepe",0,"orange",[])
		print("Si no se introduce 'España' fallará el test")
		countryToAttack = p1.whoattack()
		self.assertEqual(countryToAttack,"España")

	def test_howmanyattack(self):
		p1 = HumanPlayers("Pepe",0,"orange",[])
		print("Si no se introduce '3' fallará el test")
		battalionsToAttack = p1.howmanyattack()
		self.assertEqual(battalionsToAttack,str(3))

	def test_howmanydeffend(self):
		p1 = HumanPlayers("Pepe",0,"orange",[])
		print("Si no se introduce '1' fallará el test")
		battalionsToDeffend = p1.howmanydeffend()
		self.assertEqual(battalionsToDeffend,str(1))

if __name__ == '__main__':
	unittest.main()