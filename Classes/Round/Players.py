class Players:
	__NAME = None
	__BATTALIONS = 0
	__COLOURID = None

	def __init__(self,name,battalions,color):
		self.__NAME = name
		self.__BATTALIONS = battalions
		self.__COLOURID = color

	def getName(self):
		return self.__NAME

	def getBattalions(self):
		return self.__BATTALIONS

	def getColourId(self):
		return self.__COLOURID

	def toString(self):
		return (self.__NAME + " " + str(self.__BATTALIONS) + " " +self.__COLOURID)

# derivated class HumanPlayers
class HumanPlayers(Players):
	def __init__(self,name,battalions,color):
		super(self.__class__, self).__init__(name,battalions,color)

# derivated class IAPlayers
class IAPlayers(Players):
	def __init__(self,name,battalions,color):
		name = name + "IA"
		super(self.__class__, self).__init__(name,battalions,color)
