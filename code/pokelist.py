class Duck():
	def quack(self):
		return "Quaaack"
	def fly(self):
		return "The duck is flying"

class Parrot():
	def quack(self):
		return "The parrot parrots a quack"
	def fly(self):
		return "The parrot is flying"
	
class Man():
	def __init__(self, name):
		self.name = name
	def quack(self):
		return "The man parrots a quack too"

donald = Duck()
charlie = Parrot()
john = Man("John")
jack = Man("Jack")
v = [donald, charlie, john, jack]

def fly(self):
	return self.name + " takes a plane"

Man.fly = fly

import types

john.fly = types.MethodType(fly, john)

for i in v:
	print(i.fly())

