import turtle
import time
import random
import pygame.mixer

# GLOBAL VARIABLES
marcadorA = 0
marcadorB = 0
PUNTUACION_MAX = 11

# TURTLE VARIABLES
ventana = turtle.Screen()
bordeSuperior = turtle.Turtle()
bordeInferior = turtle.Turtle()
lineaMedio = turtle.Turtle()
marcador = turtle.Turtle()
delimitadorArribaA = turtle.Turtle()
delimitadorArribaB = turtle.Turtle()
delimitadorAbajoA = turtle.Turtle()
delimitadorAbajoB = turtle.Turtle()
bola = turtle.Turtle()
raquetaA = turtle.Turtle()
raquetaB = turtle.Turtle()
bola.dx = 3
bola.dy = 3

#CREATION OF THE WINDOW, AND ALL WHAT IT WILL CONTAIN
def crearEntorno():

    #CREATION OF THE WINDOW, NAME AND BACKGROUND COLOR
    ventana.title("PONG v1.5")
    ventana.bgcolor("black")
    ventana.setup(width=800,height=400)
    ventana.tracer(0)

    #CREATION OF BORDERS AND MIDDLE LINE. If the window's width is 800, the range would be from -400 to 400
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

    #SCORE
    marcador.speed(0)
    marcador.color("white")
    marcador.hideturtle()
    marcador.goto(0, ventana.window_height()/2 - 120)
    marcador.write("0   0", align = "center", font=("Courier", 50, "bold"))

    #CREATION OF DELIMITERS
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

    #CREATION OF THE BALL
    bola.speed(0)
    bola.shape("circle")
    colorBola()
    bola.pensize(20)
    bola.penup()
    bola.goto(0,0)
    bola.direction = "up"

    #CREATION OF THE PLAYER RAQUETS
    raquetaA.speed(0)
    raquetaA.shape("square")
    raquetaA.color("white")
    raquetaA.penup()
    raquetaA.goto(-ventana.window_width()/2 + 20, 0)
    raquetaA.shapesize(stretch_wid = 5, stretch_len = 0.5)

    raquetaB.speed(0)
    raquetaB.shape("square")
    raquetaB.color("white")
    raquetaB.penup()
    raquetaB.goto(ventana.window_width()/2 - 20, 0)
    raquetaB.shapesize(stretch_wid = 5, stretch_len = 0.5)

#COLOR OF THE BALL IS TAKEN RANDOMLY
def colorBola():
    num = random.randint(0, 5)
    if num == 0:
        bola.color("green")
    if num == 1:
        bola.color("white")
    if num == 2:
        bola.color("blue")
    if num == 3:
        bola.color("red")
    if num == 4:
        bola.color("yellow")
    if num == 5:
        bola.color("pink")

#FUNCTION THAT CALCULATES THE MOVEMENT OF THE IA RACKET A DEPENDING ON THE Y COORDINATE OF THE BALL
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


#CONFIRMS IF THE BALL IS TOUCHING ONE OF THE BORDERS
def comprobarColisionBordes():
    if bola.ycor() > ventana.window_height()/2 - 30:
        bola.dy *= -1
        pygame.mixer.music.load("sounds/Rebote.ogg")
        pygame.mixer.music.play()
    if bola.ycor() < -ventana.window_height()/2 + 30:
        bola.dy *= -1
        pygame.mixer.music.load("sounds/Rebote.ogg")
        pygame.mixer.music.play()

#LOCATES THE RACKETS IN THE INITIAL POSITION
def formacionInicialRaquetas():
    raquetaA.goto(-ventana.window_width()/2 + 20, 0)
    raquetaB.goto(ventana.window_width() / 2 - 20, 0)

#CONFIRMS IF THE BALL IS TOUCHING ONE OF THE GOALS
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

#CONFIRMS IF THE BALL IS TOUCHING ONE OF THE RACKETS
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

#IT VERIFIES IF THE GAME HAS FINISHED
def finJuego():
    if (marcadorA == PUNTUACION_MAX or marcadorB == PUNTUACION_MAX):
        return True
    else:
        return False

#ANIMATIONS WHEN THE MATCH IS FINISHED
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

#FUNCTION WITH THE MAIN LOOP OF THE GAME THAT CHECK ALL THE STUFF
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

#MAIN
if __name__ == "__main__":
    crearEntorno()

    # Loop that permits playing more matches
    while True:
        pygame.init()
        juegoPong()

    turtle.Screen().exitonclick()



