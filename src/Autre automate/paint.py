#Projet : Pi's Py Art
#Auteurs : Damien Gazi

#Paint

import pygame , time
from random import randint
from vcolorpicker import getColor
from vcolorpicker import useLightTheme
from vcolorpicker import useAlpha

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


#endregion



#Initialiste tout les cellule a 0 en faisant des listes de listes: return liste[x][y]
def generationAleatoire(): # initialisation de la grille
    global vie    
    vie = { (x,y): (0,0,0) for x in range(info[0]//CELLSIZE) for y in range(info[1]//CELLSIZE)}


    


#remplir la fenetre avec un rectangle vert si la cellule est vivante, sinon noir
def remplirGrille(): 
    for (x, y) in vie:
        screen_x = (x * CELLSIZE) + offset_x
        screen_y = (y * CELLSIZE) + offset_y
        pygame.draw.rect(fenetre, vie[(x,y)], (screen_x, screen_y, CELLSIZE, CELLSIZE))
    







#region------------------------------------------------------------__Loop__-----------------------------------------------------------------------------------------
#color = getColor()   #Choix de la couleur

old_color = (255,255,255)
picked_color = getColor(old_color)
vie={}
generationAleatoire()
selected = picked_color
mousePressed1=False
mousePressed2=False
middlePressed=False
last_mouse_pos = (0, 0)
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
                vie=generationAleatoire()

            elif event.key == pygame.K_e: offset_x,offset_y = 0,0
            
            elif event.key ==pygame.K_c:   #si echap appuyée retour au choix de la couleur
                #color = getColor()

                old_color = (255,255,255)
                picked_color = getColor(old_color)
                selected = picked_color
                
            elif event.key == pygame.K_a:
                last_mouse_pos = pygame.mouse.get_pos()
                middlePressed = True
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                middlePressed = False
                
        elif event.type == pygame.MOUSEBUTTONDOWN: #les click de la souris
            if event.button == 1:
                mousePressed1 = True
            elif event.button == 3:
                mousePressed2 = True
            elif event.button == 2:
                middlePressed = True
                last_mouse_pos = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                mousePressed1 = False
            elif event.button == 3:
                mousePressed2 = False
            elif event.button == 2:
                middlePressed = False
        elif event.type == pygame.MOUSEMOTION and middlePressed: #le mouvelement de la souris avec le click mollette pour déplace l'offset
            new_mouse_pos = pygame.mouse.get_pos()
            dx = new_mouse_pos[0] - last_mouse_pos[0]
            dy = new_mouse_pos[1] - last_mouse_pos[1]
            offset_x += dx
            offset_y += dy
            last_mouse_pos = new_mouse_pos
        elif event.type == pygame.MOUSEWHEEL:     # le zoom avec la mollette de la souris
            mouse_x, mouse_y = pygame.mouse.get_pos() 
            old_cellsize = CELLSIZE
            CELLSIZE = max(2, min(50, CELLSIZE + event.y))  
            scale_factor = CELLSIZE / old_cellsize
            offset_x = int(mouse_x - (mouse_x - offset_x) * scale_factor)
            offset_y = int(mouse_y - (mouse_y - offset_y) * scale_factor)
    
    mousepos = pygame.mouse.get_pos()
    grid_x = (mousepos[0] - offset_x) // CELLSIZE
    grid_y = (mousepos[1] - offset_y) // CELLSIZE
    if mousePressed1:
        vie[(grid_x, grid_y)] = (selected) #placer une celule vivante
    if mousePressed2:
        vie.pop((grid_x, grid_y), None) # placer une celule mort
    
    fenetre.fill((0, 0, 0)) #remplir la fenetre de noir
    remplirGrille()         #remplir la grille
    pygame.display.update() #mise a jour
    
    if run and time.monotonic() - timer > time_interval: # boucle de la simulation
        timer = time.monotonic()
        

pygame.quit()