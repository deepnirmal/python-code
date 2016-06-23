#Recursive approach to count the no of letters in a sentence

def countLetters(words):
	if len(words)<1 :
		return 0
	else :
		return len(words[0])+countLetters(words[1:])



sentence=['now','is','the','time','for','Winterfell']

print(sentence)
print(countLetters(sentence))
