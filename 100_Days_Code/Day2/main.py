# Basic Tip Calculator
# Day 2 Project
# Udemy: Angela Yu 100 Days of Code - Day 2 Project


print("Welcome to the Tip Calculator.")

# input() function will always return a string unless you cast it. I like to cast it while getting the input because it is easier to tell what type of data types each variable is.
total_bill = float(input("What is the total bill? $"))
num_people = int(input("How many people to split the bill between? "))
percent_tip = float(input("What percentage tip would you like to give? "))

total_with_tip = total_bill * (1 + (percent_tip/100.00))
per_person_pay = total_with_tip / num_people

# print(type(total_with_tip))
# print(type(total_bill))
# print(type(num_people))
# print(type(percent_tip))

# How to format using similar syntax to C:
per_person_pay = "{:.2f}".format(per_person_pay)

# f-Strings: Used to print multiple different data types, similiar to a a printf in C or Java, but much different syntax:
print(f"Each person should pay: ${per_person_pay}")
# print(round(per_person_pay, 2))

# How to do the forced rounding to multiple decimal places even if ends in zero by formatting to a string.
# print("Each person should pay: $" + "{:.2f}".format(per_person_pay))
