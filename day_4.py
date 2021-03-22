# https://th.wikipedia.org/wiki/%E0%B9%81%E0%B8%A1%E0%B8%A3%E0%B9%8C%E0%B9%81%E0%B8%8B%E0%B8%99%E0%B8%97%E0%B8%A7%E0%B8%B4%E0%B8%AA%E0%B9%80%E0%B8%95%E0%B8%AD%E0%B8%A3%E0%B9%8C

# Mersenne twister เป็นขั้นตอนวิธีหนึ่งของตัวสร้างเลขสุ่มเทียม

# https://www.saratoga.com/how-should-i-know/2013/07/what-is-the-average-air-speed-velocity-of-a-laden-swallow/

# https://www.askpython.com/ search   random module /Python random Module – Generate Random Numbers/Sequences

# https://en.wikipedia.org/wiki/List_of_U.S._states_by_date_of_admission_to_the_Union /   Lists

# https://docs.python.org/3.8/tutorial/index.html  / Data Structures

# https://www.delish.com/food-news/a26872638/dirty-dozen-foods-list-2019/ ข้อมูลผัก ผลไม้

# https://getemoji.com/  / รูปหน้าตาต่าง ๆ 

# https://www.wrpsa.com/the-official-rules-fo-rock-paper-scissors / สร้างเกมส์

#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲

import random

random_side = random.randint(0, 1)
if random_side == 1:
  print("Heads")
else :
  print("Tails")



import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# print(names)
#Get the total number of items in list.
# num_items = len(names)
# Generate random numbers between 0 and the last index.
# random_choice = random.randint(0, num_items - 1)
# person_who_will_pay = names[random_choice]
# person_who_will_pay = random.choice(names)


print(person_who_will_pay + " is going to buy the meal today!")



# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
#23
horizonal = int(position[0]) #2
vertical = int(position[1]) #3

# selected_row = map[vertical - 1]
# selected_row[horizonal - 1] = "X"
# เขียนได้อีกแบบสั้นลง
map[vertical - 1][horizonal - 1] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")




# import random
# import my_module

# random_integeter = random.randint(1, 10)
# print(random_integeter)

# print(my_module.pi)

# 0.00000000 - 0.9999999...
# random_float = random.random() * 5 / random_float * 5 / 0.00000... - 4.9999999...
# print(random_float)

# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score}")

# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# print(states_of_america[0]) // Delaware แบบเลือก

# states_of_america.append("Iceland") // เอาไปไว้ท้ายสุด

# states_of_america.extend(["Iceland", "Jack Bauer Land"]) // เอาไปไว้ท้ายสุด

# print(states_of_america)

# num_of_states = len(states_of_america)

# print(states_of_america[num_of_states - 1])


# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]


fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)





import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0 :
  print("You typed an invalid number, you lose!")
else :
  print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice == 0 and computer_choice == 2 :
  print("You win!")
elif computer_choice == 0 and user_choice == 2 :
  print("You lose")
elif computer_choice > user_choice :
  print("You lose")
elif user_choice > computer_choice :
  print("You win!")
elif computer_choice == user_choice :
  print("It's a draw")








