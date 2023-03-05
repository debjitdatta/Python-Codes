# Create a program that asks the user to enter their 
# name and their age. 
# Print out a message addressed to them that tells 
# them the year that they will turn 100 years old.

import datetime

today = datetime.date.today()

year = today.year


i = input("Enter you name: ")
j = int(input("Enter your age: "))

k = ((99-j) + year)

print(i, "will turn 100 years in", k , "years" )