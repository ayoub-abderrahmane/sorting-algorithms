from sorting import *
import colorsys 
import pygame
import sys
import random

# Initialisation de Pygame
pygame.init()

# Définition des couleurs

# Dimensions de la fenêtre
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Création de la fenêtre
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tri du spectre de couleur")

def hsv_to_rgb(h):
    """
    get HSV color and return RGB color. 
    h = num between 0 and 360 for the color id 
    """
    r, g, b = colorsys.hsv_to_rgb(h / 360.0, 1, 1)
    return int(r * 255), int(g * 255), int(b * 255)

h = 0 

print("Couleur RGB:", hsv_to_rgb(h))

def color_circle():
    colors = list(range(361))
    random.shuffle(colors)
    y=300
    x=450
    i=0
    print(colors)
    SelectionSort(colors)
    print(colors)
    for color in colors:
        pygame.draw.line(window,hsv_to_rgb(color),(400,300) , (x ,y))
        i+=1
        if i < 90:
            y+=1
            x-=1
            
        elif 360/4 < i < 360/4*2:
            y-=1
            x-=1
            
        elif 360/4*2 < i < 360/4*3:
            y-=1
            x+=1
        elif 360/4*3 < i < 360/4*4:
            
            y+=1
            x+=1
    
        


pygame.init()
window.fill((255, 255, 255))
color_circle()

pygame.display.flip()


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   


    pygame.display.flip()
    pygame.time.Clock().tick(60)


# Quitter Pygame
pygame.quit()
sys.exit()


