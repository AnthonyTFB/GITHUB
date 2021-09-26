from tkinter import * 
from tkinter import messagebox
from tkinter import dialog
raiz = Tk()
raiz.title("LA LISTA DEL MAMADO")

def salir ():
    messagebox.ask

foto = PhotoImage(file="chemsalv.png")
Label(raiz, image=foto).pack()
Checkbutton(raiz, text="Proteina"). pack()
Checkbutton(raiz, text="Musica de señoras"). pack()
Checkbutton(raiz, text="Agua"). pack()
Checkbutton(raiz, text="Descanso"). pack()
Checkbutton(raiz, text="Mas proteina"). pack()
Checkbutton(raiz, text="GANAS DE VERSE COMO GOKU ALVRGAA"). pack()

raiz.mainloop()

