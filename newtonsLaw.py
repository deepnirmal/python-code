#Newtons method to find the Square root of a number
import math

def sqaure(num):
	return num*num

def sqrt(num) :
	return sqrtHelper(1.0,num)


def sqrtHelper(guess,number) :
	if(closeEnough(guess,number) ):
		return guess
	else :
		return sqrtHelper(improve(guess,number),number)


def closeEnough(guess,number):
	return (math.fabs((sqaure(guess))-number)<0.001)

def improve(guess,x):
	return average(guess,(x/guess))

def average(x,y):
	return (x+y)/2

print("Enter a number : ")
number=int(input())

print(sqrt(number))