from random import randint

def subtract():
	x = randint(1, 100)
	y = randint(1, 100)
	z = (y - x)
	print "%s" "-" "%s" " =" " %s"  % (y, x, z)
	if z < 0:
		subtract()
	else:
		return
	
subtract()
