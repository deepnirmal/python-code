class Employee :
	def __init__(self,name,payRate):
		self.name=name
		self.payRate=payRate
	def __str__(self) :
		return self.name+" ," +str(self.payRate)

	def pay(hoursWorked) :
		return self.payRate* hoursWorked


e1=Employee("Deep Nirmal",10.00)

print(e1)
