# https://docs.python.org/3/library/functions.html

# https://reeborg.ca/index_en.html

# https://www.python.org/dev/peps/pep-0008/#tabs-or-spaces

# print("Hello")
# num_char = len("Hello")
# print(num_char)

"""
def my_function():
  print("Hello")
  print("Bye")

my_function()

"""

"""
#Draw Square
turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()
"""

"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for step in range(6):
    jump()


number_of_hurdles = 6:
while number_of_hurdles > 0:
  jump()
  number_of_hurdles -= 1
  print(number_of_hurdles)


while not at_goal():
  jump()

"""
  
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
  if wall_in_front():
      jump()
  else :
      move()





"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
  if wall_in_front():
      jump()
  else :
      move()
"""

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else :
        turn_left()

