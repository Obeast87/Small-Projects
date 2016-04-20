name = raw_input('I will judge you by the length of your name. What is your name? ')
if len(name) > 3 and name.isalpha():
	print "You seem like a cool dude! Have a great day!"
elif len(name) <= 3 and name.isalpha():
	print "You seem like a bad guy! Get away from me, criminal of life!"
elif name.isalpha() == False:
	print "Names don't have numbers! Who are you trying to fool?"
else:
	print "Fine, don't tell me your name."

