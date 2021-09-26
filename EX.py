from tkinter import *
from tkinter import messagebox  

root = Tk()
root.state("zoomed")
root.title("MONEDERO CONTABLE")
root.iconbitmap("money.ico")
root.geometry("+0+0")


class Monedero ():
    barramenu = Menu(root)
    root.config(menu = barramenu, width=300, height=300)
    

    archivomenu= Menu(barramenu, tearoff=0)
    archivomenu.add_command(label= "Crear BDD")
    archivomenu.add_separator()
    archivomenu.add_command(label= "Salir")

    contabilidadmenu = Menu(barramenu,tearoff=0 )
    contabilidadmenu.add_command(label= "Deudas")
    contabilidadmenu.add_command(label= "Prestamo")
    contabilidadmenu.add_command(label= "General")
    contabilidadmenu.add_command(label= "Bancos")

    ayudamenu = Menu(barramenu, tearoff=0)
    ayudamenu.add_command(label= "Licencia")
    ayudamenu.add_command(label= "Version")
    ayudamenu.add_command(label= "Novedades")
    ayudamenu.add_command(label= "A cerca de...")

    barramenu.add_cascade(label="Archivo", menu=archivomenu)
    barramenu.add_cascade(label="Contabildad", menu=contabilidadmenu)
    barramenu.add_cascade(label="Ayuda", menu=ayudamenu)

    def loggin():
        mflog= Toplevel()
        mflog.title("Monedero- Sistema Contable-Acceso")
        mflog.iconbitmap("money.ico")
        mflog.geometry("+500+250")
        mflog2 = Frame(mflog)
        mflog2.pack(fill="both", expand="True")
        mflog2.config(bg="#1F1F1F")
        mflog2.config(width="1200", height="600")
        mflog2.config(bd=15)
        mflog2.config(relief="groove")

        def verificar():
            if micuadrousuario.get().upper() == "USER" and micuadroclave.get().upper()=="1234":
                messagebox.showinfo(title="Login correcto", message="bienvenido"+ micuadrousuario.get())
                mflog.destroy()
                root.iconify()
                root.deiconify
            else:
                messagebox.showerror(title="Login incorrecto", message="Usuario o contraseña  incorrecta")


        micuadrousuario = StringVar()
        micuadroclave = StringVar()



    miframme = Frame(root)
    miframme.pack(fill="both", expand="True")
    miframme.config(bg="#1F1F1F")
    miframme.config(width="1280", height="676")
    miframme.config(bd=15)
    miframme.config(relief="groove")
    foto =  PhotoImage(file="SUCCES.png")
    Label(miframme, image=foto, bg="#1F1F1F").pack()
    foto2 =  PhotoImage(file="chemsalv.png")
    Label(miframme, image=foto2, bg="#1F1F1F").pack()



    root.mainloop()



