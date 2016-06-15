#inFile =open("text.txt","r")

#line=inFile.readline()
#while(line) :
#	print(line,end='')
#	line=inFile.readline()

#for line in open('text.txt') :
#	print(line,end='')
sum=0 
count=0 
for grade in open('readGrades.txt') :
	print(grade,end='')
	sum=sum+int(grade)
	count=count+1 
avg=sum/count

print("\n\t\tAvg :"+str(avg))
