#Projet : Pi's Py Art
#Auteurs : Damien Gazi



import pygame , time
from random import uniform
#region------------------------------------------------------------__Init__-----------------------------------------------------------------------------------------


voisins =[(-1,0),(1,0),(0,1),(0,-1),(-1,0),(1,0),(0,1),(0,-1),(-1,0),(1,0),(0,1),(0,-1),(-1,0),(1,0),(0,1),(0,-1),(-1,1),(1,-1),(1,1),(-1,-1)]
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


#endregion



#Initialiste tout les cellule a 0 en faisant des listes de listes: return liste[x][y]
def initialiserCellules() -> list:
    return [[0.01 for i in range(nbCellHeight+1)] for j in range(nbCellWidth+1)]


#Initialiste tout les cellule a 0 ou 1 aleatoirement en faisant des listes de listes:  return liste[x][y]
def generationAleatoire() -> list:
    return [[round(uniform(-30,30),2) for i in range(nbCellHeight+1)] for j in range(nbCellWidth+1)]
    


#remplir la fenetre avec un rectangle vert si la cellule est vivante, sinon noir
def remplirGrille(vie):
    for x in range(nbCellWidth):
        for y in range(nbCellHeight):
            if vie[x][y] > 0:    
                cellcolor = (min(vie[x][y]*100,255),0,0)
            elif vie[x][y] < 0:    
                cellcolor = (0,0,min(abs(vie[x][y])*100,255))
            else:
                cellcolor = (255,255,255)
            pygame.draw.rect(fenetre, cellcolor, (x*CELLSIZE, y*CELLSIZE, CELLSIZE, CELLSIZE))
    

#Compte le nombre de voisins vivant autoure d'une cellule --> ici 8 voisins
#Bordure type portail
def voisin(x, y, vie):
    nbvoisin = 0
    for dx ,dy in voisins:
        nx, ny = (x + dx) % nbCellWidth, (y + dy) % nbCellHeight
        nbvoisin += vie[nx][ny]
    nbvoisin/=20
    return nbvoisin

#Calacul de la prochaine generation en fonction du nombre de voisins
def prochaine_vie(vie):
    next_vie = [[0] * (nbCellHeight+1) for i in range(nbCellWidth+1)]
    
    for x in range(nbCellWidth):
        for y in range(nbCellHeight):
            a = voisin(x, y, vie)
            
            next_vie[x][y] = a

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
            vie[mousepos[0]//CELLSIZE][mousepos[1]//CELLSIZE]=25 #pose une cellule
        if mousePressed2:
                vie[mousepos[0]//CELLSIZE][mousepos[1]//CELLSIZE]=-25 #supprime une cellule

    fenetre.fill((0,0,0))   #remplit la fenetre de noir
    remplirGrille(vie)      #affiche la grille
    pygame.display.update() #mets à  jour la fentre graphique
    
    if run and  time.monotonic() - timer > time_interval:   #vitesse du jeu
        timer = time.monotonic()                            #
        
        vie=prochaine_vie(vie)                              #calcule la prochaine generation


pygame.quit()

#endregion