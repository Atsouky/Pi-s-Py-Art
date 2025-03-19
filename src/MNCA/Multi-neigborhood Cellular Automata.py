#Projet : Pi's Py Art
#Auteurs : Damien Gazi

#Day & Night

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
    





import csv

def import_csv(filename):
    with open(filename, newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        return [[int(value) for value in row if value.strip()] for row in reader]

def dxl(ring1):
    dxlst = []
    r = len(ring1)//2
    for i in range(-r,r+1):
        dxlst.append(i)
    return dxlst, r


ring1 = import_csv("test.csv")
ring2 = import_csv("test1.csv")

dxlst, offset = dxl(ring1)


def ring(x, y, vie):
    nbvoisin1 = nbvoisin2 = avg1 = avg2 = 0
    for i, dx in enumerate(dxlst):
        for j, dy in enumerate(dxlst):
            if ring1[i][j]:
                nx, ny = (x + dx) % nbCellWidth, (y + dy) % nbCellHeight
                nbvoisin1 += vie[nx][ny]
                avg1 += 1
            elif ring2[i][j]:
                nx, ny = (x + dx) % nbCellWidth, (y + dy) % nbCellHeight
                nbvoisin2 += vie[nx][ny]
                avg2 += 1
    return (nbvoisin1 / avg1 if avg1 else 0), (nbvoisin2 / avg2 if avg2 else 0)


def prochaine_vie(vie):
    next_vie = [[0] * (nbCellHeight + 1) for _ in range(nbCellWidth + 1)]
    
    for x in range(nbCellWidth):
        for y in range(nbCellHeight):
            n1, n2 = ring(x, y, vie)
            if 0.185 <= n1 <= 0.200 or 0.445 <= n2 <= 0.680:
                next_vie[x][y] = 1.0
            elif 0.343 <= n1 <= 0.580 or 0.750 <= n1 <= 0.850 or 0.150 <= n2 <= 0.280 or 0.150 <= n1 <= 0.180:
                next_vie[x][y] = 0.0
            else:
                next_vie[x][y] = vie[x][y]
    return next_vie


cell_surface = pygame.Surface((CELLSIZE, CELLSIZE))
cell_surface.fill(cellcolor)

def remplirGrille(vie):
    for x in range(nbCellWidth):
        for y in range(nbCellHeight):
            if vie[x][y]:
                fenetre.blit(cell_surface, (x * CELLSIZE, y * CELLSIZE))



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
                cell_surface = pygame.Surface((CELLSIZE, CELLSIZE))
                cell_surface.fill(cellcolor)
                vie=initialiserCellules()
                vie=generationAleatoire()
            elif event.key ==pygame.K_PAGEDOWN:   #diminuer la taille de la grille
                if CELLSIZE>1:CELLSIZE-=1
                nbCellWidth = WINDOWWIDTH // CELLSIZE
                nbCellHeight = WINDOWHEIGHT // CELLSIZE
                cell_surface = pygame.Surface((CELLSIZE, CELLSIZE))
                cell_surface.fill(cellcolor)
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