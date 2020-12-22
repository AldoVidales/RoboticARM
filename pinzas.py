import tkinter
from tkinter import *
from time import sleep
from pyfirmata import Arduino,util,SERVO

board = Arduino('COM3')
sleep(5)
board.digital[3].mode = SERVO
board.digital[5].mode = SERVO
board.digital[6].mode = SERVO
board.digital[10].mode = SERVO

def servo (posiciones):
    board.digital[3].write(posiciones)
    sleep(0.002)
    

def base(posicionbase):
    board.digital[5].write(posicionbase)
    sleep(0.002)

def tronco(posiciontronco):
    board.digital[6].write(posiciontronco)
    sleep(0.002)

def mano(posicionmano):
    board.digital[10].write(posicionmano)
    sleep(0.002)
    

root  = Tk()
root.title("CONTROL DE SERVO")
root.minsize(780,500)

angulo = Scale(root,
    command=servo,
    from_=0,
    to = 126,
    orient=HORIZONTAL,
    length =300,
    troughcolor = 'gray',
    width = 30,
    cursor = 'dot',
    label ='Pinzas')


angulo.grid(column = 2, row = 1)

eje2 = Scale(root,
   command = base,
   from_=0,
   to=180,
   orient=HORIZONTAL,
   length = 300,
   troughcolor = 'gray',
   width = 30,
   cursor = 'dot',
   label = 'Base')

eje2.grid(column=2 , row = 2)


eje3 = Scale(root,
   command = tronco,
   from_=0,
   to=90,
   orient=VERTICAL,
   length = 300,
   troughcolor = 'gray',
   width = 30,
   cursor = 'dot',
   label = 'Tronco')

eje3.grid(column=3 , row = 2)

manofx = Scale(root,
   command = mano,
   from_=0,
   to=70,
   orient=VERTICAL,
   length = 300,
   troughcolor = 'gray',
   width = 30,
   cursor = 'dot',
   label = 'MANO')

manofx.grid(column=4 , row = 2)

root.mainloop()





