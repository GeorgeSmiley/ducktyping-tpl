class Duck:
	def quack(self):
		print("Quaaack")
				
class Man:
	def quack(self):
		print("Imitates a quack")
				
class Eagle:
	def fly(self):
		print("Dude i do not quack, i just fly")
				
class MakeItQuack:
	def __init__(self, animal):
		animal.quack()
					
MakeItQuack(Duck())
MakeItQuack(Man())
MakeItQuack(Eagle())