import pygame
import math 
from random import  uniform


pygame.init()


WINDOWWIDTH = 1366
WINDOWHEIGHT = 700
WIDTH, HEIGHT = WINDOWWIDTH, WINDOWHEIGHT
clock = pygame.time.Clock()
screen = pygame.display.set_mode((0, 0), pygame.NOFRAME)
pygame.display.set_caption("Hexagon Grid")
info = pygame.display.get_surface().get_size()



Cellsize = 5
cellWidth = WIDTH // Cellsize
cellHeight = HEIGHT // Cellsize

off = 2.1


hex_cache = {}


def draw_hexagon(surface : pygame.surface, x: int, y: int, size: int,color: tuple) -> None:
    if (size, color) not in hex_cache:
        points = []
        for i in range(6):
            angle = math.pi / 3 * i
            x_offset = size * math.cos(angle)
            y_offset = size * math.sin(angle)
            points.append((x_offset, y_offset))
        hex_cache[(size, color)] = points
    points = hex_cache[(size, color)]
    pygame.draw.polygon(surface, color, [(x + p[0], y + p[1]) for p in points])


def rdgrid() -> list:
    return [[uniform(-1.0,1.0) for i in range(cellHeight)] for j in range(cellWidth)]

voisins_fliter_pair = [    #[(0, 1), (-1, 0), (1, 0), (0, -1), (-1, -1), (1, -1)]
    [-1, -1, 0.0],[0, -1, -0.1],[1, -1 , -0.3],
                  [0, 0 , 1.0 ],
    [-1, 0, -0.5],[0, 1, 0.2],  [1, 0, 0.5]
]

voisins_fliter_impair = [   #[(0, 1), (-1, 0), (1, 0), (0, -1), (1, 1), (-1, 1)]
    [-1, 0, 0.0],[0, -1, -0.1],[1, 0 , -0.3],
                  [0, 0 , 1.0 ],
    [-1, 1, -0.5],[0, 1, 0.2],  [1, 1, 0.5]
]

def voisin(x : int, y : int, vie : list) -> int:
    #return sum(vie[x-1][y-1], vie[x][y-1], vie[x+1][y-1], vie[x-1][y], vie[x+1][y], vie[x-1][y+1], vie[x][y+1], vie[x+1][y+1])
    nbvoisin = 0    
    if x%2 == 1:    vs = voisins_fliter_impair
    else:           vs = voisins_fliter_pair
    
    for dx, dy , weight in vs:
        nx, ny = (x + dx) % cellWidth, (y + dy) % cellHeight
        nbvoisin += vie[nx][ny] * weight
    return nbvoisin
        
from math import *
def f(x: float) -> float:
    return x * 1/2

def draw_hexagon_grid(grid : list) -> None:
    for x in range(0, cellWidth):
        for y in range(0, cellHeight):
            dx = x * Cellsize * off
            dy = y * Cellsize * off
            if x % 2 == 1:
                dy += Cellsize
            value = max(0.0, min(1.0, grid[x][y]))
            intensity = int(value * 255)   
            color = (max(0,intensity-100), 0, max(0,intensity-50))
            if grid[x][y] != 0:
                draw_hexagon(screen, dx,dy, Cellsize,color)
                


def nextvie(vie: list) -> list:
    newvie = [[0 for i in range(cellHeight)] for j in range(cellWidth)]
    for x in range(0, cellWidth):
        for y in range(0, cellHeight):
            a = voisin(x, y, vie)
            
            newvie[x][y] = f(voisin(x, y, vie))
                
    return newvie





grid = rdgrid()
"""grid[1][1] = 0
grid[1][2] = 1 # (0, 1)
grid[0][1] = 1 # (-1, 0)
grid[2][1] = 1 # (1, 0)s
grid[1][0] = 1 # (0, -1)
grid[2][2] = 1 # (1, 1)
grid[0][2] = 1 # (-1, 1)"""

"""grid[10][10] = 1
grid[10][11] = 1
grid[10][12] = 1"""


running = True
run= True
while running:
    screen.fill((0,0,0))
    
    draw_hexagon_grid(grid)
    if run : grid=nextvie(grid)
    
    pygame.display.flip()   
                
                
    pos = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        for x in range(0, cellWidth):
            for y in range(0, cellHeight):
                dx = x * Cellsize * off
                dy = y * Cellsize * off
                
                if (pos[0] > dx) and (pos[0] < dx + Cellsize * off) and (pos[1] > dy) and (pos[1] < dy + Cellsize * off):
                    grid[x][y] = 1
    elif pygame.mouse.get_pressed()[2]:
        for x in range(0, cellWidth):
            for y in range(0, cellHeight):
                dx = x * Cellsize * off
                dy = y * Cellsize * off
               
                if (pos[0] > dx) and (pos[0] < dx + Cellsize * off) and (pos[1] > dy) and (pos[1] < dy + Cellsize * off):
                    grid[x][y] = 0
                
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
            elif event.key == pygame.K_r:
                grid = rdgrid()
            elif event.key == pygame.K_SPACE:
                run = not run
            
            elif event.key == pygame.K_v:
                for i in range(0, cellWidth):
                    for j in range(0, cellHeight):
                        grid[i][j] = 0
                
            elif event.key == pygame.K_t:
                temp=[]
                for i in range(7):
                    temp.append(uniform(-1.0,1.0))
                for i,j in enumerate(voisins_fliter_pair):
                    j[2] = temp[i]
                for i,j in enumerate(voisins_fliter_impair):
                    j[2] = temp[i]
    
    #clock.tick(30)
pygame.quit()
