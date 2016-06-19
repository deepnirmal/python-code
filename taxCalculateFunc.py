#0-250 0%
#251-500 15%
#501- 	28&

def tax(amount) :
	if amount<=250 :
		return 0
	elif amount > 250 and amount <=500 :
		return amount*0.15
	else :
		return amount*0.28

def netpay(grosspay) :
	return grosspay-tax(grosspay)

#print("Enter the amount : ") 
#amount=int(input()) 
#print("The tax collected is : "+str(tax(amount)) )

print("Enter gross pay : ")
gp=int(input())

print("Net pay is : "+str(netpay(gp)))