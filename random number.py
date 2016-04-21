from random import randint

def subtract():
	x = randint(1, 100)
	y = randint(1, 100)
	z = (y - x)
	if z < 0:
		print z
		subtract()
	else:
		print z

subtract()