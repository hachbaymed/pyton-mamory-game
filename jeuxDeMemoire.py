import os
import time
import random
import sys
from tkinter import messagebox
from tkinter import *


window = Tk()
window.geometry("460x655")
window.configure(background='#26917D')
window.resizable(width=False, height=False)
window.title("Jeux De Mémoire")
list = []

# Les images
I1 = PhotoImage(file='icon1.png')
I2 = PhotoImage(file='icon2.png')
I3 = PhotoImage(file='icon3.png')
I4 = PhotoImage(file='icon4.png')
I5 = PhotoImage(file='icon5.png')
I6 = PhotoImage(file='icon6.png')
I7 = PhotoImage(file='icon7.png')
I8 = PhotoImage(file='icon8.png')
imgs = [I1, I2, I3, I4, I5, I6, I7, I8, I1, I2, I3, I4, I5, I6, I7, I8]
count = 0

win = []


def click(New, Old, i, j):
    global win, count, s, OldOne, NewOne, II, JJ
    count += 1

    if count > 20:
        messagebox.showwarning(title='Game Over',
                               message='Vous Avez Deppaser Le Nombre D\'Essaies')
        window.destroy()
    if count % 2 != 0:
        Old.grid(row=10, column=10)
        New.grid(row=i, column=j)
        OldOne = Old
        NewOne = New
        II = i
        JJ = j
        s = New['image']
    else:
        if s == New['image']:
            Old.grid(row=10, column=10)
            New.grid(row=i, column=j)
            win.append(1)
            count -= 2
        else:
            Old.grid(row=10, column=10)
            New.grid(row=i, column=j)
            window.update()
            time.sleep(0.02)
            NewOne.grid(row=10, column=10)
            OldOne.grid(row=II, column=JJ)
            New.grid(row=10, column=10)
            Old.grid(row=i, column=j)
    if len(win) >= 8:
        messagebox.showinfo(title="Congratulation", message="Vous Avez Gagnez")


def Restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)


# Declaration des button avec image
B1 = Button(window, bg='#2FDEBD', height=124, width=110,
            activebackground='red', image=I1)
B2 = Button(window, bg='#2FDEBD', height=124, width=110,
            activebackground='red', image=I2)
B3 = Button(window, bg='#2FDEBD', height=124, width=110,
            activebackground='red', image=I3)
B4 = Button(window, bg='#2FDEBD', height=124, width=110,
            activebackground='red', image=I4)
B5 = Button(window, bg='#2FDEBD', height=124, width=110,
            activebackground='red', image=I5)
B6 = Button(window, bg='#2FDEBD', height=124, width=110,
            activebackground='red', image=I6)
B7 = Button(window, bg='#2FDEBD', height=124, width=110,
            activebackground='red', image=I7)
B8 = Button(window, bg='#2FDEBD', height=124, width=110,
            activebackground='red', image=I8)
B11 = Button(window, bg='#2FDEBD', height=124, width=110,
             activebackground='red', image=I1)
B22 = Button(window, bg='#2FDEBD', height=124, width=110,
             activebackground='red', image=I2)
B33 = Button(window, bg='#2FDEBD', height=124, width=110,
             activebackground='red', image=I3)
B44 = Button(window, bg='#2FDEBD', height=124, width=110,
             activebackground='red', image=I4)
B55 = Button(window, bg='#2FDEBD', height=124, width=110,
             activebackground='red', image=I5)
B66 = Button(window, bg='#2FDEBD', height=124, width=110,
             activebackground='red', image=I6)
B77 = Button(window, bg='#2FDEBD', height=124, width=110,
             activebackground='red', image=I7)
B88 = Button(window, bg='#2FDEBD', height=124, width=110,
             activebackground='red', image=I8)
Buttons = [B1, B2, B3, B4, B5, B6, B7, B8,
           B11, B22, B33, B44, B55, B66, B77, B88]
for button in Buttons:
    r = random.choice(imgs)
    button['image'] = r
    imgs.remove(r)


lab = Label(window, text='JEUX DE MÉMOIRE', bg='#26917D', fg='white',
            height=3, width=30, font='Arial 15 bold')
lab.grid(row=0, column=1, columnspan=4)

b1 = Button(window, bg='#2FDEBD', height=8, width=15,
            command=lambda: click(B1, l[0], 1, 1))

b2 = Button(window, bg='#2FDEBD', height=8, width=15,
            command=lambda: click(B2, l[1], 1, 2))

b3 = Button(window, bg='#2FDEBD', height=8, width=15,
            command=lambda: click(B3, l[2], 1, 3))

b4 = Button(window, bg='#2FDEBD', height=8, width=15,
            command=lambda: click(B4, l[3], 1, 4))

b5 = Button(window, bg='#2FDEBD', height=8, width=15,
            command=lambda: click(B5, l[4], 2, 1))

b6 = Button(window, bg='#2FDEBD', height=8, width=15,
            command=lambda: click(B6, l[5], 2, 2))

b7 = Button(window, bg='#2FDEBD', height=8, width=15,
            command=lambda: click(B7, l[6], 2, 3))

b8 = Button(window, bg='#2FDEBD', height=8, width=15,
            command=lambda: click(B8, l[7], 2, 4))

b9 = Button(window, bg='#2FDEBD', height=8, width=15,
            command=lambda: click(B11, l[8], 3, 1))

b10 = Button(window, bg='#2FDEBD', height=8, width=15,
             command=lambda: click(B22, l[9], 3, 2))

b11 = Button(window, bg='#2FDEBD', height=8, width=15,
             command=lambda: click(B33, l[10], 3, 3))

b12 = Button(window, bg='#2FDEBD', height=8, width=15,
             command=lambda: click(B44, l[11], 3, 4))

b13 = Button(window, bg='#2FDEBD', height=8, width=15,
             command=lambda: click(B55, l[12], 4, 1))

b14 = Button(window, bg='#2FDEBD', height=8, width=15,
             command=lambda: click(B66, l[13], 4, 2))

b15 = Button(window, bg='#2FDEBD', height=8, width=15,
             command=lambda: click(B77, l[14], 4, 3))

b16 = Button(window, bg='#2FDEBD', height=8, width=15,
             command=lambda: click(B88, l[15], 4, 4))


quitter = Button(window, text='Quitter', bg='grey',
                 font='Arial 20 bold', width=13, command=window.destroy)

quitter.grid(row=5, column=1, columnspan=2)

Recommencer = Button(window, text='Recommencer', bg='grey',
                     font='Arial 20 bold', width=13, command=lambda: Restart())

Recommencer.grid(row=5, column=3, columnspan=2)


l = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16]
for j in l:
    j['cursor'] = 'dotbox'


B1.grid(row=1, column=1)
B2.grid(row=1, column=2)
B3.grid(row=1, column=3)
B4.grid(row=1, column=4)
B5.grid(row=2, column=1)
B6.grid(row=2, column=2)
B7.grid(row=2, column=3)
B8.grid(row=2, column=4)
B11.grid(row=3, column=1)
B22.grid(row=3, column=2)
B33.grid(row=3, column=3)
B44.grid(row=3, column=4)
B55.grid(row=4, column=1)
B66.grid(row=4, column=2)
B77.grid(row=4, column=3)
B88.grid(row=4, column=4)

window.update()
time.sleep(2)

b1.grid(row=1, column=1)
b2.grid(row=1, column=2)
b3.grid(row=1, column=3)
b4.grid(row=1, column=4)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)
b7.grid(row=2, column=3)
b8.grid(row=2, column=4)
b9.grid(row=3, column=1)
b10.grid(row=3, column=2)
b11.grid(row=3, column=3)
b12.grid(row=3, column=4)
b13.grid(row=4, column=1)
b14.grid(row=4, column=2)
b15.grid(row=4, column=3)
b16.grid(row=4, column=4)


window.mainloop()


window.mainloop()
