def square(number):
	return number*number


num=2
sqnum= square(num)

#Assigning object to a function
sqnumber= square

sqnum= sqnumber(3)
print(sqnum)

#Map function- high order function


numbers = [1,2,3,4]

numbersSquared= list(map(square,numbers))

print(numbersSquared)