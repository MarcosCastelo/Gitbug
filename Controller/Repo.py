from . import Useful
import random
class Commit:
	def __init__(self, date, info):
		self.commitedFiles = {}
		self.date = str(date)
		id = random.randint(1000, 9999)
		self.code = Useful.encrypt(str(id)+self.date)
		self.info = info


	def update(self, file):
		if file not in self.commitedFiles:
			self.commitedFiles.update({file.getName(): file})
			return "Commit File| New File:" + file.getName() + " | " + self.date
		else:
			self.commitedFiles[file.getName()].modify(file.getSource())
			return "Modified File | New File:" + file.getName() + " | " + self.date


	def getLog(self):
		return self.date + " | " + self.code + " | " + self.info