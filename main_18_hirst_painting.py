### --- EXTRACTING IMAGES FROM JPEGS --- ###

# import colorgram
#
# rgb_c = []
# colors = colorgram.extract("img.jpg", 30)
# for c in colors:
#     r = c.rgb.r
#     g = c.rgb.g
#     b = c.rgb.b
#     new_c = (r, g, b)
#     rgb_c.append(new_c)
#
# print(rgb_c)


### --- MAIN PROGRAM --- ###

import turtle as t_mod
import random

t_mod.colormode(255)
tim = t_mod.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
c_list = [(226, 147, 98), (28, 102, 177), (161, 56, 90), (148, 79, 51), (225, 61, 96),
(113, 174, 215), (244, 227, 95), (173, 20, 41), (233, 79, 51),
(224, 126, 156), (118, 184, 130), (11, 172, 207), (165, 151, 25), (13, 58, 148),
(83, 37, 23), (128, 37, 27), (37, 129, 78), (42, 192, 160), (14, 39, 92), (129, 238, 190),
(244, 162, 151), (235, 162, 181), (100, 101, 186), (127, 214, 239), (66, 77, 38), (74, 31, 46)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
n_dots = 101

for dot_count in range(1, n_dots):
    tim.dot(20, random.choice(c_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)










### --- Exit screen on click --- ###
screen = t_mod.Screen()
screen.exitonclick()