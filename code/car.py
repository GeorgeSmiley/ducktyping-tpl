class Car:
	def __init__(self, engine):
		self.engine = engine
	def run(self):
		return self.engine.turn_on()		

class ElectricEngine:
	def turn_on(self):
		return "zzzz"
class EngineV8:
	def turn_on(self):
		return "brooom"

electric = ElectricEngine()
fueled = EngineV8()

car = Car(fueled)

print(car.run())