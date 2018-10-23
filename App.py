from Controller.Tracking import *
from Controller.FilesControl import *
from Controller.Repo import *
from datetime import date

def main():
	trackingManager = None
	fileManager = FileManager()
	commits = []

	while True:
		operation = input(">").split()
		if operation[0] == "git":
			if len(operation) == 3 and trackingManager == None:
				command = operation[1]
				file = operation[2]

				if command == "add":
					error = trackingManager.addFile(fileManager.getFile(file))
					print(error)

				elif command == "reset":
					error = trackingManager.resetFile(fileManager.getFile(file))
					print(error)

			elif len(operation) == 2:
				command = operation[1]
				if command == "init":
					trackingManager = TrackingManager()
					print("Repositorio Iniciado!")

				elif command == "status":
					for file in fileManager.getFiles().keys():
						if file not in trackingManager.getTrackeds().keys():
							print("Untracked file:", file)
						else:
							print("Tracked file:", file)

				elif command == "commit":
					data = date.today()
					print(data)
					commit = Commit(data)
					for file in trackingManager.getTrackeds():
						commit.update(file)
		elif operation[0] == "create":
			name = input("|create>")
			fileManager.createFile(name)


		

if __name__ == '__main__':
	main()