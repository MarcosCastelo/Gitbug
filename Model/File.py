class File:
	def __init__(name, ext, modified):
		self.name = name
		self.ext = ext
		self.modified = modified

	def modify(self, state):
		self.modified = state

