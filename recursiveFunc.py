#5!= 5 * 4 * 3 * 2 * 1
#5!= 5 * 4!


def fact(num) :
	if num<=1 :
		return 1
	else :
		return num* fact(num-1)

print("Enter a number : ") 

number = int(input())

print("Factorial of "+str(number)+" is  : "+str(fact(number)))