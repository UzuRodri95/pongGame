import turtle
import time
import random

########################################################################################################
########################################## VARIABLES ###################################################
########################################################################################################
marcadorA = 0                                                                                    #######
marcadorB = 0                                                                                    #######
########################################################################################################
################### CREATION OF THE WINDOW, NAME AND BACKGROUND COLOR ##################################
########################################################################################################
ventana = turtle.Screen()                                                                        #######
ventana.title("PONG_AI v1.1")                                                                       #######
ventana.bgcolor("black")                                                                         #######
ventana.setup(width=800,height=400)                                                              #######
ventana.tracer(0)                                                                                #######
                                                                                                 #######
########################################################################################################
############################## CREATION OF BORDERS AND MIDDLE LINE #####################################
########################################################################################################                                                                                        #######
#If the window's width is 800, the range would be from -400 to 400                               #######
bordeSuperior = turtle.Turtle()                                                                  #######
bordeInferior = turtle.Turtle()                                                                  #######
lineaMedio = turtle.Turtle()                                                                     #######
                                                                                                 #######
bordeSuperior.color("white")
bordeSuperior.shape("square")
bordeSuperior.penup()
bordeSuperior.goto(0,ventana.window_height()/2)
bordeSuperior.shapesize(stretch_len=300, stretch_wid=2)

bordeInferior.color("white")
bordeInferior.shape("square")
bordeInferior.penup()
bordeInferior.goto(0,-ventana.window_height()/2)
bordeInferior.shapesize(stretch_len=300, stretch_wid=2)

lineaMedio.color("black")
lineaMedio.goto(0, ventana.window_height()/2)
lineaMedio.color("white")
lineaMedio.pensize(5)
lineaMedio.goto(0, -ventana.window_height()/2)
lineaMedio.pensize(30)

########################################################################################################
############################################## SCORE ###################################################
########################################################################################################
marcador = turtle.Turtle()
marcador.speed(0)
marcador.color("white")
marcador.hideturtle()
marcador.goto(0, ventana.window_height()/2 - 120)
marcador.write("0   0", align = "center", font=("Courier", 50, "bold"))

########################################################################################################
####################################### CREATION OF DELIMITERS #########################################
########################################################################################################
delimitadorArribaA = turtle.Turtle()
delimitadorArribaB = turtle.Turtle()
delimitadorAbajoA = turtle.Turtle()
delimitadorAbajoB = turtle.Turtle()

delimitadorArribaA.shape("square")
delimitadorArribaB.shape("square")
delimitadorAbajoA.shape("square")
delimitadorAbajoB.shape("square")

delimitadorArribaA.color("red")
delimitadorArribaB.color("red")
delimitadorAbajoA.color("red")
delimitadorAbajoB.color("red")

delimitadorArribaA.penup()
delimitadorArribaB.penup()
delimitadorAbajoA.penup()
delimitadorAbajoB.penup()

delimitadorArribaA.goto(-ventana.window_width()/2 + 20, ventana.window_height()/2)
delimitadorArribaB.goto(ventana.window_width()/2 - 20, ventana.window_height()/2)
delimitadorAbajoA.goto(-ventana.window_width()/2 + 20, -ventana.window_height()/2)
delimitadorAbajoB.goto(ventana.window_width()/2 - 20, -ventana.window_height()/2)
##########################################################################################
############################# CREATION OF THE BALL #######################################
##########################################################################################
bola = turtle.Turtle()
bola.speed(0)
bola.shape("circle")
bola.color("red")
bola.pensize(20)
bola.penup()
bola.goto(0,0)
bola.direction = "up"
bola.dx = 3
bola.dy = 3

##########################################################################################
######################### CREATION OF THE PLAYER RAQUETS #################################
##########################################################################################
raquetaA = turtle.Turtle()
raquetaA.speed(0)
raquetaA.shape("square")
raquetaA.color("white")
raquetaA.penup()
raquetaA.goto(-ventana.window_width()/2 + 20, 0)
raquetaA.shapesize(stretch_wid = 5, stretch_len = 0.5)

raquetaB = turtle.Turtle()
raquetaB.speed(0)
raquetaB.shape("square")
raquetaB.color("white")
raquetaB.penup()
raquetaB.goto(ventana.window_width()/2 - 20, 0)
raquetaB.shapesize(stretch_wid = 5, stretch_len = 0.5)

##########################################################################################
################################### UTIL FUNCTIONS #######################################
##########################################################################################
#Functions for calculating player's up and down movements,
def arribaB():
    if raquetaB.distance(delimitadorArribaB) > 80:
        y = raquetaB.ycor() + 25
        raquetaB.sety(y)

def abajoB():
    if raquetaB.distance(delimitadorAbajoB) > 80:
        y = raquetaB.ycor() - 25
        raquetaB.sety(y)

#Function that calculates the movement of the IA racket depending on the y coordenate of the ball
def moverIA():
    if bola.ycor() > 0 and raquetaA.distance(delimitadorArribaA) > 100 and raquetaA.ycor() < bola.ycor():
        y = raquetaA.ycor() + random.randint(1,10)
        raquetaA.sety(y)
    if bola.ycor() == 0 and raquetaA != 0:
        if raquetaA.ycor() < 0:
            y = raquetaA.ycor() + random.randint(1, 10)
            raquetaA.sety(y)
        if raquetaA.ycor() > 0:
            y = raquetaA.ycor() - random.randint(1, 10)
            raquetaA.sety(y)
    if bola.ycor() < 0 and raquetaA.distance(delimitadorAbajoA) > 100 and raquetaA.ycor() > bola.ycor():
        y = raquetaA.ycor() - random.randint(1,10)
        raquetaA.sety(y)



#Confirms if the ball is touching one of the borders
def comprobarColisionBordes():
    if bola.ycor() > ventana.window_height()/2 - 30:
        bola.dy *= -1
    if bola.ycor() < -ventana.window_height()/2 + 30:
        bola.dy *= -1

#Locates the rackets in the initial position
def formacionInicialRaquetas():
    raquetaA.goto(-ventana.window_width()/2 + 20, 0)
    raquetaB.goto(ventana.window_width() / 2 - 20, 0)

#Confirms if the ball is touching one of the goals
def comprobarPunto():
    global marcadorA
    global marcadorB
    if bola.xcor() > ventana.window_width()/2:
        marcadorA += 1
        marcador.clear()
        marcador.write(str(marcadorA) + "   " + str(marcadorB), align = "center", font=("Courier", 50, "bold"))
        formacionInicialRaquetas()
        bola.goto(0,0)
        time.sleep(1)
        bola.dx = 3
        bola.dx *= -1

    if bola.xcor() < -ventana.window_width()/2:
        marcadorB += 1
        marcador.clear()
        marcador.write(str(marcadorA) + "   " + str(marcadorB), align = "center", font=("Courier", 50, "bold"))
        formacionInicialRaquetas()
        bola.goto(0,0)
        time.sleep(1)
        bola.dx = -3
        bola.dx *= -1

#Confirms if the ball is touching one of the rackets
def comprobarColisionRaquetas():
    if 370 < bola.xcor() < 380 and bola.ycor() < raquetaB.ycor() + 70 and bola.ycor() > raquetaB.ycor() - 70:
        bola.dx = random.randint(2, 3)
        bola.dy = random.randint(-2, 2)
        bola.dx *= -3   #random.randint(1, 2)
        bola.dy *= -1 * random.randint(1, 2)

    if -370 > bola.xcor() > -380 and bola.ycor() < raquetaA.ycor() + 70 and bola.ycor() > raquetaA.ycor() - 70:
        bola.dx = -random.randint(2, 3)
        bola.dy = -1 * random.randint(-2, 2)
        bola.dx *= -3   #random.randint(1, 2)
        bola.dy *= -1 * random.randint(1, 2)

#Linking keyboard to player's movement
ventana.listen()
ventana.onkeypress(arribaB,"Up")
ventana.onkeypress(abajoB,"Down")

while True:
    ventana.update()
    time.sleep(0.01)
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    moverIA()
    comprobarColisionBordes()
    comprobarPunto()
    comprobarColisionRaquetas()

turtle.Screen().exitonclick()