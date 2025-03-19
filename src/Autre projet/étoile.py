#Projet : Pi's Py Art
#Auteurs : Damien Gazi
import pygame
from random import randint
#region------------------------------------------------------------__Init__-----------------------------------------------------------------------------------------
# pygame initialisation
clock = pygame.time.Clock()
pygame.init()
fenetre = pygame.display.set_mode((0, 0), pygame.NOFRAME)
pygame.display.set_caption("Jeu de la vie")
font = pygame.font.Font('freesansbold.ttf', 20)

# Variables de l'écran
info = pygame.display.get_surface().get_size()
cellcolor = (0, 255, 0)
CELLSIZE = 10

#offset de la écran
offset_x = 0
offset_y = 0

nbCellWidth=info[0]//CELLSIZE
nbCellHeight=info[1]//CELLSIZE
background_color = (0, 0, 0)
WINDOWWIDTH = info[0]
WINDOWHEIGHT = info[1]


#initialise un dictionnaire de cellules CELLWIDTH*CELLHEIGHT {(0, 0): 0, (1, 0): 0, (2, 0): 0, (3, 0): 0, ....(17, 14): 0, (18, 14): 0, (19, 14): 0}
#les cellules seront toutes mortes
def initialiserCellules():
    return [[[0,0,0] for i in range(nbCellHeight+1)] for j in range(nbCellWidth+1)]



#active alÃ©atoirement les cellules (mise Ã  1) {(0, 0): 0, (1, 0): 1, (2, 0): 1, (3, 0): 1, (4, 0): 1, etc...
def generationAleatoire():
    return [[[randint(0,255),randint(0,255),randint(0,255)] for i in range(nbCellHeight+1)] for j in range(nbCellWidth+1)]
    


#remplir la fenetre avec un rectangle vert si la cellule est vivante, noir sinon morte)
def remplirGrille(vie):
    
    for x in range(nbCellWidth):
        for y in range(nbCellHeight):
            if vie[x][y]!=0:
                pygame.draw.rect(fenetre, vie[x][y], (x*CELLSIZE, y*CELLSIZE, CELLSIZE, CELLSIZE))
    

#DÃ©termine combien de voisins sont en vie
#rappel item est un tuple (x,y) contenant la position de la cellule.

def voisin(x, y, vie):
    nbvoisin = 0
    for dx, dy in [ (-1, 0), (0, -1), (0, 1), (1, 0)]:
        
        nx, ny = (x + dx) % nbCellWidth, (y + dy) % nbCellHeight
        nbvoisin += vie[nx][ny]
    return nbvoisin

def mutation(color):
    
    return [
        max(0, min(255, color[0] + randint(-mutation_prob, mutation_prob))),
        max(0, min(255, color[1] + randint(-mutation_prob, mutation_prob))),
        max(0, min(255, color[2] + randint(-mutation_prob, mutation_prob)))
    ]

#calcule la prochaine Ã©tape, retourne un nouveau dictionnaire
def prochaine_vie(vie):
    next_vie = [[0,0,0] * (nbCellHeight+1) for i in range(nbCellWidth+1)]
    
    for x in range(nbCellWidth):
        for y in range(nbCellHeight):
            
            if vie[x][y]!=0:
                for dx, dy in [ (-1, 0), (0, -1), (0, 1), (1, 0)]:
        
                    nx, ny = (x + dx) % nbCellWidth, (y + dy) % nbCellHeight
                    if randint(0, 100) < chance_mutation:
                        next_vie[nx][ny] = mutation(vie[x][y])
                    else :
                        next_vie[nx][ny] = vie[x][y]
            

    return next_vie

mutation_prob = 15
chance_mutation = 0.6


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
while loop==True:
    mousepos=pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenetre (croix rouge)
        
        elif event.type == pygame.KEYDOWN:  #une touche a Ã©tÃ© pressÃ©e...laquelle ?
            if event.key == pygame.K_UP:    #est-ce la touche UP si animation est DéSACTIVER
                #vie=generationAleatoire(vie)
                vie=prochaine_vie(vie)     #manuel
            elif event.key ==pygame.K_ESCAPE:
                loop=False
            
            elif event.key ==pygame.K_SPACE:
                run=not run
            
            elif event.key ==pygame.K_v:
                vie=initialiserCellules()
            elif event.key ==pygame.K_r:
                vie=generationAleatoire()
                
            elif event.key ==pygame.K_RIGHT:
                if time_interval > 0.01: time_interval -= 0.1
            elif event.key ==pygame.K_LEFT:
                time_interval += 0.1
            
                
                
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
            
            vie[mousepos[0]//CELLSIZE][mousepos[1]//CELLSIZE]=[0,0,255]
        if mousePressed2:
                vie[mousepos[0]//CELLSIZE][mousepos[1]//CELLSIZE]=0

    fenetre.fill(background_color)
    remplirGrille(vie)
    #tracerGrille()
    pygame.display.update() #mets Ã  jour la fentre graphique
    if run and  time.monotonic() - timer > time_interval:
        timer = time.monotonic()
        vie=prochaine_vie(vie)
    #if run :vie=prochaine_vie(vie)  #pour une animation !!!!!!
    #clock.tick(FPS)

pygame.quit()

#endregion