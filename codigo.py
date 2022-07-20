from tkinter import *
from Bola import *
import time

window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

volei_bola = Bola(canvas,0,0,100,1,1,"white")
tenis_bola = Bola(canvas,0,0,50,4,3,"red")
basquete_bola = Bola(canvas,0,0,125,8,7,"yellow")
black_bola = Bola(canvas, 0, 0, 75, 2, 1, "black")

while True:
    volei_bola.move()
    tenis_bola.move()
    basquete_bola.move()
    black_bola.move()
    window.update()
    time.sleep(0.01)
window.mainloop()