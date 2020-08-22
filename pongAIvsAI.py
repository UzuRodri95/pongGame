import turtle
import time
import random
import pygame.mixer

########################################################################################################
########################################## VARIABLES ###################################################
########################################################################################################
marcadorA = 0                                                                                    #######
marcadorB = 0                                                                                    #######
PUNTUACION_MAX = 11                                                                              #######
########################################################################################################
################### CREATION OF THE WINDOW, NAME AND BACKGROUND COLOR ##################################
########################################################################################################
pygame.init()                                                                                    #######
ventana = turtle.Screen()                                                                        #######
turtle.resizemode("noresize")                                                                    #######
ventana.title("PONG_AIvsAI v1.4")                                                                #######
ventana.bgcolor("black")                                                                         #######
ventana.setup(width=800,height=400)
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

delimitadorArribaA.color("white")
delimitadorArribaB.color("white")
delimitadorAbajoA.color("white")
delimitadorAbajoB.color("white")

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

#Function that calculates the movement of the IA racket A depending on the y coordenate of the ball
def moverIA_A():
    if bola.ycor() > 0 and raquetaA.distance(delimitadorArribaA) > 100 and raquetaA.ycor() < bola.ycor() and bola.xcor() < 0:
        y = raquetaA.ycor() + random.randint(1,15)
        raquetaA.sety(y)
    if bola.ycor() == 0 and raquetaA != 0:
        if raquetaA.ycor() < 0:
            y = raquetaA.ycor() + random.randint(1, 15)
            raquetaA.sety(y)
        if raquetaA.ycor() > 0:
            y = raquetaA.ycor() - random.randint(1, 15)
            raquetaA.sety(y)
    if bola.ycor() < 0 and raquetaA.distance(delimitadorAbajoA) > 100 and raquetaA.ycor() > bola.ycor() and bola.xcor() < 0:
        y = raquetaA.ycor() - random.randint(1,15)
        raquetaA.sety(y)

#Function that calculates the movement of the IA racket B depending on the y coordenate of the ball
def moverIA_B():
    if bola.ycor() > 0 and raquetaB.distance(delimitadorArribaB) > 100 and raquetaB.ycor() < bola.ycor() and bola.xcor() > 0:
        y = raquetaB.ycor() + random.randint(1,10)
        raquetaB.sety(y)
    if bola.ycor() == 0 and raquetaB != 0:
        if raquetaB.ycor() < 0:
            y = raquetaB.ycor() + random.randint(1, 10)
            raquetaB.sety(y)
        if raquetaB.ycor() > 0:
            y = raquetaB.ycor() - random.randint(1, 10)
            raquetaB.sety(y)
    if bola.ycor() < 0 and raquetaB.distance(delimitadorAbajoB) > 100 and raquetaB.ycor() > bola.ycor() and bola.xcor() > 0:
        y = raquetaB.ycor() - random.randint(1,10)
        raquetaB.sety(y)


#Confirms if the ball is touching one of the borders
def comprobarColisionBordes():
    if bola.ycor() > ventana.window_height()/2 - 30:
        bola.dy *= -1
        pygame.mixer.music.load("sounds/Rebote.ogg")
        pygame.mixer.music.play()
    if bola.ycor() < -ventana.window_height()/2 + 30:
        bola.dy *= -1
        pygame.mixer.music.load("sounds/Rebote.ogg")
        pygame.mixer.music.play()

#Locates the rackets in the initial position
def formacionInicialRaquetas():
    raquetaA.goto(-ventana.window_width()/2 + 20, 0)
    raquetaB.goto(ventana.window_width() / 2 - 20, 0)

#Confirms if the ball is touching one of the goals
def comprobarPunto():
    global marcadorA
    global marcadorB
    if bola.xcor() > ventana.window_width()/2:
        pygame.mixer.music.load("sounds/Gol.ogg")
        pygame.mixer.music.play()
        marcadorA += 1
        marcador.clear()
        marcador.write(str(marcadorA) + "   " + str(marcadorB), align = "center", font=("Courier", 50, "bold"))
        formacionInicialRaquetas()
        bola.goto(0,0)
        time.sleep(1)
        bola.dx = 3
        bola.dx *= -1


    if bola.xcor() < -ventana.window_width()/2:
        pygame.mixer.music.load("sounds/Gol.ogg")
        pygame.mixer.music.play()
        marcadorB += 1
        marcador.clear()
        marcador.write(str(marcadorA) + "   " + str(marcadorB), align = "center", font=("Courier", 50, "bold"))
        formacionInicialRaquetas()
        bola.goto(0,0)
        time.sleep(1)
        bola.dx = -3
        bola.dx *= -1

#Confirms if the ball is touching one of the rackets, in case there is collition here is given a physic to the ball
def comprobarColisionRaquetas():
    if 370 < bola.xcor() < 380 and bola.ycor() < raquetaB.ycor() + 70 and bola.ycor() > raquetaB.ycor() - 70:
        pygame.mixer.music.load("sounds/Raqueta.ogg")
        pygame.mixer.music.play()
        bola.dx = random.randint(2, 3)
        bola.dy = random.randint(-2, 2)
        bola.dx *= -3
        bola.dy *= -1 * random.randint(1, 2)

    if -370 > bola.xcor() > -380 and bola.ycor() < raquetaA.ycor() + 70 and bola.ycor() > raquetaA.ycor() - 70:
        pygame.mixer.music.load("sounds/Raqueta.ogg")
        pygame.mixer.music.play()
        bola.dx = -random.randint(2, 3)
        bola.dy = -1 * random.randint(-2, 2)
        bola.dx *= -3
        bola.dy *= -1 * random.randint(1, 2)

#It verifies if the game has finished
def finJuego():
    if (marcadorA == PUNTUACION_MAX or marcadorB == PUNTUACION_MAX):
        return True
    else:
        return False

#Aimations when the match is finished
def mostrarGanador():
    letraSize = 50
    if marcadorA == PUNTUACION_MAX or marcadorB == PUNTUACION_MAX:
        marcador.color("red")

        #Animation going up
        while marcador.distance(0,0) > 0:
            marcador.clear()
            time.sleep(0.1)
            y = marcador.ycor() - 10
            marcador.sety(y)
            marcador.write(str(marcadorA) + "   " + str(marcadorB), align = "center", font=("Courier",letraSize, "bold"))
            letraSize += 5

        #Blinking
        pygame.mixer.music.load("sounds/Winning.ogg")
        for _ in range(0,5):
            pygame.mixer.music.play()
            marcador.clear()
            marcador.write("   ", align="center", font=("Courier", letraSize, "bold"))
            time.sleep(0.5)
            marcador.write(str(marcadorA) + "   " + str(marcadorB), align = "center", font=("Courier",letraSize, "bold"))
            time.sleep(0.5)

        #Animation going back
        while marcador.distance(0,ventana.window_height()/2 - 120) > 0:
            marcador.clear()
            time.sleep(0.1)
            y = marcador.ycor() + 10
            marcador.sety(y)
            letraSize -= 5
            marcador.write(str(marcadorA) + "   " + str(marcadorB), align = "center", font=("Courier",letraSize, "bold"))

        #Turning to white score
        time.sleep(1)
        marcador.color("white")
        marcador.clear()
        marcador.write("0   0", align="center", font=("Courier", letraSize, "bold"))

#Function with the main loop of the game that check all the stuff
def juegoPong():
    global marcadorA
    global marcadorB
    while True:
        ventana.update()
        time.sleep(0.01)
        bola.setx(bola.xcor() + bola.dx)
        bola.sety(bola.ycor() + bola.dy)

        moverIA_A()
        moverIA_B()
        comprobarColisionBordes()
        comprobarColisionRaquetas()
        comprobarPunto()

        if finJuego():
            mostrarGanador()
            time.sleep(2)
            marcador.clear()
            marcador.write("0   0", align="center", font=("Courier", 50, "bold"))
            marcadorA = 0
            marcadorB = 0
            break

#Linking keyboard to player's movement
ventana.listen()
ventana.onkeypress(arribaB,"Up")
ventana.onkeypress(abajoB,"Down")

#Loop that permites playing more matches
while True:
    juegoPong()

turtle.Screen().exitonclick()

