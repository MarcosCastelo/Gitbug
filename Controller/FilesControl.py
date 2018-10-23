class File:
	def __init__(self,name):
		self.name = name
		self.change = Change()
		self.tracked = False


	def markTracked(self):
		self.tracked = True


	def dismarkTracked(self):
		self.tracked = False


	def getName(self):
		return self.name


	def getTrack(self):
		return self.tracked


	def getStage(self):
		return self.change.getStage()


	def add(self):
		self.markTracked()
		self.change.markStaged()


	def remove(self):
		self.dismarkTracked()
		self.change.dismarkStaged()


	def modify(self):
		self.staged.dismarkStaged()


class Change:
	def __init__(self):
		self.staged = False


	def getStage(self):
		return self.staged



	def markStaged(self):
		self.staged = True


	def dismarkStaged(self):
		self.staged = False



