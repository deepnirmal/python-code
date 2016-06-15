op1=0.0
op2=0.0
op=''
while op1 != 'q' :
  print("Enter first number : (q to quite) ")
  op1=input()   
  if op1=='q':
    break; 
  op1=float(op1)
  print("Enter second number: ")
  op2=float(input())
  print("Enter operation :(+,-,/,*) ")
  op=input()
  print("Result= ",end="") 
  if op=='+' :
   print(op1+op2)
  elif op=='-' :
   print(op1-op2)
  elif op=='*' :
   print(op1*op2)
  elif op=='/' :
   if op2==0 :
     print("Division by zero not possible !")
     break 
   else :
     print(op1/op2)
  else :
    print("Invalid operator." )

  