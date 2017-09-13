#Petia Nikolova
#Wednesday, January 18, 2017
#Fizz-Buzz

def main():

	accum_3 = 0 
	accum_5 = 0
	accum_both = 0

	for digit in range(1,101):
		if ((digit % 3 == 0) and (digit % 5 == 0)):
			print("FizzBuzz")
			accum_both += 1
		elif (digit % 3 == 0):
			print("Fizz")
			accum_3 += 1
		elif (digit % 5 == 0):
			print("Buzz")
			accum_5 += 1
		else:
			print(digit)
	
	print('\n')
	print("Numbers divided by 3 are",accum_3)
	print("Numbers divided by 5 are", accum_5)
	print("Numbers divided by 3 & 5 are", accum_both)
main()

#Started 9PM
#Finished 9:25 PM
 
#I did have some online help, just to realize I was making it harder than I should have, and that my "if digit % 3 == 0 and if digit % 5 ==0", should be the first one.

#27 numbers divided by 3
#14 numbers divided by 5
#6 numbers are divided by 3 and 5 
