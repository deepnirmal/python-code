#Nested or Lexical scope

import math

def hypotenuse(s1,s2):
	def sqaure(num):
		return num*num 
	return math.sqrt(sqaure(s1)+sqaure(s2))

print("Enter two side of a traingle :")
side1=int(input())
side2=int(input())
hyp=hypotenuse(side1,side2)
print("Length of Hypotenus: "+str(hyp))