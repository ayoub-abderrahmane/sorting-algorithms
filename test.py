import tkinter
from sorting import *

import colorsys
import math
app=tkinter.Tk()

app.title("mélangeur")
app.geometry('1000x600')
canvas = tkinter.Canvas(app, width=400, height=400)
canvas.pack()

def generate_colors(num_colors):
    # Générer les couleurs dans un spectre de couleur (arc-en-ciel)
    colors = [colorsys.hsv_to_rgb(h, 1.0, 1.0) for h in [(i / num_colors) for i in range(num_colors)]]
    return colors

def draw_circle(canvas, center_x, center_y, radius, num_colors,func):
    colors = generate_colors(num_colors)
    sorted_colors = func(colors)
    for i, color in enumerate(sorted_colors):
        angle = 2 * math.pi * i / num_colors
        x = center_x + radius * math.cos(angle)
        y = center_y - radius * math.sin(angle)  # Minus to adjust for tkinter's upside-down coordinates
        canvas.create_line(center_x, center_y, x, y, fill=f'#{int(color[0]*255):02x}{int(color[1]*255):02x}{int(color[2]*255):02x}')

def update_selection(*args):
    # Fonction appelée lorsque la sélection est mise à jour
    selected_option.set(var.get())

# Création de la fenêtre principale
def test():
    print("helloworld")
# Options de la liste déroulante
options = ["MergeSort" , "QuikSort" , "SelectionSort" , "test"]

functions = [MergeSort , QuikSort , SelectionSort,test]

# Variable de contrôle pour stocker la sélection
var = tkinter.StringVar(app)
var.set(options[0])  # Sélection par défaut

# Bouton pour afficher la sélection
selected_option = tkinter.StringVar(app)
selected_option.set(var.get())  # Initialisation du texte du bouton avec la sélection par défaut
button = tkinter.Button(app, textvariable=selected_option, state="disabled")
button.pack()

def execute_selected_function(*args,func):
    selected_index = options.index(var.get())
    draw_circle[selected_index](canvas, 200, 200, 150, 1000,functions)

# Création de la liste déroulante
dropdown = tkinter.OptionMenu(app, var, *options, command=execute_selected_function)
dropdown.pack()
# Lancement de la boucle principale Tkinter

app.mainloop()
