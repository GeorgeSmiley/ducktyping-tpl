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
	def quack(self):
		return "The man parrots a quack too"

v = [Duck(), Parrot(), Man()]

for i in v:
	print(i.quack())

for i in v:
	print(i.fly())