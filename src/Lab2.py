import pygame
import random
import numpy as np

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 800
CELL_SIZE = 5
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

# Colors
BLACK = (0, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cellular Automaton Art")

# Initialize grid
grid = np.random.rand(GRID_HEIGHT, GRID_WIDTH)  # Random values between 0 and 1

# Function to update the grid based on rules
def update_grid(grid):
    new_grid = np.copy(grid)
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            # Get the neighbors' sum
            neighbors = (
                grid[(y - 1) % GRID_HEIGHT, (x - 1) % GRID_WIDTH]
                + grid[(y - 1) % GRID_HEIGHT, x]
                + grid[(y - 1) % GRID_HEIGHT, (x + 1) % GRID_WIDTH]
                + grid[y, (x - 1) % GRID_WIDTH]
                + grid[y, (x + 1) % GRID_WIDTH]
                + grid[(y + 1) % GRID_HEIGHT, (x - 1) % GRID_WIDTH]
                + grid[(y + 1) % GRID_HEIGHT, x]
                + grid[(y + 1) % GRID_HEIGHT, (x + 1) % GRID_WIDTH]
            )
            # Update rule: Combine current value and neighbor influence
            new_grid[y, x] = (grid[y, x] + neighbors / 8.0) / 2.0
            # Add some randomness for artistic effect
            new_grid[y, x] += random.uniform(-0.01, 0.01)
            # Clamp values to [0, 1]
            new_grid[y, x] = max(0, min(1, new_grid[y, x]))
    return new_grid

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update grid
    grid = update_grid(grid)

    # Draw grid
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            value = grid[y, x]
            color = (
                int(value * 255),
                int((1 - value) * 128),
                int(value * 128),
            )
            pygame.draw.rect(
                screen,
                color,
                (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE),
            )

    # Update display
    pygame.display.flip()
    clock.tick(30)  # 30 FPS

pygame.quit()
