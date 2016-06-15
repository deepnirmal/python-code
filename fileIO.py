
count=0
total=0
inFile=open('readGrades.txt','r')
grade=inFile.readline()
while (grade) :
	print(grade)
	count=count+1 
	total=total+int(grade)
	grade=inFile.readline()
avg=total/count

print("Average is : "+ str(avg)) 
outFile=open('avg.txt','w')
outFile.write("Average ="+str(avg))


