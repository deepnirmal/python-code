
def isVowel(letter):
		if letter=="a" or letter=="e" or letter=="i" or \
		letter=="o" or letter=="u" :
			return True 
		else :			
			return False


def numVowels(string):
	string=string.lower()
	count=0
	for i in range(len(string)) :
		if isVowel(string[i]) :
			count+=1 

	return count

print("Enter a string: ")
strng=input()

print("No of vowels in the string is : "+str(numVowels(strng))+"")
 