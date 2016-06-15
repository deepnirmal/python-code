

n=int(input("Enter a number to find a factorial : "))
fact=1 
for i in range(1,n+1):
	fact=fact*i

print("Factorial of "+str(n)+" is : "+str(fact))

ctr=0
temp=fact
# while temp%10 ==0  : 
# 	ctr=ctr+1 
# 	temp=temp/10

string=str(fact)


for i in range(len(string)-1,0,-1):
	if string[i] == '0' :
		ctr=ctr+1 
	else :
		break

print("no of trailing zeros : "+str(ctr))
