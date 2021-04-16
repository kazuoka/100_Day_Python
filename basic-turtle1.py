import turtle
import random

tao = turtle.Turtle()
tao.pensize(4)
tao.shape('turtle')

color = ['red', 'green', 'blue', 'yellow', 'black', 'pink', 'orange', 'brown']

for i in range(1, 11):
    c = random.choice(color)
    r = random.randint(-200, 100)
    t = random.randint(-200, 100)
    s = random.randint(100, 100)
    v  = random.randint(100, 100)
    print('เต๋าเดินรอบที่:', i)
    tao.penup()
    tao.goto(r, t)
    tao.pendown()
    tao.color(c)
    tao.fd(s)
    tao.lt(90)
    tao.fd(v)
    tao.lt(90)
    tao.fd(s)
    tao.lt(90)
    tao.fd(v)
    tao.lt(90)
    
    
    
    
    
    
    
    
    
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    