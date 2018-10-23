from Controller.Tracking import *
from Controller.FilesControl import *

def main():
	app = TrackingManager()
	fileManager = FileManager()
	commits = []

	while True:
		operation = input(">").split()
		if operation[0] is "git":
			if len(operation) == 3:
				git = operation[0]
				command = operation[1]
				file = operation[2]

					if command is "add":
						error = app.addFile(fileManager.getFile(file))
						print(error)

					elif command is "reset":
						error = app.resetFile(fileManager.getFile(file))


		

if __name__ == '__main__':
	main()