class File:
	def __init__(self,name, change):
		self.name = name
		self.change = change
		self.tracked = False


	def markTracked(self):
		self.tracked = True


	def dismarkTracked(self):
		self.tracked = False


	def getName(self):
		name, ext = self.name.split(".")
		return name,ext


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



