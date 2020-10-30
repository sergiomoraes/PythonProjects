from io import IOBase
from io import TextIOBase

content = TextIOBase()

def content():
	with open("C:\\Users\\Sergio.Moraes\\Downloads\\releasenotes.txt", newline="") as file:
		TextIOBase.tell(file)
		print(file.seek(TextIOBase.tell(),1))
		print(file.readlines(1))
		print(file.seek(TextIOBase.tell(), 2))
		print(file.readlines(1)
