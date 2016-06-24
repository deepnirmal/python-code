
#Global Scope exmaple
def getNumber() :
	print(number)

number=1
print(number)
getNumber()


#Local scope

def square(number) :
	sqaured=number*number
	return sqaured

print(square(2))

print("Squared (defined in function sqaure) :"+str(sqaured))