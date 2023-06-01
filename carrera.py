from tkinter import*


#-----------------
#variables globales
#------------------

BASE=460
ALTURA=220

#----------------------
#ventana principal
#----------------------

ventana_principal = Tk()
ventana_principal.title("Graficas 2D")
ventana_principal.resizable(False, False)
ventana_principal.geometry("500x500")
ventana_principal.config(bg="white")

#-----------------------
#frame de graficacion
#-----------------------

frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="green", width=480, height=240)
frame_graficacion.place(x=10,y=10)

#creacion canvas

c= Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.config(bg="light grey")
c.place(x=10, y=10)


#llegada
calle = c.create_rectangle(BASE/2-220,BASE/2-40,450,ALTURA-190,fill="black", outline="blue")
rect_1 = c.create_rectangle(BASE/2-150,BASE/2+220,150,ALTURA-220,fill="pink", outline="blue")
rect_2 = c.create_rectangle(BASE/2+200,BASE/2+200,360,ALTURA-220,fill="cyan", outline="blue")


# img
carro1 = PhotoImage(file="img/rayo.png")
car = c.create_image(BASE/2-175, 340/2, image = carro1)

carro2 = PhotoImage(file="img/flo (1).png")
carr = c.create_image(BASE/2-175, 110/2, image = carro2)


# tectos de inicio y fin
texto_1 = c.create_text(BASE/2+10, ALTURA-205, anchor="center", text="carrerass!", font=("Arial",25, "bold"),fill="white",
activefill="cyan")

#--------------------
#frame de controles
#-------------------

frame_controles = Frame(frame_graficacion)
frame_controles.config(bg="green", width=480, height=230)
frame_controles.place(x=10, y=260)

#desplegar ventana
ventana_principal.mainloop()