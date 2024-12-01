"""
Programme jeu de la vie rÃ©alisÃ© par Gazi Damien
Version 0.1
"""
import pygame
from random import randint,uniform
from boutton import TextInput,Bouton
from math import *

#region------------------------------------------------------------__Init__-----------------------------------------------------------------------------------------
#variables de l'Ã©cran
WINDOWWIDTH = 1366
WINDOWHEIGHT = 700
CELLSIZE = 7


FPS=1000   #vitesse du jeu

ROUGE=(255,0,0)
NOIR=(0,0,0)
BLANC=(255,255,255)
VERT=(0,255,0)
BLEU=(0,0,125)
MAGENTA=(255,0,255)
cellcolor=(15,240,46)
grillecolor=NOIR
background_color=grillecolor


global nbCellHeight, nbCellWidth
nbCellWidth=WINDOWWIDTH//CELLSIZE
nbCellHeight=WINDOWHEIGHT//CELLSIZE

clock = pygame.time.Clock()
pygame.init()
fenetre = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption("Jeu de la vie")
font = pygame.font.Font('freesansbold.ttf', 20)
#endregion





#Trace la grille
def tracerGrille():
    for i in range(0,WINDOWWIDTH+1,CELLSIZE):
        pygame.draw.line(fenetre,grillecolor,(0+i,0),(0+i,700),1)
    for j in range(0,WINDOWHEIGHT+1,CELLSIZE):
        pygame.draw.line(fenetre,grillecolor,(0,0+j),(1366,0+j),1)
    pass


#initialise un dictionnaire de cellules CELLWIDTH*CELLHEIGHT {(0, 0): 0, (1, 0): 0, (2, 0): 0, (3, 0): 0, ....(17, 14): 0, (18, 14): 0, (19, 14): 0}
#les cellules seront toutes mortes
def initialiserCellules():
    return [[0 for i in range(nbCellHeight+1)] for j in range(nbCellWidth+1)]



#active alÃ©atoirement les cellules (mise Ã  1) {(0, 0): 0, (1, 0): 1, (2, 0): 1, (3, 0): 1, (4, 0): 1, etc...
def generationAleatoire():
    return [[uniform(-1.0,1.0) for i in range(nbCellHeight+1)] for j in range(nbCellWidth+1)]
    


#remplir la fenetre avec un rectangle vert si la cellule est vivante, noir sinon morte)

def remplirGrille(vie):
    for x in range(nbCellWidth):
        for y in range(nbCellHeight):
            value = max(0.0, min(1.0, vie[x][y]))
            intensity = int(value * 255)   
            color = (max(0,intensity-100), 0, max(0,intensity-50))
            pygame.draw.rect(fenetre, color, (x * CELLSIZE, y * CELLSIZE, CELLSIZE, CELLSIZE))

            
            
            

#DÃ©termine combien de voisins sont en vie
#rappel item est un tuple (x,y) contenant la position de la cellule.
def voisin(x, y, vie):
    nbvoisin = 0.0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = (x + dx) % nbCellWidth, (y + dy) % nbCellHeight
            nbvoisin += vie[nx][ny] * filtere[f"{dx},{dy}"]
    return nbvoisin
 




filtere = {
    "-1,-1": 0.1, "0,-1": -0.1, "1,-1": 0.3,
    "-1,0": 0.0, "0,0": 1.0, "1,0": -0.3,
    "-1,1": -0.5, "0,1": -0.1, "1,1": 0.2
}

textinput10 = TextInput(10, 370, 140, 32, 16)


def compile_activation(formula):
    try:
        code = compile(formula, "<string>", "eval")
        return lambda x: max(0.0, min(1.0, eval(code, {"x": x, "__builtins__": None})))
    except Exception as e:
        print(f"Failed to compile formula: {e}")
        return lambda x: 0.0  
    
textinput10.text="x"
activation_formula = compile_activation(textinput10.text)

def activation(x):
    return activation_formula(x)



#calcule la prochaine Ã©tape, retourne un nouveau dictionnaire

def prochaine_vie(vie):
    next_vie = [[0] * (nbCellHeight+1) for i in range(nbCellWidth+1)]
    
    for x in range(nbCellWidth):
        for y in range(nbCellHeight):

            next_vie[x][y] = activation(voisin(x, y, vie))

    return next_vie





vie=initialiserCellules()
#vie=generationAleatoire()


mousePressed1=False
mousePressed2=False
import time
timer = time.monotonic()
time_interval = 0.01
#region------------------------------------------------------------__Loop__-----------------------------------------------------------------------------------------
loop=True
run=True

textinput = TextInput(10, 10, 140, 32, 16)
textinput2 = TextInput(155, 10, 140, 32, 16)
textinput3 = TextInput(300, 10, 140, 32, 16)
textinput4 = TextInput(10, 50, 140, 32, 16)
textinput5 = TextInput(155, 50, 140, 32, 16)
textinput6 = TextInput(300, 50, 140, 32, 16)
textinput7 = TextInput(10, 90, 140, 32, 16)
textinput8 = TextInput(155, 90, 140, 32, 16)
textinput9 = TextInput(300, 90, 140, 32, 16)

Bouton1 = Bouton(10, 410, 140, 32, 'Start', (0, 0, 0), (255, 255, 255))
Bouton2 = Bouton(450, 10, 140, 32, 'Random', (0, 0, 0), (255, 255, 255))
txt=[textinput,textinput2,textinput3,textinput4,textinput5,textinput6,textinput7,textinput8,textinput9,textinput10]



textinput.text="0.1"
textinput2.text="-0.1"
textinput3.text="0.3"
textinput4.text="0.0"
textinput5.text="1.0"
textinput6.text="-0.3"
textinput7.text="-0.5"
textinput8.text="-0.1"
textinput9.text="0.2"
textinput10.text="x"

def menu():
    global filtere,activation_formula
    while True:
        
        fenetre.fill((0, 0, 0))
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()        
            
            elif event.type == pygame.KEYDOWN: 
                if event.key ==pygame.K_w:
                    pygame.quit()
                elif event.type == pygame.K_ESCAPE:
                    break
            for i in txt:
                i.analyse_event(event)        
                    
        if Bouton1.draw(fenetre):
            break     
                    
        if Bouton2.draw(fenetre):
            textinput.text=str(round(uniform(-1.0,1.0),2))
            textinput2.text=str(round(uniform(-1.0,1.0),2))
            textinput3.text=str(round(uniform(-1.0,1.0),2))
            textinput4.text=str(round(uniform(-1.0,1.0),2))
            textinput5.text=str(round(uniform(-1.0,1.0),2))
            textinput6.text=str(round(uniform(-1.0,1.0),2))
            textinput7.text=str(round(uniform(-1.0,1.0),2))
            textinput8.text=str(round(uniform(-1.0,1.0),2))
            textinput9.text=str(round(uniform(-1.0,1.0),2))
            
            
        
        
        
        for i in txt:
            i.draw(fenetre)
        
        pygame.display.update()
            
    for i in txt:
        if i.text!="":
            filtere = {
                "-1,-1": float(textinput.text), "0,-1": float(textinput2.text), "1,-1": float(textinput3.text),
                "-1,0": float(textinput4.text), "0,0": float(textinput5.text), "1,0": float(textinput6.text),
                "-1,1": float(textinput7.text), "0,1": float(textinput8.text), "1,1": float(textinput9.text)
            }
    activation_formula = compile_activation(textinput10.text)
    
menu()

while loop==True:
    mousepos=pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenetre (croix rouge)
        
        elif event.type == pygame.KEYDOWN:  #une touche a Ã©tÃ© pressÃ©e...laquelle ?
            if event.key == pygame.K_UP:    #est-ce la touche UP si animation est DéSACTIVER
                #vie=generationAleatoire(vie)
                vie=prochaine_vie(vie)     #manuel
            elif event.key ==pygame.K_w:
                loop=False
            
            elif event.key ==pygame.K_SPACE:
                run=not run
            
            elif event.key ==pygame.K_r:
                vie=generationAleatoire()
            elif event.key ==pygame.K_v:
                vie=initialiserCellules()
                
            elif event.key ==pygame.K_ESCAPE:
                menu()
            
            
            elif event.key ==pygame.K_PAGEUP:
                CELLSIZE+=1
                CELLWIDTH = WINDOWWIDTH // CELLSIZE
                CELLHEIGHT = WINDOWHEIGHT // CELLSIZE
                #fenetre = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
                vie=initialiserCellules()
                vie=generationAleatoire()
            elif event.key ==pygame.K_PAGEDOWN:
                if CELLSIZE>1:CELLSIZE-=1
                nbCellWidth = WINDOWWIDTH // CELLSIZE
                nbCellHeight = WINDOWHEIGHT // CELLSIZE
                #fenetre = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
                vie=initialiserCellules()
                vie=generationAleatoire()
                
            elif event.key ==pygame.K_RIGHT:
                if time_interval > 0.01: time_interval -= 0.1
            elif event.key ==pygame.K_LEFT:
                time_interval += 0.1
            
                
            
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                mousePressed1 = False
            elif event.button == 3:
                mousePressed2 = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mousePressed1 = True
            elif event.button == 3:
                mousePressed2 = True
            
    if mousepos[0]<nbCellWidth*CELLSIZE and mousepos[1]<nbCellHeight*CELLSIZE: 
        if mousePressed1:
            
            vie[mousepos[0]//CELLSIZE][mousepos[1]//CELLSIZE]=1
        if mousePressed2:
                vie[mousepos[0]//CELLSIZE][mousepos[1]//CELLSIZE]=0

    fenetre.fill(background_color)
    remplirGrille(vie)
    #tracerGrille()
    pygame.display.update() #mets Ã  jour la fentre graphique
    if run and  time.monotonic() - timer > time_interval:
        timer = time.monotonic()
        vie=prochaine_vie(vie)#clock.tick(FPS)

pygame.quit()

#endregion