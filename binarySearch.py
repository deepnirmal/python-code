print("Enter the num of elements")
n=int(input())

print("Enter the elements.. :")
a=[]

for i in range(0,n) :
	a.append(int(input()))

key=int(input("Enter the key to search : "))

low=0
high=n
flag=0
mid=0
while (low<high) or a[mid]!=key :
	mid=int((low+high)/2)

	if key>a[mid] :
		low=mid+1 
	else :
		high=mid-1 
	

if a[mid]==key:
	print("Key found at "+str(mid+1)+" position")
else: 
	print("Not found!")
