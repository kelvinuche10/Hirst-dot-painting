import turtle as t
import colorgram
import random


tim = t.Turtle()
tim.speed('fastest')
tim.hideturtle()
tim.setheading(225)
tim.penup()
tim.forward(320)
screen = t.Screen()
screen.colormode(255)
colors = colorgram.extract('C:\\Users\\USER\Desktop\\new_angela_yu\\day-18\\image.jpg', 20)
list_of_colors = []
rgb = []
for color in colors:
    r = color.rgb.r
    b = color.rgb.b
    g = color.rgb.g
    new_color = (r, g, b)
    list_of_colors.append(new_color)

no_of_dots = 100

for dot_count in range(1, no_of_dots+1):
    tim.dot(40, random.choice(list_of_colors))
    tim.setheading(0)
    tim.forward(60)
    if dot_count % 10 == 0:
        tim.left(90)
        tim.forward(50)
        tim.left(90)
        tim.forward(590)
        tim.setheading(0)
        







screen.exitonclick()
