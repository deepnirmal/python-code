#Function Example

def square (number):
	return number * number 

def numVowels(string):
	string=string.lower()
	count=0
	for i in range(len(string)) :
		if string[i]=="a" or string[i]=="e" or string[i]=="i" or \
		string[i]=="o" or string[i]=="u" :
			count+=1 

	return count




print("Enter a num : ")
num=int(input())
numSquared= square(num) 

print("Square of "+str(num)+" is : "+str(numSquared)) ;

print("Enter a string :")
string=str(input())

noOfVowels= numVowels(string)

print("No of vowels in the given string : "+str(noOfVowels))


