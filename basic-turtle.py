import turtle
import random
tao = turtle.Turtle()
color = ['blue','yellow','green','red']
tao.pensize(4)

for i in range(1,11):
    c = random.choice(color) # สุ่มสี
    tao.color(c) # เปลี่ยนสีเต๋า
    r = random.randint(50,100)
    print('สุ่มได้รัศมี:',r)
    tao.circle(r) # สุ่มรัศมีวงกลม
    tao.left(36) # หมุน 36 องศาต่อวง
    print('หมุนครั้งที่:',i)