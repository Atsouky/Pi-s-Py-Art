# Jeu de la vie de Conway avec threading et Pygame sans NumPy

import pygame
import threading
import random

# Dimensions de la grille
WIDTH, HEIGHT = 1900, 1000
CELL_SIZE = 1
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

# Couleurs
ALIVE_COLOR = (255, 255, 255)
DEAD_COLOR = (0, 0, 0)

# Initialisation de Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu de la vie de Conway")

# Grille
grid = [[random.choice([0, 1]) for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

def draw_grid():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            color = ALIVE_COLOR if grid[y][x] == 1 else DEAD_COLOR
            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def update_grid():
    global grid
    new_grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            alive_neighbors = sum(grid[(y + dy) % GRID_HEIGHT][(x + dx) % GRID_WIDTH]
                                  for dx in [-1, 0, 1] for dy in [-1, 0, 1] if (dx != 0 or dy != 0))
            if grid[y][x] == 1 and alive_neighbors in [2, 3]:
                new_grid[y][x] = 1
            elif grid[y][x] == 0 and alive_neighbors == 3:
                new_grid[y][x] = 1
    grid = new_grid

def run_game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        update_grid()
        screen.fill(DEAD_COLOR)
        draw_grid()
        pygame.display.flip()
        pygame.time.delay(100)

if __name__ == "__main__":
    game_thread = threading.Thread(target=run_game)
    game_thread.start()
