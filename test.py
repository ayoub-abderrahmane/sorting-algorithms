from sorting import *
import colorsys 
import pygame
import sys
import random
import time


# Initialisation de Pygame
pygame.init()

# Définition des couleurs

# Dimensions de la fenêtre
WINDOW_WIDTH = 1250
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

# print("Couleur RGB:", hsv_to_rgb(h))

def color_circle_without_sort(xi,yi):
    colors = list(range(361))
    random.shuffle(colors)
    y=300
    x= xi+50
    i=0
    for color in colors:
        pygame.draw.line(window,hsv_to_rgb(color),(xi,yi) , (x ,y))
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

def color_circle(xi,yi,sort):
    starting=time.time()
    colors = list(range(361))
    random.shuffle(colors)
    y=300
    x= xi+50
    i=0
    # print(colors)
    colors = sort(colors)
    # print(colors)
    for color in colors:
        pygame.display.flip()
        pygame.draw.line(window,hsv_to_rgb(color),(xi,yi) , (x ,y))
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
    ending=time.time()
    total_time= (ending - starting)
    print(sort,":",total_time)
    

def message(size,message,message_rectangle,color):
    font=pygame.font.SysFont("arial",size)
    message = font.render(message,False,color)
    window.blit(message,message_rectangle) 
# Initialisation du cercle affiché
circle_displayed = False

# Boucle principale
running = True
sorting=[SelectionSort,MergeSort,QuikSort]
sortingMessage=["SelectionSort","MergeSort","QuikSort"]
total_time=0
while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Inversion de l'état du cercle affiché
                circle_displayed = not circle_displayed
                if circle_displayed:  
                    yi=300
                    xi=120
                    for i in sorting:
                        color_circle_without_sort(xi,yi)
                        xi+=180
                else:
                    yi=300
                    xi=120
                    m=0
                    for i in sorting:
                        color_circle(xi,yi,i)
                        message(24,f"{sortingMessage[m]}",(xi-75,yi+100,0,0),(255,255,255))
                        message(24,f"{total_time}",(xi-75,yi+135,0,0),(255,255,255))
                        xi+=180
                        m+=1
                        
                        
                
    # Mise à jour de l'affichage
    pygame.display.flip()
    
    # Limiter le taux de rafraîchissement
    pygame.time.Clock().tick(60)

# Quitter Pygame
pygame.quit()
sys.exit()



