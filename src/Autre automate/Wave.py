#Projet : Pi's Py Art
#Auteurs : Damien Gazi

#Wave v0.1

import pygame , time
from random import uniform
#region------------------------------------------------------------__Init__-----------------------------------------------------------------------------------------


cellcolor = (0,255,0)

clock = pygame.time.Clock()
pygame.init()



fenetre = pygame.display.set_mode((0,0), pygame.NOFRAME)

pygame.display.set_caption("Wave")
font = pygame.font.Font('freesansbold.ttf', 20)

#variables de l'écran
info = pygame.display.get_surface().get_size()
WINDOWWIDTH = info[0]
WINDOWHEIGHT = info[1]
CELLSIZE = 7
CELLWIDTH = WINDOWWIDTH // CELLSIZE
CELLHEIGHT = WINDOWHEIGHT // CELLSIZE

global nbCellHeight, nbCellWidth
nbCellWidth=WINDOWWIDTH//CELLSIZE
nbCellHeight=WINDOWHEIGHT//CELLSIZE


#endregion



#Initialiste tout les cellule a 0 en faisant des listes de listes: return liste[x][y]
def initialiserCellules() -> list:
    return [[0 for i in range(nbCellHeight+1)] for j in range(nbCellWidth+1)]


#Initialiste tout les cellule a 0 ou 1 aleatoirement en faisant des listes de listes:  return liste[x][y]
def generationAleatoire() -> list:
    return [[round(uniform(-0.5,0.5),2) for i in range(nbCellHeight+1)] for j in range(nbCellWidth+1)]
    


#remplir la fenetre avec un rectangle vert si la cellule est vivante, sinon noir
def remplirGrille(vie):
    for x in range(nbCellWidth):
        for y in range(nbCellHeight): 
            value = vie[x][y] * 10
            if value > 0:
                green = min(255, int(value * 255))  
                color = (0, green, 0)
            elif value < 0:
                red = min(255, int(abs(value) * 255))  
                color = (red, 0, 0)
            else:
                color = (0, 0, 0)  
            pygame.draw.rect(fenetre, color, (x * CELLSIZE, y * CELLSIZE, CELLSIZE, CELLSIZE))
    

#Compte le nombre de voisins vivant autoure d'une cellule --> ici 8 voisins
#Bordure type portail
#Renvoie la moyenne de voisins
def voisin(x, y, vie):
    nbvoisin = 0
    for dx,dy in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
        nx, ny = (x + dx) % nbCellWidth, (y + dy) % nbCellHeight
        nbvoisin += vie[nx][ny]
    nbvoisin /= 8
    return nbvoisin
import math
#Calacul de la prochaine generation en fonction du nombre de voisins
def prochaine_vie(vie):
    next_vie = [[0] * (nbCellHeight+1) for i in range(nbCellWidth+1)]
    
    for x in range(nbCellWidth):
        for y in range(nbCellHeight):
            a = voisin(x, y, vie)

            vienew = vie[x][y] + alpha * (a - vie[x][y]) # - beta * vie[x][y]

            if vienew>0.8: next_vie[x][y] = 1
            elif vienew<-0.8: next_vie[x][y] = -1
            else:next_vie[x][y] = max(-1.0, min(1.0, vienew))

    return next_vie



#region------------------------------------------------------------__Loop__-----------------------------------------------------------------------------------------


vie=initialiserCellules()
vie=generationAleatoire()
mousePressed1=False
mousePressed2=False
timer = time.monotonic()
time_interval = 0.01
loop=True
run=True

#special variables
alpha = 0.5 #propagation
beta = 0.05 #damping 


while loop==True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:           #fermeture du jeu
            loop = False            
        
        elif event.type == pygame.KEYDOWN:      # Vérifie les touches appuyées
            
            if event.key ==pygame.K_ESCAPE:          #fermeture du jeu
                loop=False
            
            elif event.key ==pygame.K_SPACE:    #activer/desactiver pause
                run=not run
            
            elif event.key ==pygame.K_v:        #vider la grille
                vie=initialiserCellules()
            elif event.key ==pygame.K_r:        #remplir la grille aléatoirement
                vie=generationAleatoire()
                
            elif event.key ==pygame.K_RIGHT:    #augmenter la vitesse
                if time_interval > 0.01: time_interval -= 0.1
            elif event.key ==pygame.K_LEFT:     #diminuer la vitesse
                time_interval += 0.1
            
                
                
            elif event.key ==pygame.K_PAGEUP:   #augmenter la taille de la grille
                CELLSIZE+=1
                CELLWIDTH = WINDOWWIDTH // CELLSIZE
                CELLHEIGHT = WINDOWHEIGHT // CELLSIZE
                vie=initialiserCellules()
                vie=generationAleatoire()
            elif event.key ==pygame.K_PAGEDOWN:   #diminuer la taille de la grille
                if CELLSIZE>1:CELLSIZE-=1
                nbCellWidth = WINDOWWIDTH // CELLSIZE
                nbCellHeight = WINDOWHEIGHT // CELLSIZE
                vie=initialiserCellules()
                vie=generationAleatoire()
                            
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
            vie[mousepos[0]//CELLSIZE][mousepos[1]//CELLSIZE]=0.5 #poser une cellule verte
        if mousePressed2:
                vie[mousepos[0]//CELLSIZE][mousepos[1]//CELLSIZE]=-0.5 #poser une cellule rouge

    fenetre.fill((0,0,0))   #remplit la fenetre de noir
    remplirGrille(vie)      #affiche la grille
    pygame.display.update() #mets à  jour la fentre graphique
    
    if run and  time.monotonic() - timer > time_interval:   #vitesse du jeu
        timer = time.monotonic()                            #
        
        vie=prochaine_vie(vie)                              #calcule la prochaine generation


pygame.quit()

#endregion