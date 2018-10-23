class File:
	def __init__(self,name):
		self.name = name
		self.change = Change()
		self.tracked = False
		self.source = ""


	def markTracked(self):
		self.tracked = True


	def dismarkTracked(self):
		self.tracked = False
		self.change.dismarkStaged()


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


	def modify(self, modifications):
		self.source = modifications
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


class FileManager:
	def __init__(self):
		self.files = {}

	def createFile(self, name):
		file = File(name)
		self.files.update({name:file})
		return "File created: " + name

	def delFile(self, name):
		if name in self.files:
			del self.files[name]


	def modify(self, name, modifications):
		if name in self.files:
			self.files[name].modify(modifications)


	def getFile(self, name):
		if name in self.files:
			return self.files[name]
		else:
			return None
