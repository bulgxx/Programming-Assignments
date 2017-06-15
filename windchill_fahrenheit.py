import math
def main():
   
	print("Big Blue Wind Chill")

	velocity = float(input("Enter the wind velocity (mpy) "))
	tempF = float(input("Enter air temperature (F) "))
		 
	the_root = math.sqrt(velocity)
	
	OldStyleWC = round((0.081 * ((3.71 * the_root) + 5.81 - (.25 * velocity)) * (tempF - 91.4) + 91.4),1)
	NewStyleWC = round((35.74 + (0.6215 * tempF) - 35.75 * (velocity **0.16) + (0.4275 * tempF * (velocity ** 0.16))),1)
	

	new_chill =('new wind chill in Fahrenheit')
	old_chill =('old wind chill in Fahrenheit')
	print(NewStyleWC, 'new wind chill in Fahrenheit')
	print(OldStyleWC, 'old wind chill in Fahrenheit')

main() 
