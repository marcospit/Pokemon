import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.style import Style

import heart

def get_value():
    e_text=entry.get()
    heart.pokemon(e_text)

app = ttk.Window("Pokemon")
app.geometry("550x500")
style = Style(theme="darkly")

label =  ttk.Label(app, text="Pokemon Finder")
label.pack(pady=35)
label.config(font=("Arial", 20, "bold"))


nome = ttk.Frame(app)
nome.pack(pady=18, padx=10, fill="x")
ttk.Label(nome,text= "Nome").pack(side=LEFT, padx=5)
entry = ttk.Entry(nome)
entry.pack(side=LEFT, fill="x", expand=True, padx=5)


button= ttk.Button(app, text="Enter", command= get_value)
button.pack()


app.mainloop()