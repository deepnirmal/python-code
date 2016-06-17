#Example 1
#N = range(1,100)
#EN= [ x for x in N if x % 2==0 ]
#print(EN)  

sent=" welcome to the python programming world "
sent+="hello world"
words= sent.split(' ')

wlen = [ (word,len(word)) for word in words]
for i in wlen :
	print(i)