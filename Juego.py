# 1 - Import library
import pygame
from pygame.locals import *
import os
import time
O=350
V=40
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (O,V)

#Inicio del Juego
pygame.init()
"Sonidos"
pygame.mixer.pre_init(44100, -16, 2, 2048)
#pygame.mixer.music.load("sonidos/instrumental.wav")
#pygame.mixer.music.load("sonidos/Power of NEO.mp3")
#pygame.mixer.music.play(5)

"Lineas "
#pygame.draw.line(screen,color,(80,80),(90,90),9)

"Tamano Pantallas"
width, height = 640, 650
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Primer Juego")
tiempodeactualizacion = pygame.time.Clock()

"Codigo de colores"
colornegro=(0,0,0)
colorgris=(200,200,200)
colorblanco=(255, 255, 255)

"Tipo de Letras"
fuentetitulo=pygame.font.SysFont("Arial",24,True,True)
fuentedeljuego=pygame.font.SysFont("Arial",13,True,True)
Titulo=fuentetitulo.render("Bienvenidos al Juego",0,(0,0,0))

"Rectagulo Intrucciones"
rectanguloderecho=pygame.Rect(500,0,300,640)
rectanguloarriba=pygame.Rect(10,5,200,30)

"imagenes"
imagefondo= pygame.image.load("imagenes/Fondo.png")
figuradeo= pygame.image.load("imagenes/figurao.png")
figuradex= pygame.image.load("imagenes/figurax.png")
blanco= pygame.image.load("imagenes/blanco.png")
ganadoro = pygame.image.load("imagenes/ganadoro.png")
ganadory = pygame.image.load("imagenes/ganadory.png")

"Posicion por defecto"
posicionx=500
posiciony=300
posicionmousex=0
posicionmousey=0

"Color de fondo de la pantalla"
screen.fill(colorblanco)

"Imagen de fondo"
screen.blit(imagefondo, (25, 100))

"Texto Instruciones"
instrucciones = fuentedeljuego.render("Instrucciones",0,(colornegro))
screen.blit(instrucciones, (500, 15))
enturno=fuentedeljuego.render("Jugador en Turno",0,(colornegro))
screen.blit(enturno, (520, 275))

"Comprobador de ganador jugador"
jugadorx=[]
jugadoro=[]

"Estado de las jugadas"
estadofigura = [False, False]

def click(numero):
    figura = blanco
    print (estadofigura)
    if mouse[0] == True and estadofigura[0] == False:
        figura = figuradeo
        screen.blit(blanco, (posicionx, posiciony))
        screen.blit(figura, (posicionx, posiciony))
        estadofigura[0] = True
        estadofigura[1] = False
        if numero != None:
            estado[numero] = True
            jugadoro.append(1+numero)
            jugadoro.sort()
            print("Jugador del O "+str(jugadoro))
            print(estado)
    if mouse[2] == True and estadofigura[1] == False:
        figura = figuradex
        screen.blit(blanco, (posicionx, posiciony))
        screen.blit(figura, (posicionx, posiciony))
        estadofigura[1] = True
        estadofigura[0] = False
        if numero!=None:
            estado[numero] = True
            jugadorx.append(1+numero)
            jugadorx.sort()
            print ("Jugador de la X "+str(jugadorx))
            print(estado)
    return figura

"Estados de las imagenes"
estado = [False,False,False,False,False,False,False,False,False]
# 4 - keep looping through
"Posiciones de las imagenes"
posicion1 = []
posicion2 = []
posicion3 = []
posicion4 = []
posicion5 = []
posicion6 = []
posicion7 = []
posicion8 = []
posicion9 = []

"creacion de cuadro de localizadorar"
for a in range (30,155,1):
    for b in range (120,225,1):
        #if not (a,b) in posicion1:
        posicion1.append((a,b))
        #if not (a,b) in posicion4:
        posicion4.append((150+a,b))
        # if not (a,b) in posicion7:
        posicion7.append((300+ a, b))

for a in range (30,155,1):
    for b in range (245,340,1):
        #if not (a,b) in posicion2:
        posicion2.append((a,b))
        #if not (a,b) in posicion5:
        posicion5.append((150+a,b))
        # if not (a,b) in posicion8:
        posicion8.append((300 + a, b))

for a in range (30,155,1):
    for b in range (415,530,1):
        #if not (a,b) in posicion3:
        posicion3.append((a,b))
        #if not (a,b) in posicion6:
        posicion6.append((150+a,b))
        # if not (a,b) in posicion9:
        posicion9.append((300 + a, b))

def ganador():
    resultado=None

    "Posibilidades de ganar"
    jugada1=[1,4,7]
    jugada2=[2,5,8]
    jugada3=[3,6,9]
    jugada4=[1,2,3]
    jugada5=[4,5,6]
    jugada6=[7,8,9]
    jugada7=[1,5,9]
    jugada8=[3,5,7]

    "Datos de la X"
    creador = []
    creador2 = []
    creador3 = []
    creador4 = []
    creador5 = []
    creador6 = []
    creador7 = []
    creador8 = []

    "Datos de la O"
    creadory = []
    creadory2 = []
    creadory3 = []
    creadory4 = []
    creadory5 = []
    creadory6 = []
    creadory7 = []
    creadory8 = []

    if len(jugadorx) <= 4 or len(jugadoro) <= 4:
        if jugadorx == jugada1 or jugadorx == jugada2 or jugadorx == jugada3 or jugadorx == jugada4 or jugadorx == jugada5 or jugadorx == jugada6 or jugadorx == jugada7 or jugadorx == jugada8:
            resultado = "Ganador el jugador de la X"
            screen.blit(ganadory, (25, 100))
        if jugadoro == jugada1 or jugadoro == jugada2 or jugadoro == jugada3 or jugadoro == jugada4 or jugadoro == jugada5 or jugadoro == jugada6 or jugadoro == jugada7 or jugadoro == jugada8:
            resultado = "Ganador el jugador de la O"
            screen.blit(ganadoro, (25, 100))
    if len(jugadorx) > 3 or len(jugadoro) > 3:
        for x in jugadorx:
            if x in jugada1:
                if x not in creador:
                    creador.append(x)
                    creador.sort()
            #print ("Posicion 1 " + str(creador))
            if x in jugada2:
                if x not in creador2:
                    creador2.append(x)
                    creador2.sort()
            #print "Posicion 2 " + str(creador2)
            if x in jugada3:
                if x not in creador3:
                    creador3.append(x)
                    creador3.sort()
            #print "Posicion 3 " + str(creador3)
            if x in jugada4:
                if x not in creador4:
                    creador4.append(x)
                    creador4.sort()
            #print "Posicion 4 " + str(creador4)
            if x in jugada5:
                if x not in creador5:
                    creador5.append(x)
                    creador5.sort()
            #print "Posicion 5 " + str(creador5)
            if x in jugada6:
                if x not in creador6:
                    creador6.append(x)
                    creador6.sort()
            #print "Posicion 6 " + str(creador6)
            if x in jugada7:
                if x not in creador7:
                    creador7.append(x)
                    creador7.sort()
            #print "Posicion 7 " + str(creador7)
            if x in jugada8:
                if x not in creador8:
                    creador8.append(x)
                    creador8.sort()
            #print "Posicion 8 " + str(creador8)
        for y in jugadoro:
            if y in jugada1:
                if y not in creadory:
                    creadory.append(y)
            if y in jugada2:
                if y not in creadory2:
                    creadory2.append(y)
            if y in jugada3:
                if y not in creadory3:
                    creadory3.append(y)
            if y in jugada4:
                if y not in creadory4:
                    creadory4.append(y)
            if y in jugada5:
                if y not in creadory5:
                    creadory5.append(y)
            if y in jugada6:
                if y not in creadory6:
                    creadory6.append(y)
            if y in jugada7:
                if y not in creadory7:
                    creadory7.append(y)
            if y in jugada8:
                if y not in creadory8:
                    creadory8.append(y)
            if creador == jugada1 or creador2 == jugada2 or creador3 == jugada3 or creador4 == jugada4 or creador5 == jugada5 or creador6 == jugada6 or creador7 == jugada7 or creador8 == jugada8:
                resultado = "Ganador el jugador de la X"
                screen.blit(ganadory, (25, 100))
            if creadory == jugada1 or creadory2 == jugada2 or creadory3 == jugada3 or creadory4 == jugada4 or creadory5 == jugada5 or creadory6 == jugada6 or creadory7 == jugada7 or creadory8 == jugada8:
                resultado = "Ganador el jugador de la O"
                screen.blit(ganadoro, (25, 100))
    return resultado



while True:
    "Titulo de Juego"
    screen.blit(Titulo, (150, 30))
    "Contador de Tiempo"
    pygame.draw.rect(screen,colorblanco,rectanguloarriba)
    tiempojuego = (pygame.time.get_ticks() / 1000)
    tiempojuego = str(tiempojuego)
    if float(tiempojuego) <=60:
        contadortiempo = fuentedeljuego.render("Tiempo de Juego "+tiempojuego[:2]+" Segundos", 0, (colornegro))
    else:
        tiempojuego=float(tiempojuego)/60
        tiempojuego=str(tiempojuego)
        contadortiempo = fuentedeljuego.render("Tiempo de Juego: " + tiempojuego[:4] + " Minutos", 0, (colornegro))
    "Tiempo de juego"
    screen.blit(contadortiempo,(10,5))
    "Mover Imagen Mouse"
    mouse = pygame.mouse.get_pressed()
    posicion=pygame.mouse.get_pos(posicionmousex, posicionmousey)
    velocidad=20
    if ganador()!=None:
        velocidad=5
    if len(jugadorx)>=5 or len(jugadoro)>=5:
        break
    else:
        "Sentencias de colocacion de la x y o"
        if posicion in posicion1 and mouse[0] == True or posicion in posicion1 and mouse[2] == True:
            if estado[0] == False:
                numero=0
                valor = click(numero)
                screen.blit(valor, (30, 105))

        if posicion in posicion2 and mouse[0] == True or posicion in posicion2 and mouse[2] == True:
            if estado[1] == False:
                numero = 1
                valor2 = click(numero)
                screen.blit(valor2, (30, 260))

        if posicion in posicion3 and mouse[0] == True or posicion in posicion3 and mouse[2] == True:
            if estado[2] == False:
                numero = 2
                valor3 = click(numero)
                screen.blit(valor3, (30,420))

        if posicion in posicion4 and mouse[0] == True or posicion in posicion4 and mouse[2] == True:
            if estado[3] == False:
                numero = 3
                valor4 = click(numero)
                screen.blit(valor4, (180, 105))

        if posicion in posicion5 and mouse[0] == True or posicion in posicion5 and mouse[2] == True:
            if estado[4] == False:
                numero = 4
                valor5 = click(numero)
                screen.blit(valor5, (180, 260))

        if posicion in posicion6 and mouse[0] == True or posicion in posicion6 and mouse[2] == True:
            if estado[5] == False:
                numero = 5
                valor6 = click(numero)
                screen.blit(valor6, (180, 420))

        if posicion in posicion7 and mouse[0] == True or posicion in posicion7 and mouse[2] == True:
            if estado[6] == False:
                numero = 6
                valor7 = click(numero)
                screen.blit(valor7, (335, 105))

        if posicion in posicion8 and mouse[0] == True or posicion in posicion8 and mouse[2] == True:
            if estado[7] == False:
                numero = 7
                valor8 = click(numero)
                screen.blit(valor8, (335, 260))

        if posicion in posicion9 and mouse[0] == True or posicion in posicion9 and mouse[2] == True:
            if estado[8] == False:
                numero = 8
                valor9 = click(numero)
                screen.blit(valor9, (335, 420))
    numero=None
    pygame.display.flip()
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)
    tiempodeactualizacion.tick(velocidad)
