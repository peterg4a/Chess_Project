from turtle import *
speed(1000)
shape('triangle')
hideturtle()
pu()
right(30)

def triangle(levels, length):
    if levels == 0:
        forward(2*length)
        right(150)
        pd()
        begin_fill()
        for i in range(3):
            forward((3**0.5)*length*2)
            right(120)
        end_fill()
        pu()
        left(150)
        backward(length*2)
        return
    
    for i in range(3):
        forward(length)
        triangle(levels-1, length/2)
        backward(length)
        right(120)

triangle(4, 50)
mainloop()