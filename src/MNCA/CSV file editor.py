#Projet : Pi's Py Art
#Auteurs : Damien Gazi et Aide d'une intelligence artificielle

import pygame
import csv
import os

# Constants
CELL_SIZE = 20
GRID_COLOR = (100, 100, 100)
CELL_COLOR = (200, 200, 200)
LIVE_CELL_COLOR = (0, 255, 0)
WINDOW_PADDING = 50
FONT_SIZE = 24

# Load CSV file
def load_csv(filename):
    with open(filename, newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        return [[int(value) for value in row if value.strip()] for row in reader]

# Save CSV file
def save_csv(filename, grid):
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(grid)

# Initialize Pygame
pygame.init()

# Create window
screen = pygame.display.set_mode((500, 200))
pygame.display.set_caption("File Menu")

# Load font
font = pygame.font.Font(None, FONT_SIZE)

# Create an input box for the filename
input_box = pygame.Rect(50, 50, 400, 32)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
text = ''
clock = pygame.time.Clock()

def draw_text(text, font, color, surface, rect):
    if text:
        label = font.render(text, True, color)
        surface.blit(label, (rect.x + 5, rect.y + 5))

def draw_input_box(text, rect, color):
    pygame.draw.rect(screen, color, rect, 2)
    draw_text(text, font, color, screen, rect)

# Main menu loop
running = True
while running:
    screen.fill((255, 255, 255))
    
    # Draw input box
    draw_input_box(text, input_box, color)

    # Draw labels
    draw_text("Enter the filename:", font, (0, 0, 0), screen, pygame.Rect(50, 20, 400, FONT_SIZE))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                active = True
                color = color_active
            else:
                active = False
                color = color_inactive
        elif event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    if text: # If there's a filename entered
                        text = text + ".csv"
                        if os.path.exists(text):  # Check if the file exists
                            grid = load_csv(text)
                            print(f"File '{text}' loaded successfully.")
                            running = False  # Exit the menu to continue the program
                        else:
                            print(f"File '{text}' does not exist. Creating new file.")
                            grid = [[0]*5 for _ in range(5)]  # Default grid size if file does not exist
                            running = False
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

    clock.tick(30)

# Now proceed with the original grid editor
pygame.quit()

# Constants for grid editor
CELL_SIZE = 20
GRID_COLOR = (100, 100, 100)
CELL_COLOR = (200, 200, 200)
LIVE_CELL_COLOR = (0, 255, 0)
WINDOW_PADDING = 50

# Initialize Pygame again for the editor
pygame.init()

# Grid dimensions based on the loaded grid
rows, cols = len(grid), len(grid[0])
win_width = cols * CELL_SIZE + WINDOW_PADDING
win_height = rows * CELL_SIZE + WINDOW_PADDING

# Create window for the grid editor
screen = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("CSV Grid Editor")

running = True
mouse_held = False  # Track whether the mouse is being held down

def render_text(text, x, y, color=(255, 255, 255)):
    # Render the text into a surface
    rendered_text = font.render(text, True, color)
    # Blit the text onto the screen at (x, y)
    screen.blit(rendered_text, (x, y))
font = pygame.font.Font(None, 36)
while running:
    screen.fill(CELL_COLOR)

    # Draw labels
    
    
    # Draw grid
    for y in range(rows):
        for x in range(cols):
            color = LIVE_CELL_COLOR if grid[y][x] == 1 else CELL_COLOR
            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, GRID_COLOR, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

    xlabel = "x "+str(rows)+" y "+str(cols)
    
    
    
    render_text(xlabel, 10, win_height - 30)
    
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            grid_x, grid_y = mouse_x // CELL_SIZE, mouse_y // CELL_SIZE

            if event.button == 1:  # Left mouse button (add live cell)
                if 0 <= grid_x < cols and 0 <= grid_y < rows:
                    grid[grid_y][grid_x] = 1  # Add live cell
                    mouse_held = True

            elif event.button == 3:  # Right mouse button (remove live cell)
                if 0 <= grid_x < cols and 0 <= grid_y < rows:
                    grid[grid_y][grid_x] = 0  # Remove live cell
                    mouse_held = True

        elif event.type == pygame.MOUSEMOTION:
            if mouse_held:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                grid_x, grid_y = mouse_x // CELL_SIZE, mouse_y // CELL_SIZE

                if 0 <= grid_x < cols and 0 <= grid_y < rows:
                    if pygame.mouse.get_pressed()[0]:  # Left click (add)
                        grid[grid_y][grid_x] = 1
                    elif pygame.mouse.get_pressed()[2]:  # Right click (remove)
                        grid[grid_y][grid_x] = 0

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 or event.button == 3:  # Left or right mouse button
                mouse_held = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:  # Press 'S' to save changes
                save_csv(text, grid)  # Save the grid to the file name entered
                print("Grid saved to", text)

            elif event.key == pygame.K_r:  # Reset all cells to 0
                for i in range(rows):
                    for j in range(cols):
                        grid[i][j] = 0

            elif event.key == pygame.K_DOWN:  # Add a row at the bottom
                grid.append([0] * cols)
                rows += 1
                win_height = rows * CELL_SIZE + WINDOW_PADDING
                screen = pygame.display.set_mode((win_width, win_height))

            elif event.key == pygame.K_UP and rows > 1:  # Remove last row
                grid.pop()
                rows -= 1
                win_height = rows * CELL_SIZE + WINDOW_PADDING
                screen = pygame.display.set_mode((win_width, win_height))

            elif event.key == pygame.K_RIGHT:  # Add a column on the right
                for row in grid:
                    row.append(0)
                cols += 1
                win_width = cols * CELL_SIZE + WINDOW_PADDING
                screen = pygame.display.set_mode((win_width, win_height))

            elif event.key == pygame.K_LEFT and cols > 1:  # Remove last column
                for row in grid:
                    row.pop()
                cols -= 1
                win_width = cols * CELL_SIZE + WINDOW_PADDING
                screen = pygame.display.set_mode((win_width, win_height))

pygame.quit()
