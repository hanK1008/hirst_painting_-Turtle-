# # how to export color from image using colorgram module
# # Download and Import
# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
#
# rgb_values = []
# for color in colors:
#     red = color.rgb.r
#     green = color.rgb.g
#     blue = color.rgb.b
#     rgb = (red, green, blue)
#     rgb_values.append(rgb)
#
# print(rgb_values)
# # Get rid of white shades: delete all which is very close to 255 rgb value

import turtle
import random


color_list = [(250, 228, 12), (198, 11, 36), (207, 13, 11), (233, 228, 5), (195, 67, 21),
         (239, 147, 30), (45, 210, 59), (30, 91, 187), (34, 32, 153), (17, 25, 54), (245, 38, 143), (68, 10, 52),
         (224, 249, 240), (61, 205, 231), (14, 203, 220), (247, 43, 12), (64, 25, 11), (223, 20, 102), (14, 150, 30),
         (227, 167, 8), (97, 75, 9), (248, 11, 8), (64, 242, 167), (226, 241, 247), (224, 137, 208), (9, 97, 62),
         (5, 46, 38), (85, 227, 237)]


# for setting so turtle can take tuple RGB values
# without this colormode programme will give error for color tuple values
turtle.colormode(255)

t = turtle.Turtle()
t.hideturtle()          # hide the turtle in result window
t.speed("fast")         # for drawing in fast speed


def painting(dot_size, space):              # dot_size = 20 , space = 50
    for i in range(1, 101):                 # for 100 dots
        color = random.choice(color_list)   # FOr choosing random RGB tuple value from above list
        t.dot(dot_size, color)              # Setting dot size and dot color
        t.penup()                           # For creating dot we don't need the pendown
        t.forward(space)
        if i % 10 == 0:    # For going to one line top to the previous line
            y = i/10
            t.goto(0, space*y)


painting(20, 50)     # calling the function


screen = turtle.Screen()
screen.exitonclick()

