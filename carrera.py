from tkinter import*
import random
#funciones del juego
#funcio para modificar
#def modificar_imagen(posicion):
   # c.itemconfig(modificar_imagen, extent= posicion)


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
rect_1 = c.create_rectangle(BASE/2-150,BASE/2+220,125,ALTURA-220,fill="pink", outline="blue")
rect_2 = c.create_rectangle(BASE/2+200,BASE/2+200,380,ALTURA-220,fill="cyan", outline="blue")


rect_3 = c.create_rectangle(BASE/2+20,BASE/2-120,130,ALTURA-120,fill="white", outline="white")
rect_4 = c.create_rectangle(BASE/2+20,BASE/2-120,180,ALTURA-120,fill="white", outline="white")
rect_3 = c.create_rectangle(BASE/2+40,ALTURA/2-10,BASE/2+150,ALTURA/2,fill="white", outline="white")
# img
carro1 = PhotoImage(file="img/rayo.png")
car = c.create_image(BASE/2-185, 340/2, image = carro1)

carro2 = PhotoImage(file="img/flo (1).png")
carr = c.create_image(BASE/2-185, 110/2, image = carro2)


velocidad_x1= random.randint(2,4)
velocidad_x2= random.randint(2,4)
intervalo=90

def mover_carro():
    global velocidad_x1
    c.move(carro1, velocidad_x1,0)
    frame_graficacion.after(intervalo,mover_carro)
    c.move(carro2,velocidad_x2,0)
    frame_graficacion.after(intervalo, mover_carro)


# tectos de inicio y fin
texto_1 = c.create_text(BASE/2+10, ALTURA-205, anchor="center", text="carrerass!", font=("Arial",25, "bold"),fill="deep pink",
activefill="green2")

texto_s = c.create_text(BASE/2-125, ALTURA-190, anchor="center", text="s", font=("Arial",25, "bold"),fill="white",
activefill="pink")
texto_a = c.create_text(BASE/2-125, ALTURA-160, anchor="center", text="a", font=("Arial",25, "bold"),fill="white",
activefill="pink")
texto_l = c.create_text(BASE/2-125, ALTURA-130, anchor="center", text="l", font=("Arial",25, "bold"),fill="white",
activefill="pink")
texto_i = c.create_text(BASE/2-125, ALTURA-100, anchor="center", text="i", font=("Arial",25, "bold"),fill="white",
activefill="pink")
texto_d = c.create_text(BASE/2-125, ALTURA-70, anchor="center", text="d", font=("Arial",25, "bold"),fill="white",
activefill="pink")
texto_a = c.create_text(BASE/2-125, ALTURA-40, anchor="center", text="a", font=("Arial",25, "bold"),fill="white",
activefill="pink")

texto_f = c.create_text(BASE/2+175, ALTURA-160, anchor="center", text="f", font=("Arial",25, "bold"),fill="white",
activefill="cyan")
texto_i = c.create_text(BASE/2+175, ALTURA-120, anchor="center", text="i", font=("Arial",25, "bold"),fill="white",
activefill="cyan")
texto_n = c.create_text(BASE/2+175, ALTURA-90, anchor="center", text="n", font=("Arial",25, "bold"),fill="white",
activefill="cyan")



#--------------------
#frame de controles
#-------------------

frame_controles = Frame(ventana_principal)
frame_controles.config(bg="green", width=480, heigh=230)
frame_controles.place(x=10, y=260)


#boton para datos academicos
bandera=PhotoImage(file="img/bandera (2).png")
bt_bandera =Button(ventana_principal)
bt_bandera.config(image=bandera, width=100, height=100)
bt_bandera.place(x=200, y=270)
def mover_carro():
    global velocidad_x1
    c.move(carro1, velocidad_x1,0)
    frame_graficacion.after(intervalo,mover_carro)
    c.move(carro2,velocidad_x2,0)
    frame_graficacion.after(intervalo, mover_carro)


#desplegar ventana
ventana_principal.mainloop()