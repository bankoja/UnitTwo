#James Bankole 9/15/16
#This program calculates the compound and simple interest, displays them, and then calculates and displays the
# difference between the two.

#Introduce the program.
print("This program calculates and compares compound and simple interest.")

#Define the variables that the user is prompted to input.
#I used float so that I wouldn't have to enter "int" repeatedly. I also used float so that my program would not crash
# if a decimal number was inputed.
principle_amount = float(input("What is the principle amount?"))
annual_rate = float(input("What is the annual rate of interest? (as a decimal)"))
number_years_deposited = float(input("How many years is the amount deposited or borrowed for?"))
number_times_compounded = float(input("How many times is the interest compounded a year?"))

#Calculates the simple and compound interest and the difference between the two.
#Used absolute value so a negative number would not be displayed.
simple_interest = (principle_amount)*(annual_rate)*(number_years_deposited) + (principle_amount)
compound_interest = (principle_amount)*(1+ ((annual_rate)/(number_times_compounded)))**((number_times_compounded)*
                                                                                        (number_years_deposited))
difference = abs((compound_interest) - (simple_interest))

#Prints out final information to the user.
print("The amount generated by simple interest is:", simple_interest)
print("The amount generate by compound interest is:", compound_interest)
print("The difference is:", difference)