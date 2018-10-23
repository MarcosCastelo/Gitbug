from Controller.Tracking import *
from Controller.FilesControl import *

def main():
	app = TrackingManager()
	while  True:
		nomeArquivo = input(">")
		print("OK")
		arq = File(nomeArquivo)
		print(app.addFile(arq))
		print(app.trackedFiles)

if __name__ == '__main__':
	main()