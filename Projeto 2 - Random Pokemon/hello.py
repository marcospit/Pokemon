import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.style import Style
import tkinter.messagebox
import random 
import heart

def get_value():
    n = random.randint(1,151)
    pk_name = heart.pokemon(str(n))
    message ="Parabens, você é um(a) "+ pk_name 
    tkinter.messagebox.showinfo(title="!!!", message=message)
    
app = ttk.Window("Pokemon")
app.geometry("550x500")
style = Style(theme="darkly")

label =  ttk.Label(app, text="Pokemon Random")
label.pack(pady=35)
label.config(font=("Arial", 20, "bold"))

button= ttk.Button(app, text="Roll the Dice", command= get_value)
button.pack()

app.mainloop()