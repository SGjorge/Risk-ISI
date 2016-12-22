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

# derivated class HumanPlayers
class HumanPlayers(Players):
	def __init__(self):
		None

# derivated class IAPlayers
class IAPlayers(Players):
	def __init__(self, name):
		self.name = name + "IA"
