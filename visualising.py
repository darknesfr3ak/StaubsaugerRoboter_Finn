import turtle

ScaleX = 840
ScaleY = 440

# Initialisierung der Turtle: Erstellen wenn benötigt von der Turtle, Sceen etc.
def Initialise():
    Smol_turtle = turtle.Turtle()
    Smol_turtle.speed(0)
    #Smol_turtle.hideturtle()
    Smol_turtle.shape("turtle")
    screen = turtle.Screen()
    screen.setup(ScaleX, ScaleY)
    screen.tracer(False)

    # turtle.mainloop()
    return Smol_turtle

# Visualisierung der Räume; MultV steht für wie groß ein Feld ist (25 = 25pxx25px)

OffsetX = -420
OffsetY = (ScaleY/2)-20#-220

def Visualise(Smol_turtle, X,Y, Type, Extra = "", Floor = ""):
    MultV = 25
    MultX = X*MultV
    MultY = Y*MultV
    Smol_turtle.penup()
    Smol_turtle.setpos(MultX+OffsetX,MultY+OffsetY)
    Smol_turtle.pendown()
    screen = Smol_turtle.getscreen()
    if Type == "ChargingStation":
        Smol_turtle.fillcolor((178/255, 240/255, 151/255))
        Smol_turtle.begin_fill()
    elif Type == "Blocked":
        Smol_turtle.fillcolor((0.25, 0.25, 0.25))
        Smol_turtle.begin_fill()
    elif Type == "Wall":
        Smol_turtle.fillcolor((99/255, 99/255, 99/255))
        Smol_turtle.begin_fill()
    elif Floor == "Hard":
        Smol_turtle.fillcolor((255/255,255/255,255/255))
        Smol_turtle.begin_fill()
    elif Floor == "Soft":
        Smol_turtle.fillcolor((214/255,214/255,214/255))
        Smol_turtle.begin_fill()
    else:
        Smol_turtle.color((0,0,0))
    if Extra == "Cleaned":
        Smol_turtle.fillcolor((151/255, 237/255, 240/255))
        Smol_turtle.begin_fill()
    elif Extra == "Path":
        Smol_turtle.fillcolor((191/255, 151/255, 240/255))
        Smol_turtle.begin_fill()
    else:
        Smol_turtle.pencolor((0,0,0))
    for i in range(4):
        Smol_turtle.forward(MultV)
        Smol_turtle.left(90)
    
    Smol_turtle.end_fill()
    Smol_turtle.color((0,0,0))
    screen.update()

def EndVisualising():
    turtle.mainloop()