def square(num):
	return num*num
#numbers=[1,2,3]
#numbersqr=list(map(square,numbers))
#print(numbersqr)

#FILTER
#consider the boolean values of the return
#if true then assign the value to the list

def even(num):
	if num%2 == 0 :
		return True
	else:
		return False


numbers= list(range(1,11))
evens=list(filter(even,numbers))
print(numbers)
print("FILTER WORKS :" + str(evens)) 


#Reduce function : sum of sequence of numbers
def sum(x,y):
	return x+y
numbers=list(range(1,11))
print(numbers)

import functools
sum=functools.reduce(sum,numbers)
print("REDUCE WORKS The sum of the range is : "+str(sum))