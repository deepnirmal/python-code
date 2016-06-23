
#in my deep opinion
#IMDO

def first(word):
	return word[0]

words=['in','my','deep','opinion']

#acro=list(map(first,words))
#it returns a list

def acronym(words):
	acro=''
	acro=acro.join(list(map(first,words))).upper() 	 
	return acro
#acro=''
#acro=acro.join(list(map(first,words))).upper() 	 
acro=acronym(words)

print(acro)