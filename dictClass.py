#Duplication of words and count

sentence="hello deep nirmal python"
sentence+=" welcome to python programming"

words=sentence.split(' ')
words=sorted(words)

print("Sentence in sorted order " )
print(words)
numWords= { }

for i in range(0,len(words)):
	if words[i] in numWords :
		numWords[words[i]]+=1
	else:
		numWords[words[i]]=1

print("Word list and count: \n")
for key in numWords.keys():
	print(key,numWords[key])