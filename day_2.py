#Data Types

#String

# print("Hello"[0])

# print("123" + "456")

#Integer

# print(123 + 456)

# 123_456_789 # Large Integers

#Float

# 3.14159 # Floating Point Number

#Boolean

# True
# False

# num_char = len(input("What is your name?"))
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters.")

a = float(123)
print(type(a))

# print(70 + float("100.5"))
print(str(70) + str(100))


# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

# print(first_digit)
# print(second_digit)

result = int(first_digit) + int(second_digit)
print(result)



#Data Types

#String
"Hello"

#Integer
123

#Float
3.14159

#Boolean
True
False

#Type Errors
# num_char = len(input("What is your name?"))
# new_num_char = str(num_char)
# print("Your name has " + num_char + " characters.")

#Type Checking
type()

#Type Conversion
str()
int()
float()
bool()

# Maths Operations
3 + 5
7 - 4
3 * 2
6 / 3
2 ** 3

# PEMDASLR (Parentheses, Exponents, Multiply & Divide, Add & Subtract, Left to Right)
# ()
# **
# * /
# + -

print(3 * (3 + 3) / 3 - 3)

#Rounding Numbers
round(4.6666666666)

#Floor division
9 // 4

#Shorthand Operators
# a += 2  short for a = a + 2
# -=
# *=
# /=


#f-Strings
score = 0
height = 1.8
isWinning = True
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")


#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places.
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

#FAQ: How to round to 2 decimal places?
#https://www.udemy.com/course/100-days-of-code/learn/lecture/17965132#questions/13315048

print(f"Each person should pay: ${final_amount}")








