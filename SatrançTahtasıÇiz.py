import turtle

cizim = turtle.Turtle()
cizim.pensize(1)
cizim.speed(10)
genislik = 40


def mysquare(kim, renk, boyut):
    kim.pendown()
    kim.pencolor(renk)
    kim.fillcolor(renk)
    kim.begin_fill()
    kim.setheading(0)
    for i in range(4):
        kim.forward(boyut)
        kim.left(90)
    kim.end_fill()


for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            zrengi = 'black'
        else:
            zrengi = 'lightgray'
        cizim.penup()
        cizim.goto((i - 4) * genislik, (j - 4) * genislik)
        mysquare(cizim, zrengi, genislik)