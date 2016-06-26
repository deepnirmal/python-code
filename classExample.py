#Example of definition and declaration of classes or objects

class Name :
	#constructor - instantiation
	def __init__(self,first,middle,last):
		self.first=first
		self.middle=middle
		self.last=last

	#to-string method
	def __str__(self):
		return self.first+' '+self.middle+' '+self.last

	def lastFirst(self):
		return self.last+","+self.first+" "+self.middle

	def initials(self):
		return self.first[0]+self.middle[0]+self.last[0]

dName= Name('Deep','S','Nirmal')
kName=Name('Krupa','S','Nirmal')

print("dName is : "+str(dName))
print("last first : "+str(dName.lastFirst()))
print(dName.initials())