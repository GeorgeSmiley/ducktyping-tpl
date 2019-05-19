class Bird():
	def __init__(self, var1, var2):
		self.var1 = var1
		self.var2 = var2
	def fly(self):
		return "A bird can fly"

class Duck(Bird):
	def __init__(self, var1, var2, var3):
		Bird.__init__(self, var1, var2)
		self.var3 = var3
	def quack(self):
		return "Quaaack"
	def fly(self, var):
		return "The duck is flying " + var 


	
b = Bird("ciao", "bella")
print(b.fly())


d = Duck("ciao", "bella", "ciao")
print(d.fly("ciao"))