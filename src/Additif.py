"""
Programme jeu de la vie rÃ©alisÃ© par nom, prÃ©nom, classe
"""
import pygame
from random import randint
#region------------------------------------------------------------__Init__-----------------------------------------------------------------------------------------
#variables de l'Ã©cran
WINDOWWIDTH = 1366
WINDOWHEIGHT = 700
CELLSIZE = 10


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
    vie=initialiserCellules()
    for i in range(nbCellWidth):
        for j in range(nbCellHeight):
            if randint(0,5)==1:
                vie[i][j]=randint(0,4)
    return vie
    
    

dictionairedescouleur={
    
    1:(200,200,200),      
    2:(150,150,150),        
    3:(100,100,100),       
    4:(50,50,50),        
    
}


#remplir la fenetre avec un rectangle vert si la cellule est vivante, noir sinon morte)

def remplirGrille(vie):
    c=30
    for x in range(nbCellWidth):
        for y in range(nbCellHeight):
            if vie[x][y]!=0:
                colo = (c*vie[x][y],c*vie[x][y],c*vie[x][y])
                #colo = (0,c*vie[x][y],0)
                pygame.draw.rect(fenetre, colo, (x*CELLSIZE, y*CELLSIZE, CELLSIZE, CELLSIZE))

            
    

#DÃ©termine combien de voisins sont en vie
#rappel item est un tuple (x,y) contenant la position de la cellule.
'''''
def voisins(item,vie):
    nbVoisins = 0
    for x in range (-1,2):
        for y in range (-1,2):
            xv=item[0]+x
            yv=item[1]+y

            
    return nbVoisins
    '''
def voisin(x, y, vie):
    nbvoisin = 0
    nbvoisin1 = 0
    nbvoisin2 = 0
    nbvoisin3 = 0
    nbvoisin4 = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = (x + dx) % nbCellWidth, (y + dy) % nbCellHeight
            if vie[nx][ny] != 0:
                nbvoisin += 1
            if vie[nx][ny] == 1:
                nbvoisin1 += 1
            if vie[nx][ny] == 2:
                nbvoisin2 += 1
            if vie[nx][ny] == 3:
                nbvoisin3 += 1
            if vie[nx][ny] == 4:    
                nbvoisin4 += 1
                
    return nbvoisin ,nbvoisin1,nbvoisin2,nbvoisin3,nbvoisin4
 
   

#calcule la prochaine Ã©tape, retourne un nouveau dictionnaire
def prochaine_vie(vie):
    next_vie = [[0] * (nbCellHeight+1) for i in range(nbCellWidth+1)]
    
    for x in range(nbCellWidth):
        for y in range(nbCellHeight):
            a, b, c,d,e= voisin(x, y, vie)
            
            
            
            next_vie[x][y] = (b+c+d+e) 
            
            


    return next_vie


vie=initialiserCellules()
#ie=generationAleatoire()


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
            elif event.key ==pygame.K_w:
                loop=False
            
            elif event.key ==pygame.K_SPACE:
                run=not run
            
            elif event.key ==pygame.K_v:
                vie=initialiserCellules()
            elif event.key ==pygame.K_r:
                vie=generationAleatoire()
                            
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