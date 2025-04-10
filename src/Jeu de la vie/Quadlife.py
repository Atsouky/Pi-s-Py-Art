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
    return [[0 for i in range(nbCellHeight+1)] for j in range(nbCellWidth+1)]



#active alÃ©atoirement les cellules (mise Ã  1) {(0, 0): 0, (1, 0): 1, (2, 0): 1, (3, 0): 1, (4, 0): 1, etc...
def generationAleatoire():
    vie=initialiserCellules()
    for i in range(nbCellWidth):
        for j in range(nbCellHeight):
            if randint(0,5)==1:
                vie[i][j]=randint(0,4)
    return vie
    
    

    


#remplir la fenetre avec un rectangle vert si la cellule est vivante, noir sinon morte)
def remplirGrille(vie):
    
    for x in range(nbCellWidth):
        for y in range(nbCellHeight):
            if vie[x][y]==1:
                pygame.draw.rect(fenetre, cellcolor, (x*CELLSIZE, y*CELLSIZE, CELLSIZE, CELLSIZE))
            elif vie[x][y]==2:
                pygame.draw.rect(fenetre, (255,0,0), (x*CELLSIZE, y*CELLSIZE, CELLSIZE, CELLSIZE))
            elif vie[x][y]==3:
                pygame.draw.rect(fenetre, (255,255,0), (x*CELLSIZE, y*CELLSIZE, CELLSIZE, CELLSIZE))
            elif vie[x][y]==4:
                pygame.draw.rect(fenetre, (255,0,255), (x*CELLSIZE, y*CELLSIZE, CELLSIZE, CELLSIZE))

            
    

#DÃ©termine combien de voisins sont en vie

    
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
            
            if a==3 : 
                if b > c and b > d and b > e:
                    next_vie[x][y] = 1
                elif c > b and c > d and c > e:
                    next_vie[x][y] = 2
                elif d > b and d > c and d > e:
                    next_vie[x][y] = 3
                elif e > b and e > c and e > d:
                    next_vie[x][y] = 4
                elif b==0:
                    next_vie[x][y] = 1
                elif c==0:
                    next_vie[x][y] = 2
                elif d==0:
                    next_vie[x][y] = 3
                elif e==0:
                    next_vie[x][y] = 4
                
            elif a==3 or a==2 : next_vie[x][y] = vie[x][y]
            
            else: next_vie[x][y] = 0

    return next_vie


vie=initialiserCellules()
vie=generationAleatoire()


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