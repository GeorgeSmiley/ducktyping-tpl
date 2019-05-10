class Parrot():
	def __init__(self, name = "Perry"):
		self.name = name

bird1 = Parrot()
bird2 = Parrot("Jack")

print(bird1.name)
print(bird2.name)