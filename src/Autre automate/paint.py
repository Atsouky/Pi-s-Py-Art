"""
Programme jeu de la vie rÃ©alisÃ© par Gazi Damien Tg3
"""

#Paint

import pygame , time
from random import randint
#region------------------------------------------------------------__Init__-----------------------------------------------------------------------------------------



cellcolor = (0,255,0)

clock = pygame.time.Clock()
pygame.init()

display_info = pygame.display.Info()
l = display_info.current_w
h = display_info.current_h - 50 #pour la barre de menu windows

fenetre = pygame.display.set_mode((l,h), pygame.RESIZABLE)

pygame.display.set_caption("Paint")
font = pygame.font.Font('freesansbold.ttf', 20)

#variables de l'écran
WINDOWWIDTH = l
WINDOWHEIGHT = h
CELLSIZE = 3
CELLWIDTH = WINDOWWIDTH // CELLSIZE
CELLHEIGHT = WINDOWHEIGHT // CELLSIZE

global nbCellHeight, nbCellWidth
nbCellWidth=WINDOWWIDTH//CELLSIZE
nbCellHeight=WINDOWHEIGHT//CELLSIZE


#endregion



#Initialiste tout les cellule a 0 en faisant des listes de listes: return liste[x][y]
def initialiserCellules() -> list:
    return [[(0,0,0) for i in range(nbCellHeight+1)] for j in range(nbCellWidth+1)]



    


#remplir la fenetre avec un rectangle vert si la cellule est vivante, sinon noir
def remplirGrille(vie):
    for x in range(nbCellWidth):
        for y in range(nbCellHeight):
            if vie[x][y]!=(0,0,0):
                pygame.draw.rect(fenetre, vie[x][y], (x*CELLSIZE, y*CELLSIZE, CELLSIZE, CELLSIZE))
    

#Compte le nombre de voisins vivant autoure d'une cellule --> ici 8 voisins
#Bordure type portail
def voisin(x, y, vie):
    nbvoisin = 0
    for dx ,dy in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
        nx, ny = (x + dx) % nbCellWidth, (y + dy) % nbCellHeight
        nbvoisin += vie[nx][ny]
    return nbvoisin

#Calacul de la prochaine generation en fonction du nombre de voisins



#region------------------------------------------------------------__Loop__-----------------------------------------------------------------------------------------


vie=initialiserCellules()
selected = (255,0,0)
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

            elif event.key ==pygame.K_1:
                selected = (255,0,0)
            elif event.key ==pygame.K_2:
                selected = (0,255,0)
            elif event.key ==pygame.K_3:
                selected = (0,0,255)

                
            elif event.key ==pygame.K_RIGHT:    #augmenter la vitesse
                if time_interval > 0.01: time_interval -= 0.1
            elif event.key ==pygame.K_LEFT:     #diminuer la vitesse
                time_interval += 0.1
            
                
                
            elif event.key ==pygame.K_PAGEUP:   #augmenter la taille de la grille
                CELLSIZE+=1
                CELLWIDTH = WINDOWWIDTH // CELLSIZE
                CELLHEIGHT = WINDOWHEIGHT // CELLSIZE
                vie=initialiserCellules()

            elif event.key ==pygame.K_PAGEDOWN:   #diminuer la taille de la grille
                if CELLSIZE>1:CELLSIZE-=1
                nbCellWidth = WINDOWWIDTH // CELLSIZE
                nbCellHeight = WINDOWHEIGHT // CELLSIZE
                vie=initialiserCellules()

                            
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
            vie[mousepos[0]//CELLSIZE][mousepos[1]//CELLSIZE]=selected #pose une cellule
        if mousePressed2:
                vie[mousepos[0]//CELLSIZE][mousepos[1]//CELLSIZE]=(0,0,0) #supprime une cellule

    fenetre.fill((0,0,0))   #remplit la fenetre de noir
    remplirGrille(vie)      #affiche la grille
    pygame.display.update() #mets à  jour la fentre graphique
    
    if run and  time.monotonic() - timer > time_interval:   #vitesse du jeu
        timer = time.monotonic()                            #
        
                                     #calcule la prochaine generation


pygame.quit()

#endregion