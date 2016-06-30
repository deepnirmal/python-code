try:
	print("Enter a file name :")
	name=input()
	file=open(name,'r')
	display(file)
except :
	print("Error with file ")
	print("Enter a file name ")
	name=input()
	file=open(name,'r')
	display(file)

finally:
	file.close()

	