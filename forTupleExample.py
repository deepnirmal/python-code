numbers=(1,2,3,4,5,6,7,8,9,10)

#sum=0 

#for num in numbers:
#	sum=sum+num
#	print(num)

#print("Sum="+str(sum))


words=("Deep","nirmal","is","programmer")

for word in words :
	print(word) 

max=0 
for i in range(1,len(words)) :
	if(len(words[i])>len(words[max])):
		max=i



print("The longest word is "+words[max])
