from Bulles import Bulles
from Insertion import Insertion
from Peigne import Peigne
import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.list = [5,3,7,9,10,2,8,4,1,6]
        self.geometry("600x500")
        self.title("CTk example")
        self.bulles = Bulles(self.list)
        self.solving_bulles = self.bulles.sorting()
        self.button = customtkinter.CTkButton(self, command=self.button_click)
        self.button.grid(row=0, column=0, padx=20, pady=10)
        
        

    # add methods to app
    def button_click(self):
        self.textbox = customtkinter.CTkTextbox(master=self, width=400, corner_radius=0)
        self.textbox.grid(row=0, column=0, sticky="nsew")
        self.textbox.insert("0.0", self.solving_bulles) 

app = App()
app.mainloop()