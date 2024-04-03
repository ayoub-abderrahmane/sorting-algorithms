import tkinter as tk
import time

def tri_bulle_animation(tableau):
    n = len(tableau)
    for i in range(n):
        for j in range(0, n-i-1):
            if tableau[j] > tableau[j+1]:
                # Échange les deux éléments
                tableau[j], tableau[j+1] = tableau[j+1], tableau[j]
                
                # Met à jour l'affichage
                update_display(tableau, j, j+1)
                time.sleep(1)  # Délai pour l'animation

def update_display(tableau, index1, index2):
    canvas.delete("all")
    for i, value in enumerate(tableau):
        x0 = i * 50 + 50
        y0 = 50
        x1 = x0 + 40
        y1 = y0 + value * 10
        color = "blue" if i == index1 or i == index2 else "black"
        canvas.create_rectangle(x0, y0, x1, y1, fill=color)
        canvas.create_text((x0 + x1) // 2, y1 + 10, text=str(value))
    root.update_idletasks()

# Initialisation de la fenêtre Tkinter
root = tk.Tk()
root.title("Tri à bulles avec interface graphique")
root.geometry("600x400")

# Création d'un canvas pour dessiner les barres
canvas = tk.Canvas(root, width=600, height=300)
canvas.pack()

# Liste initiale
liste = [5, 3, 8, 1, 2]

# Affichage initial
update_display(liste, -1, -1)

# Bouton pour démarrer le tri
button = tk.Button(root, text="Démarrer le tri", command=lambda: tri_bulle_animation(liste))
button.pack()

root.mainloop()