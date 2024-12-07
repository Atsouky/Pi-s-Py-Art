import pygame
import math 
from random import randint


pygame.init()


WINDOWWIDTH = 1366
WINDOWHEIGHT = 700
WIDTH, HEIGHT = WINDOWWIDTH, WINDOWHEIGHT
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hexagon Grid")




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
    return [[randint(0,1) for i in range(cellHeight)] for j in range(cellWidth)]

def voisin(x : int, y : int, vie : list) -> int:
    #return sum(vie[x-1][y-1], vie[x][y-1], vie[x+1][y-1], vie[x-1][y], vie[x+1][y], vie[x-1][y+1], vie[x][y+1], vie[x+1][y+1])
    nbvoisin = 0    
    if x%2 == 1:    vs = [(0, 1), (-1, 0), (1, 0), (0, -1), (1, 1), (-1, 1)]
    else:           vs = [(0, 1), (-1, 0), (1, 0), (0, -1), (-1, -1), (1, -1)]
    
    for dx, dy in vs:
        nx, ny = (x + dx) % cellWidth, (y + dy) % cellHeight
        if vie[nx][ny] == 1: 
            nbvoisin += 1
    return nbvoisin
        



def draw_hexagon_grid(grid : list) -> None:
    for x in range(0, cellWidth):
        for y in range(0, cellHeight):
            dx = x * Cellsize * off
            dy = y * Cellsize * off
            if x % 2 == 1:
                dy += Cellsize
            if grid[x][y] == 1:
                draw_hexagon(screen, dx,dy, Cellsize,(0,255,0))
                


def nextvie(vie: list) -> list:
    newvie = [[0 for i in range(cellHeight)] for j in range(cellWidth)]
    for x in range(0, cellWidth):
        for y in range(0, cellHeight):
            a = voisin(x, y, vie)
            
            if a == 3:newvie[x][y] = 1
            elif a == 2: newvie[x][y] = vie[x][y]
            else:newvie[x][y] = 0
                
    return newvie





grid = rdgrid()
"""grid[1][1] = 0
grid[1][2] = 1 # (0, 1)
grid[0][1] = 1 # (-1, 0)
grid[2][1] = 1 # (1, 0)
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

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                running = False
                pygame.quit()
            elif event.key == pygame.K_r:
                grid = rdgrid()
            elif event.key == pygame.K_SPACE:
                run = not run
            elif event.key == pygame.K_v:
                for x in range(0, cellWidth):
                    for y in range(0, cellHeight):
                        grid[x][y] = 0
                
                
                
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
                
    
    
    clock.tick(30)
pygame.quit()
