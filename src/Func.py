from math import *
import pygame



def f(x):
    return x**2


pygame.init()



fenetre = pygame.display.set_mode()
l,h = fenetre.get_size()

WINDOWWIDTH = l
WINDOWHEIGHT = h

pygame.display.set_caption("Menu")
font = pygame.font.Font('freesansbold.ttf', 20)

def draw(screen, function, scale_x, scale_y, offset_x, offset_y):
    points = []
    for x_pixel in range(WINDOWWIDTH):
        x = (x_pixel - offset_x) / scale_x
        y = function(x)
        y_pixel = offset_y - y * scale_y
        points.append((x_pixel, y_pixel))
    if len(points) > 1:
        pygame.draw.lines(screen, (255, 0,0), False, points, 2)
        
def implicit_equation(x, y):
    return x**2 + y**2 - 100  # Circle equation: x^2 + y^2 = 100

# Draw implicit equation
def draw_implicit_equation(screen, equation, scale_x, scale_y, offset_x, offset_y):
    for x_pixel in range(width):
        for y_pixel in range(height):
            # Convert pixel coordinates to math coordinates
            x = (x_pixel - offset_x) / scale_x
            y = (offset_y - y_pixel) / scale_y  # Invert y-axis
            # Check if the equation is approximately satisfied
            if abs(equation(x, y)) < 0.1:  # Allow a small tolerance
                screen.set_at((x_pixel, y_pixel), red)  # Draw a point
        

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                pygame.quit()
                break


    fenetre.fill((52,78,91))
    pygame.draw.line(fenetre, (0, 0, 0), (0, WINDOWHEIGHT//2), (WINDOWWIDTH, WINDOWHEIGHT//2), 2) 
    pygame.draw.line(fenetre, (0, 0, 0), (WINDOWWIDTH//2, 0), (WINDOWWIDTH//2, WINDOWHEIGHT), 2) 

    
    draw(fenetre, f, 100,100, WINDOWWIDTH//2, WINDOWHEIGHT//2)


    pygame.display.update()