import turtle

def draw_shape(some_turtle):
    for i in range(1,5,1):
        some_turtle.forward(100)
        some_turtle.right(90)


def main_func():
    win=turtle.Screen()
    win.bgcolor("red")
    hem=turtle.Turtle()
    hem.shape("turtle")
    hem.color("green")
    hem.speed(2)

    for j in range(1, 37):
        draw_shape(hem)
        hem.right(10)




    win.exitonclick()

main_func()
