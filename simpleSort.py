#Sort function!

print("Enter the no of the elements : ")

n=int(input())

array=[]
print("Enter the elements :")
for i in range(0,n) :	
	array.append(int(input()))



array.sort()
print("Sorted arryay :")
for i in array :
	print(i)	
