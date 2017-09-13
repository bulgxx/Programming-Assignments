# Purpose: The program should receive input from user, and generate an output of ohms/current in ciruit(amps) using different formulas. 
# Pre-conditions: User inputs resistance of resistors, & then power in watts
# Post-conditions: Program outputs resistance of resistors in series & parallel, in ohms. Also how many amps are in the current in the circuit (series & parallel)

# Import math to be able to use square root function

import math
def main():

	# Print the title & tab it towards the middle(name included)
	print("\tResistor Calculations")
	print("\t  by Petia Nikolova\n")



	# Ask for input form user for three resistors
	# Make resistors == 0.01 if resistance entered is 0 or <0.
	resistor1 = float(input("Enter the resistance of the first resistor: "))
	if (resistor1 == 0):
		resistor1 = 0.01
	elif (resistor1 < 0):
		resistor1 = abs(resistor1) 
	resistor2 = float(input("Enter the resistance of the second resistor: "))
	if (resistor2 == 0):
		resistor2 = 0.01
	elif (resistor2 < 0):
		resistor2 = abs(resistor2)
	resistor3 = float(input("Enter the resistance of the third resistor: "))
	if (resistor3 == 0):
		resistor3 = 0.01
	elif (resistor3 < 0):
		resistor3 = abs(resistor3)


	# Write formula for series resistors (add togther)	
	series_tot = (resistor1 + resistor2 + resistor3)
	# Write formula for parallel resistors in two parts
	parallel_tot = ((1/resistor1) + (1/resistor2) + (1/resistor3))
	parallel_tot = (1/parallel_tot)
	

	# Print total for series and parallel in "ohms." Round numbers to the hundredths place
	print("\nThe resistance of these three resistors in series is", round(series_tot,2), "ohms")	
	print("The resistance of these three resistors in parallel is", round(parallel_tot,2), "ohms")


	# Ask user for input on watts
	p = float(input("\nHow much power (in watts)? "))
	# If/elif watts input is 0 or <0
	if (p == 0):
		p = 0.01
	elif (p < 0):
		p = abs(p)

	
	# I = sqrt(P/R) == series_current; round number to 4 decimal places
	# Use same formula for I, Just change R (depending if series/parallel); round to 4 dec. places
	series_current = math.sqrt(p/series_tot)
	round_sc = round(series_current,4)
	parallel_current = math.sqrt(p/parallel_tot)
	round_pc = round(parallel_current,4)

	# Print how many amps is in the circuit that fluctuates depending on user input
	# Make print statement for circuit in series, and circuit in parallel	
	print("\nThe current in the circuit with the resistors in series is", round_sc, "amps when the power is", p, "watts.")
	print("The current in the circuit with the resistors in parallel is", round_pc, "amps when the power is", p, "watts.\n")

main()
