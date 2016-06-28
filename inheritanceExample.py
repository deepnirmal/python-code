class Shape:
	def __init__(self,xcor,ycor) :
		self.x=xcor
		self.y=ycor

	def __str__(self):
		return "X : "+str(self.x)+" Y : "+str(self.y)

	def move(self,x1,y1):
		self.x=self.x+x1
		self.y=self.y+y1

#Class rectangle inherits from class Shape
class Rectangle(Shape) :
	def __init__(self,xcor,ycor,width,height):
		Shape.__init__(self,xcor,ycor)
		self.width=width
		self.height=height

	def __str__(self):
		retStr=Shape.__str__(self)
		retStr+=" Width: " +str(self.width)+\
			" Height: "+str(self.height) 
		return retStr


rec= Rectangle(5,10,8,9)
print(rec)

rec.move(10,12)
print(rec)




