class Duck():
	#Constructor 
	def __init__(myself, name = "Don", colour = "brown"):
		myself.name = name
		myself.colour = colour
	
	def quack(myself):
		return "Quaaack"

	def fly(myself):
		return "The duck is flying"

		

donald = Duck("","white")

print(donald.name)
print(donald.colour)

print(donald.quack())
print(donald.fly())

don = Duck()
