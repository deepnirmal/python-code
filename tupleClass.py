#Composition not inheritance
class Point:
	def __init__(self,x,y):
		self.point=(x,y)

	def __str__(self):
		return "X: "+str(self.point[0])+" Y:"+str(self.point[1])
	def setLocation(self,x,y) :
		self.point=(x,y)


class Line:
	def __init__(self,p1,p2):
		self.point1=p1
		self.point2=p2

	def __str__(self):
		return "Point 1 : "+str(self.point1)+" Point 2:"+str(self.point2)

p1=Point(1,2)
print(p1)
p1.setLocation(10,20)
print(p1)

p2=Point(8,9)
line1=Line(p1,p2)

p2.setLocation(12,22)
print(line1)