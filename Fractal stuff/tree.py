from turtle import *
speed(0)
def tree(size, levels, angle):
    if levels == 0:
        return

    forward(size)

    right(angle)
    tree(size*0.8, levels-1, angle)

    left(angle*2)
    tree(size*0.8, levels-1, angle)

    right(angle)
    backward(size)




left(90)
tree(60, 9, 45)

mainloop()
