
for number in range(1, 101):
	if ((number % 4) == 0):
		if ((number % 5) == 0):
			print(f"{number} Go Figure")
	elif ((number % 4) == 0):
		print(f"{number} Go")
	elif ((number % 5) == 0):
		print(f"{number} Figure")
