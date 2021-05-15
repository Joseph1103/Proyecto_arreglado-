# Joseph Coronado Alvarado
# Operacion Moonlight
# Primero se procedera con la creacion del menu junto con todos sus agregados para luego proceder con el videojuego
# import tkinter
from tkinter import *
import pygame
from threading import Thread
import time

# Musica
pygame.mixer.init()
def play():
    pygame.mixer.music.load("C:/Users/50685/Downloads/Zanac intro.mp3")
    pygame.mixer.music.play(loops=5000)
def stop():
    pygame.mixer.music.stop()

def play_laser():
    pygame.mixer.music.load("C:/Users/50685/Desktop/Escritorio/Sprites para el juego/laser1.png")
    pygame.mixer.music.play(loops=0)

# Pantalla Principal y ventanas
class Ventana():
    def __init__(self, ventana):
        self.ventana = ventana
        self.canvas = Canvas(self.ventana, width=350, height=450,bg="white", highlightbackground="White")
        self.canvas.pack()
        self.canvas.place(x=-5, y=0)
        self.PantallaPrincipal()

    def PantallaPrincipal(self):
        global flag_bullet
        global jefe
        global vida
        vida = 50
        global vida_enemigo1
        vida_enemigo1 = 30
        global score
        score = 0
        flag_bullet = False
        self.canvas = Canvas(self.ventana, width=350, height=450, highlightbackground="White")
        bg = PhotoImage(file="C:/Users/50685/Imagenes/Imágenes/fondo.gif")
        self.canvas.create_image(0, 0, image=bg, anchor="nw")
        self.canvas.place(x=-5, y=0)
        self.canvas.create_text(180, 125, text="OPERATION \nMOON LIGHT", font=("Airstrike", 25), fill="green")
        self.canvas.create_text(180, 45, text="ENTER YOUR NAME", font=("Airstrike", 15), fill="green")
# Entry del nombre
        un_entry = Entry(self.ventana, font=("Airstrike", 20),width=10, fg="black")
        un_window = self.canvas.create_window(80,55, anchor="nw", window=un_entry)
# Boton nivel 1
        self.boton_start = Button(self.canvas, text="Level 1", font=("Airstrike",10), command=self.first_level)
        self.boton_start.place(x=85, y=300)
# Boton nivel 2
        self.boton_second_level = Button(self.canvas, text="Level 2", font=("Airstrike", 10), command=self.second_level)
        self.boton_second_level.place(x=150, y=300)
# Boton nivel 3
        self.boton_third_level = Button(self.canvas, text="Level 3", font=("Airstrike", 10), command=self.third_level)
        self.boton_third_level.place(x=218, y=300)
# Boton pagina de creditos
        self.boton_credits = Button(self.canvas, text="Credits", font=("Airstrike",10),command=self.credits)
        self.boton_credits.place(x=0, y=400)
# Boton Quitar juego
        self.boton_quitButton = Button(self.canvas, text="Quit", font=("Airstrike", 10), command=self.quitGame)
        self.boton_quitButton.place(x=300, y=400)
        self.ventana.mainloop()
# Nivel 1
    def first_level(self):
        self.canvas = Canvas(self.ventana, width=350, height=450, highlightbackground="White")
        self.canvas.place(x=-5, y=0)
        bg = PhotoImage(file="C:/Users/50685/Imagenes/Imágenes/partida.png")
        self.canvas.create_image(0, 0, image=bg, anchor="nw")
        self.boton2 = Button(self.canvas, text="Menu", font=("Airstrike", 10), bg="Yellow",command=self.PantallaPrincipal)
        self.boton2.place(x=0, y=0)

# Nave
        self.nave_player = PhotoImage(file="C:/Users/50685/Desktop/Escritorio/Pixel Spaceships/nav.png")
        self.nave = self.canvas.create_image(142, 360, anchor=NW, image=self.nave_player)

# Boss 1
        self.boss_l1 = PhotoImage(file="C:/Users/50685/Desktop/Escritorio/Pixel Spaceships/boss1.png")
        self.boss = self.canvas.create_image(135, 10, anchor=NW, image=self.boss_l1)

# Barra de progreso del jugador, jefes y tiempo
        self.progresbar = LabelFrame(self.canvas, width= 500, height=25, background = "black")
        self.progresbar.place(x=0, y=423)
        self.vida = Label(self.canvas, text= "Vida: "+ str(vida),font=("Airstrike", 11))
        self.vida.place(x = 5, y =423)

        self.Label_time =  Label(self.canvas, text="Time")
        self.Label_time.place(x = 100, y = 423)

        self.minutos1 = Label(self.canvas, text=int("0"), font=("Airstrike", 11))
        self.minutos1.place(x= 133, y=423)

        self.label_divi = Label(self.canvas, text=":", font=("Airstrike", 11))
        self.label_divi.place(x=147, y=423)

        self.segundos1 = Label(self.canvas, text="", font=("Airstrike", 11))
        self.segundos1.place(x=152, y=423)

        self.sec1=0
        self.min1=0
        self.contar_segundos1()

    def contar_segundos1(self):
        if self.sec1 != 60:
            self.sec1 += 1
            self.zero1 = ""
            if 0 <= self.sec1 < 10:
                self.zero1 = "0" +str(self.sec1)
            else:
                 self.zero1 = str(self.sec1)
            self.segundos1.configure(text= self.zero1)
            self.canvas.after(1000, self.contar_segundos1)
        elif self.sec1 == 60:
            self.sec1 = 0
            self.min1 += 1
            self.minutos1.configure(text = self.min1)


# Mecanica de disparo
        def Bullet(disparo):
            global flag_bullet
            flag_bullet = True
            flag = True
            while flag_bullet and flag:
                try:
                    if self.canvas.coords(disparo)[1] < -20:
                        flag = False
                        self.canvas.delete(disparo)
                    else:
                        self.canvas.move(disparo, 0, -10)
                        print("Disparo")
                        time.sleep(0.03)
                except Exception as errtxt:
                            print("Error en hilo")

 # Movimiento de la nave y disparo
        def left(event):
            x = -12
            y = 0
            self.canvas.move(self.nave, x, y)

        def right(event):
            x = 12
            y = 0
            self.canvas.move(self.nave, x, y)

        def up(event):
            x = 0
            y = -12
            self.canvas.move(self.nave, x, y)

        def down(event):
            x = 0
            y = 12
            self.canvas.move(self.nave, x, y)

        def space(event):
            coords = self.canvas.coords(self.nave)
            bullet_player = PhotoImage(file="C:/Users/50685/Desktop/Escritorio/Sprites para el juego/laser1.png")
            bullet = self.canvas.create_image(coords[0]+18, coords[1], anchor=NW, image=bullet_player)
            a = Thread(target=Bullet, args=(bullet,))

            a.start()

            self.ventana.mainloop()

        self.ventana.bind("<Left>", left)
        self.ventana.bind("<Right>", right)
        self.ventana.bind("<Up>", up)
        self.ventana.bind("<Down>", down)
        self.ventana.bind("<space>", space)

        self.ventana.mainloop()

#######################################################################################################################
# segundo nivel

    def second_level(self):
        self.canvas = Canvas(self.ventana, width=350, height=450, highlightbackground="White")
        bg = PhotoImage(file="C:/Users/50685/Imagenes/Imágenes/partida.png")
        self.canvas.create_image(0, 0, image=bg, anchor="nw")
        self.canvas.place(x=-5, y=0)

        self.boton2 = Button(self.canvas, text="Menu", font=("Airstrike", 10), bg="Yellow", command=self.PantallaPrincipal)
        self.boton2.place(x=0, y=0)
        # Nave
        self.nave_player = PhotoImage(file="C:/Users/50685/Desktop/Escritorio/Pixel Spaceships/nav.png")
        self.nave = self.canvas.create_image(142, 360, anchor=NW, image=self.nave_player)

# boss_2
        self.boss_2 = PhotoImage(file="C:/Users/50685/Desktop/Escritorio/Pixel Spaceships/boss2.png")
        self.boss2 = self.canvas.create_image(122, 5, anchor=NW, image=self.boss_2)

# Barra de progreso del jugador, jefes y tiempo
        self.progresbar = LabelFrame(self.canvas, width=500, height=25, background="black")
        self.progresbar.place(x=0, y=423)
        self.vida = Label(self.canvas, text="Vida: " + str(vida), font=("Airstrike", 11))
        self.vida.place(x=5, y=423)

        self.Label_time = Label(self.canvas, text="Time")
        self.Label_time.place(x=100, y=423)

        self.minutos2 = Label(self.canvas, text=int("0"), font=("Airstrike", 11))
        self.minutos2.place(x=133, y=423)

        self.label_divi = Label(self.canvas, text=":", font=("Airstrike", 11))
        self.label_divi.place(x=147, y=423)

        self.segundos2 = Label(self.canvas, text="", font=("Airstrike", 11))
        self.segundos2.place(x=152, y=423)

        self.sec2 = 0
        self.min2 = 0
        self.contar_segundos2()

    def contar_segundos2(self):
        if self.sec2 != 60:
            self.sec2 += 1
            self.zero2 = ""
            if 0 <= self.sec2 < 10:
                self.zero2 = "0" + str(self.sec2)
            else:
                self.zero2 = str(self.sec2)
            self.segundos2.configure(text=self.zero2)
            self.canvas.after(1000, self.contar_segundos2)
        elif self.sec2 == 60:
            self.sec2 = 0
            self.min2 += 1
            self.minutos1.configure(text=self.min2)


# mecanicas de disparo
        def Bullet(disparo):
            global flag_bullet
            flag_bullet = True
            flag = True
            while flag_bullet and flag:
                try:
                    if self.canvas.coords(disparo)[1] < -20:
                        flag = False
                        self.canvas.delete(disparo)
                    else:
                        self.canvas.move(disparo, 0, -10)
                        print("Ayuda")
                        time.sleep(0.03)


                except Exception as errtxt:
                    print("Error en hilo")

        # Movimiento de la nave y disparo
        def left(event):
            x = -12
            y = 0
            self.canvas.move(self.nave, x, y)

        def right(event):
            x = 12
            y = 0
            self.canvas.move(self.nave, x, y)

        def up(event):
            x = 0
            y = -12
            self.canvas.move(self.nave, x, y)

        def down(event):
            x = 0
            y = 12

            self.canvas.move(self.nave, x, y)

        def space(event):
            coords = self.canvas.coords(self.nave)
            bullet_player = PhotoImage(file="C:/Users/50685/Desktop/Escritorio/Sprites para el juego/laser1.png")
            bullet = self.canvas.create_image(coords[0]+18, coords[1], anchor=NW, image=bullet_player)
            a = Thread(target=Bullet, args=(bullet,))

            a.start()
            self.ventana.mainloop()

        self.ventana.bind("<Left>", left)
        self.ventana.bind("<Right>", right)
        self.ventana.bind("<Up>", up)
        self.ventana.bind("<Down>", down)
        self.ventana.bind("<space>", space)
        self.ventana.mainloop()

########################################################################################################################
# tercer nivel

    def third_level(self):
        self.canvas = Canvas(self.ventana, width=350, height=450, highlightbackground="White")
        bg = PhotoImage(file="C:/Users/50685/Imagenes/Imágenes/partida.png")
        self.canvas.create_image(0, 0, image=bg, anchor="nw")
        self.canvas.place(x=-5, y=0)

        self.boton2 = Button(self.canvas, text="Menu", font=("Airstrike", 10), bg="Yellow",command=self.PantallaPrincipal)
        self.boton2.place(x=0, y=0)
        # Nave
        self.nave_player = PhotoImage(file="C:/Users/50685/Desktop/Escritorio/Pixel Spaceships/nav.png")
        self.nave = self.canvas.create_image(142, 360, anchor=NW, image=self.nave_player)

        #boos_3
        self.boss3_l3 = PhotoImage(file="C:/Users/50685/Desktop/Escritorio/Pixel Spaceships/boss3.png")
        self.boss3 = self.canvas.create_image(119, 5, anchor=NW, image=self.boss3_l3)

# Barra de progreso del jugador, jefes y tiempo
        self.progresbar = LabelFrame(self.canvas, width=500, height=25, background="black")
        self.progresbar.place(x=0, y=423)
        self.vida = Label(self.canvas, text="Vida: " + str(vida), font=("Airstrike", 11))
        self.vida.place(x=5, y=423)

        self.Label_time = Label(self.canvas, text="Time")
        self.Label_time.place(x=100, y=423)

        self.minutos3 = Label(self.canvas, text=int("0"), font=("Airstrike", 11))
        self.minutos3.place(x=133, y=423)

        self.label_divi = Label(self.canvas, text=":", font=("Airstrike", 11))
        self.label_divi.place(x=147, y=423)

        self.segundos3 = Label(self.canvas, text="", font=("Airstrike", 11))
        self.segundos3.place(x=152, y=423)

        self.sec3 = 0
        self.min3 = 0
        self.contar_segundos3()

    def contar_segundos3(self):
        if self.sec3 != 60:
            self.sec3 += 1
            self.zero3 = ""
            if 0 <= self.sec3 < 10:
                self.zero3 = "0" + str(self.sec3)
            else:
                self.zero3 = str(self.sec3)
            self.segundos3.configure(text=self.zero3)
            self.canvas.after(1000, self.contar_segundos3)
        elif self.sec3 == 60:
            self.sec3 = 0
            self.min3 += 1
            self.minutos3.configure(text=self.min3)

        # comportamiento del disparo
        def Bullet(disparo):
            global flag_bullet
            flag_bullet = True
            flag = True
            while flag_bullet and flag:
                try:
                    if self.canvas.coords(disparo)[1] < -20:
                        flag = False
                        self.canvas.delete(disparo)
                    else:
                        self.canvas.move(disparo, 0, -10)
                        print("Ayuda")
                        time.sleep(0.03)


                except Exception as errtxt:
                    print("Error en hilo")

        # Movimiento de la nave y disparo
        def left(event):
            x = -12
            y = 0
            self.canvas.move(self.nave, x, y)

        def right(event):
            x = 12
            y = 0
            self.canvas.move(self.nave, x, y)

        def up(event):
            x = 0
            y = -12
            self.canvas.move(self.nave, x, y)

        def down(event):
            x = 0
            y = 12
            self.canvas.move(self.nave, x, y)

        def space(event):
            coords = self.canvas.coords(self.nave)
            bullet_player = PhotoImage(file="C:/Users/50685/Desktop/Escritorio/Sprites para el juego/laser1.png")
            bullet = self.canvas.create_image(coords[0]+18, coords[1], anchor=NW, image=bullet_player)
            a = Thread(target=Bullet, args=(bullet,))

            a.start()
            self.ventana.mainloop()

        self.ventana.bind("<Left>", left)
        self.ventana.bind("<Right>", right)
        self.ventana.bind("<Up>", up)
        self.ventana.bind("<Down>", down)
        self.ventana.bind("<space>", space)
        self.ventana.mainloop()


########################################################################################################################
#Creditos
    def credits(self):
        self.canvas = Canvas(self.ventana, width=350, height=450, highlightbackground="White")
        bg = PhotoImage(file="C:/Users/50685/Imagenes/Imágenes/fondo.gif")
        self.canvas.create_image(0, 0, image=bg, anchor="nw")
        self.canvas.place(x=-5, y=0)
        self.canvas.create_text(180, 40, text="Created in Costa Rica", font=("Airstrike", 12), fill="green")
        self.canvas.create_text(180, 80, text="Tecnologico De Costa Rica,\nIngenieria en Computadores", font=("Airstrike", 12), fill="green")
        self.canvas.create_text(180, 120, text="Taller de Programacion,2021, Grupo", font=("Airstrike", 12), fill="green")
        self.canvas.create_text(180, 160, text="Leonardo Araya", font=("Airstrike", 12), fill="green")
        self.canvas.create_text(180, 200, text="Ver.1.0", font=("Airstrike", 12), fill="green")
        self.canvas.create_text(180, 240, text="Pogramador:\nJoseph Coronado Alvarado", font=("Airstrike", 12), fill="green")
        self.canvas.create_text(180, 280, text="Bibliotecas: Tkinter, Pygame", font=("Airstrike", 12), fill="green")
        self.canvas.create_text(180,320 , text="Derechos de distribucion reservados", font=("Airstrike", 12), fill="green")
        self.boton2 = Button(self.canvas, text="Menu", font=("Airstrike", 10), bg="Yellow", command=self.PantallaPrincipal)
        self.boton2.place(x=0, y=0)
        self.ventana.mainloop()

########################################################################################################################
#Creditos
    def quitGame(self):
        self.ventana.destroy()
        self.ventana.mainloop()


ventana = Tk()
ventana.title("Operation Moon Light")
ventana.minsize(350, 450)
ventana.resizable(width=NO, height=NO)
ventana.config(bg="Black")

miObjetoVentanas = Ventana(ventana)
ventana.mainloop()
















