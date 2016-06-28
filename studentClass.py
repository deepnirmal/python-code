class student :
	#fields - name,id,grades(list)
	grades=[]
	def __init__(self,name,id):
		self.name=name
		self.id=id 

	def addGrade(self,grade):
		self.grades.append(grade)

	def showGrades(self) :
		grds=''
		for grade in self.grades:
			grds+=str(grade)+" "
		return grds

	def __str__(self):
		return "Name : "+self.name+"\n"+\
				"ID : "+self.id+"\n"+\
				"Grades : "+self.showGrades()

	def average(self) :
		total =0
		for grade in self.grades:
		 	total+=grade
		return total/len(self.grades) 

stud1= student('Deep','055')
stud1.addGrade(99)
stud1.addGrade(89)
stud1.addGrade(92)

print(stud1)

print("Average: "+str(stud1.average()))
