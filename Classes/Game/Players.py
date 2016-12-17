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