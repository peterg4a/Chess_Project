from turtle import *
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
def save():
 ts = getscreen()
 ts.getcanvas().postscript(file="Square.png")
onkeypress(save, key="q")
mainloop()