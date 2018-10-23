from . import Useful
import random
class Commit:
	def __init__(self, date):
		self.commitedFiles = {}
		self.date = date
		id = random.randint(1000, 9999)

		self.code = Useful.encrypt(str(id)+str(date))


	def update(self, file):
		if file not in self.commitedFiles:
			self.commitedFiles.update({file.getName(): file})
		else:
			self.commitedFiles[file.getName()].modify(file.getSource())
