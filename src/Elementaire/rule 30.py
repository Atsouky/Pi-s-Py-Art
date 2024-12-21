"""
Programme jeu de la vie rÃ©alisÃ© par nom, prÃ©nom, classe
"""
import pygame
from random import randint,choice
#region------------------------------------------------------------__Init__-----------------------------------------------------------------------------------------
#variables de l'Ã©cran
WINDOWWIDTH = 1366
WINDOWHEIGHT = 700
CELLSIZE = 1
CELLWIDTH = WINDOWWIDTH // CELLSIZE
CELLHEIGHT = WINDOWHEIGHT // CELLSIZE

FPS=1000   #vitesse du jeu

ROUGE=(255,0,0)
NOIR=(0,0,0)
BLANC=(255,255,255)
VERT=(0,255,0)
BLEU=(0,0,125)
MAGENTA=(255,0,255)
cellcolor=(15,240,46)
cellcolor = (0,0,255)
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
    return [0 for i in range(nbCellWidth)]



#active alÃ©atoirement les cellules (mise Ã  1) {(0, 0): 0, (1, 0): 1, (2, 0): 1, (3, 0): 1, (4, 0): 1, etc...
def generationAleatoire(vie):
    for i in range(nbCellWidth):
        vie[i] = randint(0, 1)
    return vie
    


#remplir la fenetre avec un rectangle vert si la cellule est vivante, noir sinon morte)
def remplirGrille(vie):
    for y in range(nbCellHeight):
        for x in range(nbCellWidth):
            if vie[y][x]:
                pygame.draw.rect(fenetre, cellcolor, (x * CELLSIZE, y * CELLSIZE, CELLSIZE, CELLSIZE))


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
    x0 = 0
    x1=0
    x2=0
    if vie[x-1][y]==1: x0=1
    if vie[x][y]==1: x1=1
    if vie[x+1][y]==1: x2=1
    
    return str(x0)+str(x1)+str(x2)
 
 


rule30 = {
    
    '000':0,
    '001':1,
    '010':1,
    '011':1,
    '100':1,
    '101':0,
    '110':0,
    '111':0
    
}


rule110 = {
    
    '000':0,
    '001':1,
    '010':1,
    '011':1,
    '100':0,
    '101':1,
    '110':1,
    '111':0
    
}

rule184={
    
    '000':0,
    '001':0,
    '010':0,
    '011':1,
    '100':1,
    '101':1,
    '110':0,
    '111':1
}


#calcule la prochaine Ã©tape, retourne un nouveau dictionnaire
"""def prochaine_vie(vie,y):
    #next_vie = [[0] * (nbCellHeight+1) for _ in range(nbCellWidth+1)]
    
    
    for x in range(1,nbCellWidth):
        #a = voisin(x, y, vie)
        
        
        
        a =voisin(x, y, vie)
        #print(a)
        vie[x][y-1] = rule30[a]

    return vie#next_vie"""

def prochaine_vie(vie, row_index):# aide par vous savez qui
    next_row = [0] * nbCellWidth  
    for x in range(1, nbCellWidth - 1):  
        pattern = str(vie[row_index][x - 1]) + str(vie[row_index][x]) + str(vie[row_index][x + 1])  
        next_row[x] = rule184.get(pattern, 0)  
    return next_row

vie = [initialiserCellules() for i in range(nbCellHeight)] 
vie[0] = generationAleatoire(vie[0])
#vie=generationAleatoire()



seclecteur=1
mousePressed1=False
mousePressed2=False


#region------------------------------------------------------------__Loop__-----------------------------------------------------------------------------------------
loop=True
run=False
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
            elif event.key ==pygame.K_w:
                loop=False
            
            elif event.key ==pygame.K_SPACE:
                run=not run
            
            elif event.key ==pygame.K_r:
                vie = [initialiserCellules() for i in range(nbCellHeight)]  
                vie[0] = generationAleatoire(vie[0])
                
            elif event.key ==pygame.K_PAGEUP:
                CELLSIZE+=1
                CELLWIDTH = WINDOWWIDTH // CELLSIZE
                CELLHEIGHT = WINDOWHEIGHT // CELLSIZE
                #fenetre = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
                vie = [initialiserCellules() for i in range(nbCellHeight)] 
                vie[0] = generationAleatoire(vie[0])
            elif event.key ==pygame.K_PAGEDOWN:
                if CELLSIZE>1:CELLSIZE-=1
                nbCellWidth = WINDOWWIDTH // CELLSIZE
                nbCellHeight = WINDOWHEIGHT // CELLSIZE
                #fenetre = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
                vie = [initialiserCellules() for i in range(nbCellHeight)]  
                vie[0] = generationAleatoire(vie[0])
                
                

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
                
    """if mousepos[0]<nbCellWidth*CELLSIZE and mousepos[1]<nbCellHeight*CELLSIZE:
        if mousePressed1:
            vie[mousepos[0]//CELLSIZE][mousepos[1]//CELLSIZE]=seclecteur
            vie=prochaine_vie(vie,y)
        elif mousePressed2:
            vie[mousepos[0]//CELLSIZE][mousepos[1]//CELLSIZE]=0
            """ 
            
    fenetre.fill(background_color)
    remplirGrille(vie)
    #tracerGrille()
    for i in range(1, nbCellHeight):
            vie[i] = prochaine_vie(vie, i - 1)
    
    #time.sleep(1)
    pygame.display.update() #mets Ã  jour la fentre graphique
    #if run :vie=prochaine_vie(vie)#;time.sleep(0.1)  #pour une animation !!!!!!
    #clock.tick(FPS)

pygame.quit()

#endregion