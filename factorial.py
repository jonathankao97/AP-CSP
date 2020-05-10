import re


def factorial(index):
	if index==1:
		return 1
	return index*factorial(index-1)


factorialStart = input("Enter factorial you wish to calculate!:")
if re.match('\\d', factorialStart):
	print(str(factorialStart) + "! is equal to: " + str(factorial(int(factorialStart))))
else:
	print("Invalid Input, Try again!")
