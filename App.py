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

		if trackingManager != None:
			if operation[0] == "git":
				if len(operation) == 3:
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

					if command == "status":
						for file in fileManager.getFiles().keys():
							if file not in trackingManager.getTrackeds().keys():
								print("Untracked file:", file)
							else:
								print("Tracked file:", file)
								if fileManager.getFile(file).getStage() == False:
									print("Unstage file", file)

					elif command == "commit":
						data = date.today()
						info = input(">info> ")
						commit = Commit(data, info)
						for file in trackingManager.getTrackeds():
							error = commit.update(fileManager.getFile(file))
							print(error)
						commits.append(commit)
					elif command == "log":
						for commit in commits:
							log = commit.getLog()
							print(log,"\n")

		else:
			print("Nenhum repositorio iniciado")

		if operation[0] == "git" and operation[1] == "init":
			trackingManager = TrackingManager()
			print("Repositorio Criado")
		elif operation[0] == "create":
			name = input(">create> ")
			fileManager.createFile(name)
		elif operation[0] == "modify":
			name = input(">modify> ")
			modifications = input(">modify>modifications> ")
			error = fileManager.modify(name, modifications)
			print(error)
		elif operation[0] == "delete":
			name = input(">delete> ")
			if fileManager.getFile(file) not None:
				error = fileManager.delFile(file)
				print(error)


if __name__ == '__main__':
	main()
