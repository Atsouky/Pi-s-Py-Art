"""
Programme jeu de la vie rÃ©alisÃ© par Gazi Damien Tg3
"""

#Day & Night

import pygame , time
from random import randint
<<<<<<< HEAD
#region------------------------------------------------------------__Init__----------------------------------------------------------------
=======
#region------------------------------------------------------------__Init__-----------------------------------------------------------------------------------------
>>>>>>> 74773e15971563ae9225f20f689744483673ef24



cellcolor = (0,255,0)

clock = pygame.time.Clock()
pygame.init()

display_info = pygame.display.Info()
l = display_info.current_w
h = display_info.current_h - 50 #pour la barre de menu windows

fenetre = pygame.display.set_mode((l,h), pygame.RESIZABLE)

<<<<<<< HEAD
pygame.display.set_caption("Day&Night")
=======
pygame.display.set_caption("Lab3")
>>>>>>> 74773e15971563ae9225f20f689744483673ef24
font = pygame.font.Font('freesansbold.ttf', 20)

#variables de l'écran
WINDOWWIDTH = l
WINDOWHEIGHT = h
<<<<<<< HEAD
CELLSIZE = 1
populace=1
CELLWIDTH = WINDOWWIDTH // CELLSIZE
CELLHEIGHT = WINDOWHEIGHT // CELLSIZE
=======
CELLSIZE = 3
>>>>>>> 74773e15971563ae9225f20f689744483673ef24

global nbCellHeight, nbCellWidth
nbCellWidth=WINDOWWIDTH//CELLSIZE
nbCellHeight=WINDOWHEIGHT//CELLSIZE


#endregion

<<<<<<< HEAD
def initialiserCellules():
    return []

def generationAleatoire(rd,vie):
    viee=vie
    for x in range(nbCellWidth):
        for y in range(nbCellHeight):
            if randint(0,rd)==1:
                viee.append((x,y))
        
    return viee
=======


#Initialiste tout les cellule a 0 en faisant des listes de listes: return liste[x][y]
def initialiserCellules() -> list:
    return [[0 for i in range(nbCellHeight+1)] for j in range(nbCellWidth+1)]


#Initialiste tout les cellule a 0 ou 1 aleatoirement en faisant des listes de listes:  return liste[x][y]
def generationAleatoire() -> list:
    return [[randint(0,N) for i in range(nbCellHeight+1)] for j in range(nbCellWidth+1)]
>>>>>>> 74773e15971563ae9225f20f689744483673ef24
    


#remplir la fenetre avec un rectangle vert si la cellule est vivante, sinon noir
def remplirGrille(vie):
<<<<<<< HEAD
    for i,j in vie:
        pygame.draw.rect(fenetre, cellcolor, (i*CELLSIZE, j*CELLSIZE, CELLSIZE, CELLSIZE))
=======
    for x in range(nbCellWidth):
        for y in range(nbCellHeight):
            if vie[x][y] <10:
                pygame.draw.rect(fenetre, (0,0,0), (x*CELLSIZE, y*CELLSIZE, CELLSIZE, CELLSIZE))
            elif 10 <vie[x][y] < 20:
                pygame.draw.rect(fenetre, (255,0,0), (x*CELLSIZE, y*CELLSIZE, CELLSIZE, CELLSIZE))
            elif 20 <vie[x][y] < 30:
                pygame.draw.rect(fenetre, (0,100,0), (x*CELLSIZE, y*CELLSIZE, CELLSIZE, CELLSIZE))
            elif 30 <vie[x][y] < 40:
                pygame.draw.rect(fenetre, (0,255,0), (x*CELLSIZE, y*CELLSIZE, CELLSIZE, CELLSIZE))
            elif 40 <vie[x][y] < 50:
                pygame.draw.rect(fenetre, (100,100,0), (x*CELLSIZE, y*CELLSIZE, CELLSIZE, CELLSIZE))
            elif 50 <vie[x][y] < 60:
                pygame.draw.rect(fenetre, (100,255,0), (x*CELLSIZE, y*CELLSIZE, CELLSIZE, CELLSIZE))
            elif 60 <vie[x][y] < 70:
                pygame.draw.rect(fenetre, (255,100,0), (x*CELLSIZE, y*CELLSIZE, CELLSIZE, CELLSIZE))
            elif 70 <vie[x][y] < 80:
                pygame.draw.rect(fenetre, (255,255,0), (x*CELLSIZE, y*CELLSIZE, CELLSIZE, CELLSIZE))
            elif 80 <vie[x][y] < 90:
                pygame.draw.rect(fenetre, (0,0,100), (x*CELLSIZE, y*CELLSIZE, CELLSIZE, CELLSIZE))
            elif 90 <vie[x][y] < 100:
                pygame.draw.rect(fenetre, (0,0,255), (x*CELLSIZE, y*CELLSIZE, CELLSIZE, CELLSIZE))
                
>>>>>>> 74773e15971563ae9225f20f689744483673ef24
    

#Compte le nombre de voisins vivant autoure d'une cellule --> ici 8 voisins
#Bordure type portail
def voisin(x, y, vie):
    nbvoisin = 0
<<<<<<< HEAD
    for dx,dy in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
        if ((dx+x)%nbCellWidth,(dy+y)%nbCellHeight) in vie:
            nbvoisin+=1
=======
    for dx ,dy in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
        nx, ny = (x + dx) % nbCellWidth, (y + dy) % nbCellHeight
        nbvoisin += vie[nx][ny]
>>>>>>> 74773e15971563ae9225f20f689744483673ef24
    return nbvoisin

#Calacul de la prochaine generation en fonction du nombre de voisins
def prochaine_vie(vie):
<<<<<<< HEAD
    next_vie = []
    candidates = set(vie) | {
        (x + dx, y + dy)
        for x, y in vie
        for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    }

    for cell in candidates:
        voisins = voisin(cell[0], cell[1], vie)
        if (cell in vie and voisins in [2, 3]) or (cell not in vie and voisins == 3):
            next_vie.append(cell)
    
=======
    next_vie = [[0] * (nbCellHeight+1) for i in range(nbCellWidth+1)]
    
    for x in range(nbCellWidth):
        for y in range(nbCellHeight):
            a = voisin(x, y, vie)
            
            if a % 3 == 0:
                next_vie[x][y] = vie[x][y] +1 
            elif a % 2 == 1:
                next_vie[x][y] = a/2
                
>>>>>>> 74773e15971563ae9225f20f689744483673ef24

    return next_vie



<<<<<<< HEAD
#region------------------------------------------------------------__Loop__-------------------------------------------------------------


vie=initialiserCellules()
#vie=generationAleatoire(populace,vie)
#print(vie)
=======
#region------------------------------------------------------------__Loop__-----------------------------------------------------------------------------------------

N=100
epsi = 7
vie=initialiserCellules()
vie=generationAleatoire()
>>>>>>> 74773e15971563ae9225f20f689744483673ef24
mousePressed1=False
mousePressed2=False
timer = time.monotonic()
time_interval = 0.01
loop=True
run=True

while loop==True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:           #fermeture du jeu
            loop = False            
        
        elif event.type == pygame.KEYDOWN:      # Vérifie les touches appuyées
            
            if event.key ==pygame.K_w:          #fermeture du jeu
                loop=False
            
            elif event.key ==pygame.K_SPACE:    #activer/desactiver pause
                run=not run
            
            elif event.key ==pygame.K_v:        #vider la grille
                vie=initialiserCellules()
            elif event.key ==pygame.K_r:        #remplir la grille aléatoirement
<<<<<<< HEAD
                vie=generationAleatoire(populace,vie)
=======
                vie=generationAleatoire()
>>>>>>> 74773e15971563ae9225f20f689744483673ef24
                
            elif event.key ==pygame.K_RIGHT:    #augmenter la vitesse
                if time_interval > 0.01: time_interval -= 0.1
            elif event.key ==pygame.K_LEFT:     #diminuer la vitesse
                time_interval += 0.1
            
                
                
            elif event.key ==pygame.K_PAGEUP:   #augmenter la taille de la grille
                CELLSIZE+=1
                CELLWIDTH = WINDOWWIDTH // CELLSIZE
                CELLHEIGHT = WINDOWHEIGHT // CELLSIZE
                vie=initialiserCellules()
<<<<<<< HEAD
                vie=generationAleatoire(populace,vie)
=======
                vie=generationAleatoire()
>>>>>>> 74773e15971563ae9225f20f689744483673ef24
            elif event.key ==pygame.K_PAGEDOWN:   #diminuer la taille de la grille
                if CELLSIZE>1:CELLSIZE-=1
                nbCellWidth = WINDOWWIDTH // CELLSIZE
                nbCellHeight = WINDOWHEIGHT // CELLSIZE
                vie=initialiserCellules()
<<<<<<< HEAD
                vie=generationAleatoire(populace,vie)
=======
                vie=generationAleatoire()
>>>>>>> 74773e15971563ae9225f20f689744483673ef24
                            
        elif event.type == pygame.MOUSEBUTTONUP:    #Vérifie si un bouton de la souris est appuyé
            if event.button == 1:
                mousePressed1 = False
            elif event.button == 3:
                mousePressed2 = False
        elif event.type == pygame.MOUSEBUTTONDOWN: #Vérifie si un bouton de la souris est relache
            if event.button == 1:
                mousePressed1 = True
            elif event.button == 3:
                mousePressed2 = True
    
    mousepos=pygame.mouse.get_pos()
         
    if mousepos[0]<nbCellWidth*CELLSIZE and mousepos[1]<nbCellHeight*CELLSIZE: 
        if mousePressed1:
<<<<<<< HEAD
            print((mousepos[0]//CELLSIZE,mousepos[1]//CELLSIZE))
            vie.append((mousepos[0]//CELLSIZE,mousepos[1]//CELLSIZE))
        if mousePressed2 and (mousepos[0]//CELLSIZE,mousepos[1]//CELLSIZE) in vie:
            vie.remove((mousepos[0]//CELLSIZE,mousepos[1]//CELLSIZE))
=======
            vie[mousepos[0]//CELLSIZE][mousepos[1]//CELLSIZE]=1 #pose une cellule
        if mousePressed2:
                vie[mousepos[0]//CELLSIZE][mousepos[1]//CELLSIZE]=0 #supprime une cellule
>>>>>>> 74773e15971563ae9225f20f689744483673ef24

    fenetre.fill((0,0,0))   #remplit la fenetre de noir
    remplirGrille(vie)      #affiche la grille
    pygame.display.update() #mets à  jour la fentre graphique
    
    if run and  time.monotonic() - timer > time_interval:   #vitesse du jeu
        timer = time.monotonic()                            #
        
        vie=prochaine_vie(vie)                              #calcule la prochaine generation


pygame.quit()

#endregion