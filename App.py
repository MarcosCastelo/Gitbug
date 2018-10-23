from Controller.Tracking import *
from Controller.FilesControl import *

def main():
	app = TrackingManager()
	fileManager = FileManager()

	while True:
		operation = input(">")
		if operation == "create":
			name = input(">create>")
			error = fileManager.createFile(name)
			print(error)
		if operation == "add":
			name = input(">add>")
			file = fileManager.getFile(name)
			error = app.addFile(file)
			print(error)

if __name__ == '__main__':
	main()