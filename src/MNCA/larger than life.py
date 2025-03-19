#Projet : Pi's Py Art
#Auteurs : Damien Gazi

#Larger than life

import pygame , time
from random import uniform,randint
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

WINDOWWIDTH = info[0]
WINDOWHEIGHT = info[1]


#endregion



#Initialiste tout les cellule a 0 en faisant des listes de listes: return liste[x][y]
def initialiserCellules() -> list:
    return [[0 for i in range(nbCellHeight+1)] for j in range(nbCellWidth+1)]


#Initialiste tout les cellule a 0 ou 1 aleatoirement en faisant des listes de listes:  return liste[x][y]
def generationAleatoire() -> list:
    return [[randint(0,1) for i in range(nbCellHeight+1)] for j in range(nbCellWidth+1)]
    


#remplir la fenetre avec un rectangle vert si la cellule est vivante, sinon noir
def remplirGrille(vie):
    for x in range(nbCellWidth):
        for y in range(nbCellHeight):
            if vie[x][y]:
                pygame.draw.rect(fenetre, cellcolor, (x*CELLSIZE, y*CELLSIZE, CELLSIZE, CELLSIZE))
    



ring1 =[
     0,0,0,0,0,0,0,0,0,
     0,0,0,0,0,0,0,0,0,
     0,0,0,0,0,0,0,0,0,
     0,0,0,0,0,0,0,0,0,
     0,0,0,0,'',0,0,0,0,
     0,0,0,0,0,0,0,0,0,
     0,0,0,0,0,0,0,0,0,
     0,0,0,0,0,0,0,0,0,
     0,0,0,0,0,0,0,0,0,
     
 ]

ring2 =[
     0,0,0,0,0,0,0,0,0,
     0,0,0,0,0,0,0,0,0,
     0,0,0,0,0,0,0,0,0,
     0,0,0,0,0,0,0,0,0,
     0,0,0,0,'',0,0,0,0,
     0,0,0,0,0,0,0,0,0,
     0,0,0,0,0,0,0,0,0,
     0,0,0,0,0,0,0,0,0,
     0,0,0,0,0,0,0,0,0,
     
 ]

ring3 =[
     0,0,0,0,0,0,0,0,0,
     0,0,0,0,0,0,0,0,0,
     0,0,0,0,0,0,0,0,0,
     0,0,0,0,0,0,0,0,0,
     0,0,0,0,'',0,0,0,0,
     0,0,0,0,0,0,0,0,0,
     0,0,0,0,0,0,0,0,0,
     0,0,0,0,0,0,0,0,0,
     0,0,0,0,0,0,0,0,0,
     
 ]










#Compte le nombre de voisins vivant autoure d'une cellule --> ici 8 voisins
#Bordure type portail
def r5x5(x, y, vie):
    nbvoisin = 0
    for dx in [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]:
        for dy in [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = (x + dx) % nbCellWidth, (y + dy) % nbCellHeight
            nbvoisin += vie[nx][ny]
    return nbvoisin

def r3x3(x, y, vie):
    nbvoisin = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = (x + dx) % nbCellWidth, (y + dy) % nbCellHeight
            nbvoisin += vie[nx][ny]
    return nbvoisin


#Calacul de la prochaine generation en fonction du nombre de voisins
def prochaine_vie(vie):
    next_vie = [[0] * (nbCellHeight+1) for i in range(nbCellWidth+1)]
    
    for x in range(nbCellWidth):
        for y in range(nbCellHeight):
            
            nbvoisin = r5x5(x, y, vie)
            
            next_vie[x][y] = vie[x][y]
                
            
                
            if 0 <= nbvoisin <= 33:
                next_vie[x][y] = 0
            
            elif 34 <= nbvoisin <= 45:
                next_vie[x][y] = 1
            
            elif 58 <=nbvoisin <= 121 :
                next_vie[x][y] = 0
                
                    
            
            
            

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
            vie[mousepos[0]//CELLSIZE][mousepos[1]//CELLSIZE]=1 #pose une cellule
        if mousePressed2:
                vie[mousepos[0]//CELLSIZE][mousepos[1]//CELLSIZE]=0 #supprime une cellule

    fenetre.fill((0,0,0))   #remplit la fenetre de noir
    remplirGrille(vie)      #affiche la grille
    pygame.display.update() #mets à  jour la fentre graphique
    
    if run and  time.monotonic() - timer > time_interval:   #vitesse du jeu
        timer = time.monotonic()                            #
        
        vie=prochaine_vie(vie)                              #calcule la prochaine generation


pygame.quit()

#endregion