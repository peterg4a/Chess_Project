from turtle import *
def snowflake_side(length, levels):
    length /= 3
    if levels == 0:
        forward(length)
        return

    snowflake_side(length, levels-1)
    left(60)
    snowflake_side(length, levels-1)
    right(120)
    snowflake_side(length, levels-1)
    left(60)
    snowflake_side(length, levels-1)

def snowflake(sides, length, levels):
    for i in range(sides):
        snowflake_side(length, levels)
        right(360/sides)

speed(0)
penup()
goto(-200, 200)
pendown()

snowflake(3, 500, 3)

mainloop()