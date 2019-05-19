class Person():
	def __init__(self, name, surname):
		self.name = name
		self.surname = surname
	def get_info(self):
		return self.name + " " + self. surname

class Teacher(Person):
	def __init__(self, name, surname):
		Person.__init__(self, name, surname)
	def get_info(self):
		return self.name + " " + self. surname + " is a teacher"

class Student(Person):
	def __init__(self, name, surname, id):
		Person.__init__(self, name, surname)
		self.id = id
	def get_info(self):
		return self.name + " " + self. surname + " is a student"
	def get_id(self):
		return self.id











person = Person("Mario", "Rossi")
teacher = Teacher("Mario", "Bianchi")
student = Student("Mario", "Verdi", 64000)

print(person.get_info())
print(teacher.get_info())
print(student.get_info())
print(student.get_id())