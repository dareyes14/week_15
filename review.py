#Booleans

#Check Even or Odd: Write a program to check if a number entered by the user is even or odd.
# Input: Integer
# Output: "Even" or "Odd"

# num = int(input("Enter a number: "))
# if num % 2:
#     print("This number is Odd!")
# else:
#     print("This number is Even!")


# Comparison Operators

# Max of Three Numbers: Compare three numbers entered by the user and print the largest.
# Input: Three integers
# Output: Largest number

# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))
# num3 = int(input("Enter a final number: "))

# numbers = [num1, num2, num3]

# num_1 = max(numbers)

# print(num_1 " is the largest number!")


#Decisionmaking

#Voting Eligibility: Prompt the user for their age and citizenship status. Determine if they can vote.
#Input: Integer (age), String ("yes" or "no" for citizenship)
#Output: "Eligible to vote" or "Not eligible to vote"

# age = int(input("Please enter your age: "))
# ctz = str(input("Are you a citizen? Enter yes or no: "))

# if (age >= 18) and (ctz == "yes"):
#     print("You are an eligible voter!")
# else:
#     print("You are not an eligible voter!")


#List Comprehension

# Temperature Conversion: Convert a list of Celsius temperatures to Fahrenheit using list comprehension.
# Formula: 
# F=C×95+32
# F=C×
# 5
# 9
# ​
# +32
# Input: List of Celsius temperatures
# Output: List of Fahrenheit temperatures

temps = int(input("Please list all temperatures and divide with a comma: "))

temp_change = [(temps) * 95 + 32]


print(temp_change)