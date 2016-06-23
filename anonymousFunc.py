#Anonymous function
#known as Lambda form


#def square(number) :
# 	return number*number


square= lambda x: x*x
print(square(2))


numbers=[1,2,3,4]

numbersqr=list(map(lambda x:x*x,numbers))
print(numbersqr) 
