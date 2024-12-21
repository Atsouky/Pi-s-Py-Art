"""
Programme jeu de la vie rÃ©alisÃ© par Gazi Damien Tg3
"""

# Day & Night with Color Field Automaton

import pygame, time
from random import uniform
#region------------------------------------------------------------__Init__-----------------------------------------------------------------------------------------

clock = pygame.time.Clock()
pygame.init()

display_info = pygame.display.Info()
l = display_info.current_w
h = display_info.current_h - 50  # pour la barre de menu windows

fenetre = pygame.display.set_mode((l, h), pygame.RESIZABLE)
pygame.display.set_caption("Day & Night: Color Field Automaton")
font = pygame.font.Font('freesansbold.ttf', 20)

# Variables de l'écran
WINDOWWIDTH = l
WINDOWHEIGHT = h
CELLSIZE = 5
CELLWIDTH = WINDOWWIDTH // CELLSIZE
CELLHEIGHT = WINDOWHEIGHT // CELLSIZE

global nbCellHeight, nbCellWidth
nbCellWidth = WINDOWWIDTH // CELLSIZE
nbCellHeight = WINDOWHEIGHT // CELLSIZE

#endregion

# Initialize all cells with random floating-point RGB values
def initialiserCellules() -> list:
    return [[[uniform(0, 1) for _ in range(3)] for _ in range(nbCellHeight + 1)] for _ in range(nbCellWidth + 1)]

# Fill the window with rectangles colored according to each cell's RGB value
def remplirGrille(vie):
    for x in range(nbCellWidth):
        for y in range(nbCellHeight):
            color = tuple(int(c * 255) for c in vie[x][y])  # Convert RGB from [0,1] to [0,255]
            pygame.draw.rect(fenetre, color, (x * CELLSIZE, y * CELLSIZE, CELLSIZE, CELLSIZE))

# Calculate the weighted average RGB of neighbors
def moyenne_voisins(x, y, vie):
    sum_r, sum_g, sum_b = 0, 0, 0
    for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        nx, ny = (x + dx) % nbCellWidth, (y + dy) % nbCellHeight
        r, g, b = vie[nx][ny]
        sum_r += r
        sum_g += g
        sum_b += b
    n = 8  # 8 neighbors
    return sum_r / n, sum_g / n, sum_b / n

# Calculate the next generation based on neighbor influence and random noise
def prochaine_vie(vie):
    next_vie = [[[0, 0, 0] for _ in range(nbCellHeight + 1)] for _ in range(nbCellWidth + 1)]
    for x in range(nbCellWidth):
        for y in range(nbCellHeight):
            r, g, b = vie[x][y]
            avg_r, avg_g, avg_b = moyenne_voisins(x, y, vie)

            # Blend current color with the average neighbor color and add slight noise
            next_vie[x][y][0] = max(0, min(1, 0.5 * r + 0.5 * avg_r + uniform(-0.01, 0.01)))
            next_vie[x][y][1] = max(0, min(1, 0.5 * g + 0.5 * avg_g + uniform(-0.01, 0.01)))
            next_vie[x][y][2] = max(0, min(1, 0.5 * b + 0.5 * avg_b + uniform(-0.01, 0.01)))
    return next_vie

#region------------------------------------------------------------__Loop__-----------------------------------------------------------------------------------------

vie = initialiserCellules()
mousePressed1 = False
mousePressed2 = False
timer = time.monotonic()
time_interval = 0.01
loop = True
run = True

while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # fermeture du jeu
            loop = False

        elif event.type == pygame.KEYDOWN:  # Vérifie les touches appuyées
            if event.key == pygame.K_w:  # fermeture du jeu
                loop = False

            elif event.key == pygame.K_SPACE:  # activer/desactiver pause
                run = not run

            elif event.key == pygame.K_r:  # Réinitialiser avec une nouvelle grille aléatoire
                vie = initialiserCellules()

            elif event.key == pygame.K_RIGHT:  # augmenter la vitesse
                if time_interval > 0.01:
                    time_interval -= 0.01
            elif event.key == pygame.K_LEFT:  # diminuer la vitesse
                time_interval += 0.01

            elif event.key == pygame.K_PAGEUP:  # augmenter la taille de la grille
                CELLSIZE += 1
                CELLWIDTH = WINDOWWIDTH // CELLSIZE
                CELLHEIGHT = WINDOWHEIGHT // CELLSIZE
                vie = initialiserCellules()
            elif event.key == pygame.K_PAGEDOWN:  # diminuer la taille de la grille
                if CELLSIZE > 1:
                    CELLSIZE -= 1
                CELLWIDTH = WINDOWWIDTH // CELLSIZE
                CELLHEIGHT = WINDOWHEIGHT // CELLSIZE
                vie = initialiserCellules()

    fenetre.fill((0, 0, 0))  # Remplit la fenêtre de noir
    remplirGrille(vie)  # Affiche la grille
    pygame.display.update()  # Met à jour la fenêtre graphique

    if run and time.monotonic() - timer > time_interval:  # vitesse du jeu
        timer = time.monotonic()
        vie = prochaine_vie(vie)  # calcule la prochaine génération

pygame.quit()

#endregion
