class Duck:
	pass

def quack(myself, arg):
	myself.val = arg
	return myself.val

donald = Duck()

Duck.quack = quack



print donald.quack("Quaaack!")