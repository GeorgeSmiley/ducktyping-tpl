
#Always false
#print("10" == 10)
#The non numeric type will always be grather than the numeric type 
print("10">10)
print("10">=10)
print("10"<10)
print("10"<=10)

class Duck:
	def quack(self):
		print("Quaaack")
class Eagle:
	def fly(self):
		print("flyyy")

eagle = Eagle()
donald = Duck()


print (eagle<donald)
