class Players:
	__NAME = None
	__BATTALIONS = 0
	__COLOURID = None

	@classmethod
	def getName(self):
		return self.__NAME

	def getBattalions(self):
		return self.__BATTALIONS

	def getColourId(self):
		return self.__COLOURID

	def getChildrenClassesNames(self):


# derivated class HumanPlayers
class HumanPlayer(Players):

	def __init__(self,name):
		self.__NAME = name

# derivated class IAPlayers
class IAPlayer(Players):
	def __init__(self, name):
		self.name = name + "IA"
		
