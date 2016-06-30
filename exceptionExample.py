#Divide by zero exception
#print("Enter a numerator : ")
#numo=int(input())
#print("Enter a  denominator: ")
#deno=int(input())

#quotient=numo/deno 

#print(quotient)

#File exception
#file=open('blahbb.text','r')


try:
	print("Enter a numerator : ")
	numo=int(input())
	print("Enter a  denominator: ")
	deno=int(input())

	quotient=numo/deno 

	print(quotient)
except:
	print("Cannot divide by zero!")
	print("Enter a new  denominator: ")
	deno=int(input())

	quotient=numo/deno 

	print(quotient)
	


try :
	print("Enter the name of the file : ")
	name=input()
	file=open(name,'r')
#except IOerror:
#excpet ZeroDivision
except:
	print("Cannot open file")
	print("Enter the name of the file to open : ")
	name=input()
	file=open(name,'r')

