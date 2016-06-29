class Account:
	def __init__(self,accNumber,balance) :
		self.accNumber=accNumber
		self.balance=balance

	def __str__(self):
		return "Account number : "+str(self.accNumber)+\
		"\nBalance : " + str(self.balance) 

	def deposit(self,amount):
		self.balance+=amount
		
class Checking(Account) :
	def __init__(self,accNumber,balance,fee) :
		Account.__init__(self,accNumber,balance)
		self.fee=fee


	def __str__(self):
		resStr= "Account type: Checking\n"
		resStr+= Account.__str__(self)
		return resStr

	def getFee(self) :
		return self.fee

	def withdraw(self,amount) :
		if amount>self.balance :
			print("Insufficient balance!")
		else :
			self.balance=self.balance-amount-self.fee

class Savings(Account):
	def __init__(self,accNumber,balance) :
		Account.__init__(self,accNumber,balance)
	
	def __str__(self):
		resStr= "Account type: Savings\n"
		resStr+= Account.__str__(self)
		return resStr


	def withdraw(self,amount) :
		if amount>self.balance :
			print("Insufficient balance!")
		else :
			self.balance=self.balance-amount


ca=Checking("123",500,50)
print(ca)
ca.withdraw(100)
print(ca)
ca.deposit(200)
print(ca)


sa=Savings("Deep Nirmal",1000)
print(sa)
sa.withdraw(250)
print(sa)
sa.deposit(125)
print(sa)

accounts=[ca,sa]
print("\n\nDisplaying all accounts : ")
for i in range(0,len(accounts)):
	print(accounts[i])