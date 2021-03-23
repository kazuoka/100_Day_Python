# https://haveibeenpwned.com/ 

# https://en.wikipedia.org/wiki/List_of_the_most_common_passwords

# https://th.wikipedia.org/wiki/%E0%B8%84%E0%B8%B2%E0%B8%A3%E0%B9%8C%E0%B8%A5_%E0%B8%9F%E0%B8%A3%E0%B8%B5%E0%B8%94%E0%B8%A3%E0%B8%B4%E0%B8%8A_%E0%B9%80%E0%B8%81%E0%B8%B2%E0%B8%AA%E0%B9%8C

# https://stackoverflow.com/questions/2177590/how-can-i-reorder-a-list/2177607

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# print(student_heights)
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
# print(len(student_heights))
# print(sum(student_heights))

# total_height = sum(student_heights)
total_height = 0
for height in student_heights:
  total_height += height
# print(total_height)

# number_of_students = len(student_heights)
number_of_students = 0
for student in student_heights:
  number_of_students += 1
# print(number_of_students)

average_height = round(total_height / number_of_students)
print(average_height)




# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
# print(max(student_scores))
highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score
print(f"The highest score in the class is: {highest_score}")





#Write your code below this row 👇

total = 0
# เลขคี่
# for number in range(1, 101, 2):
# เลขคู่
for number in range(2, 101, 2):
  # print(number)
  total += number
  # print(total)
print(total)

total2 = 0
for number in range(1, 101):
  if number % 2 == 0:
    total2 += number

print(total2)
  




#Write your code below this row 👇

"""
for number in range(1, 101):
  if number % 3 == 0:
    #Divisible by 3
  elif number % 5 == 0:
    #Divisible by 5
  elif number % 3 == 0 and % 5 == 0:
    #Divisble by both 3 and 5
"""
for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else :
    print(number)





#For Loop with Lists
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
  print(fruit)
  print(fruit + " Pie")

#For Loop with Range

for number in range(1, 100):
  print(number)

for number in range(1, 101):
  print(number)

# แบบข้ามไปทีล่ะ 3
for number in range(1, 11, 3):
  print(number) # 1 4 7 10

#Calculating the sum of all the numbers from 1 to 100.
total = 0
for number in range(1, 101):
  total += number
print(total)





#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# password = ""
"""
#nr_letters = 4
for char in range(1, nr_letters + 1):
  #1 - 4
  random_char = random.choice(letters)
  # print(random_char)
  password += random.char
  print(password)
"""
"""
for char in range(1, nr_letters + 1):
  password += random.choice(letters)

for char in range(1, nr_symbols + 1):
  password += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password += random.choice(numbers)

print(password)
"""


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_list = []

for char in range(1, nr_letters + 1):
  password_list += random.choice(letters)

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")