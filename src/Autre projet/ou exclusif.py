#Projet : Pi's Py Art
#Auteurs : Damien Gazi
import pygame
from random import randint,choice
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
CELLSIZE = 1

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
    return [[0 for _ in range(nbCellHeight+1)] for _ in range(nbCellWidth+1)]



#active alÃ©atoirement les cellules (mise Ã  1) {(0, 0): 0, (1, 0): 1, (2, 0): 1, (3, 0): 1, (4, 0): 1, etc...
def generationAleatoire():
    return [[randint(0,1) for _ in range(nbCellHeight+1)] for _ in range(nbCellWidth+1)]
    


#remplir la fenetre avec un rectangle vert si la cellule est vivante, noir sinon morte)
def remplirGrille(vie):
    
    for x in range(nbCellWidth):
        for y in range(nbCellHeight):
            if vie[x][y]:
                pygame.draw.rect(fenetre, cellcolor, (x*CELLSIZE, y*CELLSIZE, CELLSIZE, CELLSIZE))
    

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
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < nbCellWidth and 0 <= ny < nbCellWidth:
                nbvoisin += vie[nx][ny]
    return nbvoisin
 
    return nbVoisins


    



#calcule la prochaine Ã©tape, retourne un nouveau dictionnaire
def prochaine_vie(vie):
    #next_vie = [[0] * (nbCellHeight+1) for _ in range(nbCellWidth+1)]
    
    for x in range(nbCellWidth):
        for y in range(nbCellHeight):
            #a = voisin(x, y, vie)
            #game of life
            """if a==2:   next_vie[x][y] = vie[x][y] 
            elif a==3: next_vie[x][y] = 1
            elif a<2:  next_vie[x][y] = 0
            elif a>3:  next_vie[x][y] = 0"""
            try:
                a=vie[x][y]
                b=vie[x-1][y]
            except:
                print('out of range')
            
            if a+b == 1:
                vie[x][y+1] = 1
                
                
            
            
            
                
            

    return vie#next_vie


vie=initialiserCellules()
vie[1][1]=1
#vie=generationAleatoire()
vie=prochaine_vie(vie)
seclecteur=1
mousePressed1=False
mousePressed2=False
#region------------------------------------------------------------__Loop__-----------------------------------------------------------------------------------------
loop=True
run=True
mousePressed = False
import time
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
            
            elif event.key ==pygame.K_r:
                vie=initialiserCellules()
                
            elif event.key ==pygame.K_g:
                vie=generationAleatoire()
            elif event.key ==pygame.K_PAGEUP:
                CELLSIZE+=1
                CELLWIDTH = WINDOWWIDTH // CELLSIZE
                CELLHEIGHT = WINDOWHEIGHT // CELLSIZE
                #fenetre = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
                vie=initialiserCellules()
                vie[1][1]=1
                vie=prochaine_vie(vie)
            elif event.key ==pygame.K_PAGEDOWN:
                if CELLSIZE>1:CELLSIZE-=1
                nbCellWidth = WINDOWWIDTH // CELLSIZE
                nbCellHeight = WINDOWHEIGHT // CELLSIZE
                #fenetre = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
                vie=initialiserCellules()
                vie[1][1]=1
                vie=prochaine_vie(vie)
            
        
            
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
            vie[mousepos[0]//CELLSIZE][mousepos[1]//CELLSIZE]=seclecteur
            vie=prochaine_vie(vie)
        elif mousePressed2:
            vie[mousepos[0]//CELLSIZE][mousepos[1]//CELLSIZE]=0
            
            
    fenetre.fill(background_color)
    remplirGrille(vie)
    #tracerGrille()
    pygame.display.update() #mets Ã  jour la fentre graphique
    #if run :vie=prochaine_vie(vie)#;time.sleep(0.1)  #pour une animation !!!!!!
    #clock.tick(FPS)

pygame.quit()

#endregion