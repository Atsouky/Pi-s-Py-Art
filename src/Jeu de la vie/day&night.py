#Projet : Pi's Py Art
#Auteurs : Damien Gazi

import pygame , time
from random import randint
#pourquoi que des comprhénsions? solution trouver par ia
#c'est plus rapide que des boucles for

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

def generationAleatoire(): # initialisation de la grille
    global vie    
    vie = { (x,y): 1 for x in range(info[0]//CELLSIZE) for y in range(info[1]//CELLSIZE) if randint(0, 1) == 0}

def remplirGrille(): # affiche la grille uniquement les cellule vivante et dans l'écran
    for (x, y) in vie:
        screen_x = (x * CELLSIZE) + offset_x
        screen_y = (y * CELLSIZE) + offset_y
        pygame.draw.rect(fenetre, cellcolor, (screen_x, screen_y, CELLSIZE, CELLSIZE))

def voisin(x, y): # calcule le nombre de voisin avec un compréhention
    return sum(vie.get((x+dx, y+dy), 0) for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)])

def prochaine_vie(): # calcule la prochaine étape 
    global vie
    new_vie = {}
    #toute les cellule autour des cellule vivante
    candidates = set(vie.keys()) | { (x+dx, y+dy) for x, y in vie for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]}
    
    #calcule la prochaine étape
    for cell in candidates:
        n = voisin(*cell)
        if n in [3, 6, 7, 8] or (cell in vie and n in [3, 4, 6, 7]):
            new_vie[cell] = 1
    vie = new_vie

#variable d'événement

mousePressed1 = False
mousePressed2 = False
middlePressed = False
last_mouse_pos = (0, 0)

timer = time.monotonic()
time_interval = 0.01
loop = True
run = True

generationAleatoire()

while loop:
    for event in pygame.event.get():  # les touche d'action
        if event.type == pygame.QUIT: 
            loop = False
        elif event.type == pygame.KEYDOWN: #quitter 
            if event.key == pygame.K_ESCAPE:
                loop = False
            elif event.key == pygame.K_SPACE: #pause
                run = not run
            elif event.key == pygame.K_v: #vider
                vie = {}
            elif event.key == pygame.K_r: #generation aléatoire
                generationAleatoire()
            elif event.key == pygame.K_a:
                last_mouse_pos = pygame.mouse.get_pos()
                middlePressed = not middlePressed
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
        vie[(grid_x, grid_y)] = 1 #placer une celule vivante
    if mousePressed2:
        vie.pop((grid_x, grid_y), None) # placer une celule mort
    
    fenetre.fill((0, 0, 0)) #remplir la fenetre de noir
    remplirGrille()         #remplir la grille
    pygame.display.update() #mise a jour
    
    if run and time.monotonic() - timer > time_interval: # boucle de la simulation
        timer = time.monotonic()
        prochaine_vie()

pygame.quit()