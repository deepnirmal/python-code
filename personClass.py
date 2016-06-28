class Person :
	def __init__(self,name,sex,age) :
		self.name=name
		self.sex=sex
		self.age=age

	def __str__(self):
		return self.name+' '+self.sex+' '+str(self.age)

	def changeName(self,name):
		self.name=name

	def changeAge(self):
		self.age=self.age+1


person1=Person('Deep','M',21)
person2=Person('Harsh','M',21)

print("Person 1 : "+str(person1))
person1.changeAge()
print("Person 1 : "+str(person1))

print("Person 2 : "+str(person2))
person2.changeName("Venky")

print("Person 2 : "+str(person2))
