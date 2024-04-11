from sorting import *
import colorsys 
import pygame
import sys
import random
import time


# pygame init
pygame.init()

#widht and height of the window
WINDOW_WIDTH = 1250
WINDOW_HEIGHT = 600

# create the window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#page name
pygame.display.set_caption("Tri du spectre de couleur")

"""
function to convert hsv to rgb because hsv has 1 argument for color(the 2 other are for the saturation and brightness , 
it's not important)
and rgb has 3 argument. So more rgb is harder to associate a number to a color than hsv.
"""

def hsv_to_rgb(h):
    """
    get HSV color and return RGB color. 
    h = num between 0 and 360 for the color id 
    """
    r, g, b = colorsys.hsv_to_rgb(h / 360.0, 1, 1)
    return int(r * 255), int(g * 255), int(b * 255)
# print("Couleur RGB:", hsv_to_rgb(h))

def color_rectangle_without_sort(xi,yi,element_num):
    colors = list(range(element_num+1))
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

def color_rectangle(xi,yi,sort,element_num):
    total_time=0
    starting=time.time()
    colors = list(range(element_num+1))
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
    

def message(size,message,message_rectangle,color):
    font=pygame.font.SysFont("arial",size)
    message = font.render(message,False,color)
    window.blit(message,message_rectangle) 
# Initialisation du cercle affiché


def main():
    rectangle_displayed = False
    running = True
    sorting=[SelectionSort,MergeSort,QuikSort,bubble_sort,heap_sort]
    sortingMessage=["SelectionSort","MergeSort","QuikSort","bubble_sort","heap_sort"]
    total_time=0
    element_number=360
    while running:
        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    #display rectangle not sorted
                    message(24,f"elements:{element_number}",(0,0,0,0),(255,255,255))
                    rectangle_displayed = not rectangle_displayed
                    if rectangle_displayed:  
                        yi=300
                        xi=120
                        for i in sorting:
                            color_rectangle_without_sort(xi,yi,element_number)
                            xi+=180
                    else:
                        yi=300
                        xi=120
                        m=0
                        for i in sorting:
                            starting=time.time()
                            color_rectangle(xi,yi,i,element_number)
                            ending=time.time()
                            total_time=ending-starting
                            total_time = "{:.2f}".format(total_time)
                            message(24,f"{total_time}s",(xi-75,yi+135,0,0),(255,255,255))
                            message(24,f"{sortingMessage[m]}",(xi-75,yi+100,0,0),(255,255,255))

                            xi+=180
                            m+=1
                            
        pygame.display.flip()
        pygame.time.Clock().tick(60)

if __name__ == "__main__":
    main()





