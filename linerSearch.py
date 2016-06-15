#Linear sort implementation

print("Hello Welcome to Linear search!")

print("Enter the no of the elements : ")

n=int(input())

array=[]
print("Enter the elements :")
for i in range(0,n) :	
	array.append(int(input()))

key=int(input("Enter the key to be search.. :"))
x=0
for i in array :
	x=x+1
	if key == i :
		print("found at"+str(x))
		exit()
print("Not found!")	


