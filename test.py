import tkinter

app=tkinter.Tk()

app.title("mélangeur")
app.geometry('1000x600')


def update_selection(*args):
    # Fonction appelée lorsque la sélection est mise à jour
    selected_option.set(var.get())

# Création de la fenêtre principale

# Options de la liste déroulante
options = ["Option 1", "Option 2", "Option 3", "Option 4"]

# Variable de contrôle pour stocker la sélection
var = tkinter.StringVar(app)
var.set(options[0])  # Sélection par défaut

# Création de la liste déroulante
dropdown = tkinter.OptionMenu(app, var, *options, command=update_selection)
dropdown.pack()

# Bouton pour afficher la sélection
selected_option = tkinter.StringVar(app)
selected_option.set(var.get())  # Initialisation du texte du bouton avec la sélection par défaut
button = tkinter.Button(app, textvariable=selected_option, state="disabled")
button.pack()

# Lancement de la boucle principale Tkinter

app.mainloop()
