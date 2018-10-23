from . import *

class TrackingManager:
	def __init__(self):
		self.trackedFiles = {}


	def addFile(self, file):
		if file.getName() not in self.trackedFiles:
			file.add()
			self.trackedFiles.update({file.getName() : file})
			return "new file add: " + file.getName()
		else:
			Tfile = self.trackedFiles[file.getName()]
			if not Tfile.getStage():
				self.trackedFiles[file.getName()] = file
				return "Unstaged file is updated"

		return "File is already updated"


