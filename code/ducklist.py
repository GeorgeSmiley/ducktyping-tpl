class Bird():
	def fly():
		pass

class Duck(Bird):
	def quack(self):
		return "Quaaack"
	def fly(self):
		return "The duck is flying"

class Parrot(Bird):
	def quack(self):
		return "The parrot parrots a quack"
	def fly(self):
		return "The parrot is flying"
	
class Man():
	def quack(self):
		return "The man parrots a quack too"

d = Duck()
p = Parrot()
m = Man()
v = [d, p, m]

print(isinstance(d, Bird))

for i in v:
	print(i.quack())

for i in v:
	print(i.fly())