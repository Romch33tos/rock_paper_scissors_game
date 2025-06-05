import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
import random
l = 0
d = 0
w = 0
list1 = [ 'Камень', 'Ножницы', 'Бумага']
root = Tk()
txt = StringVar()
txt2 = StringVar()
txt3 = StringVar()
def rock():
    answer = random.choice(list1)
    text.configure(state = NORMAL)
    text.delete("1.0", END)  
    text.insert("1.0", "Камень, ножницы, бумага!")
    text.insert(END, "\nРаз, два, три!")
    text.insert(END, "\nТвой выбор: Камень")
    if answer == 'Камень':
        global d
        d +=1        
        txt3.set(str(d))   
        text.insert(END, "\nМой выбор: " + str(answer))
        text.insert(END, "\nНичья!")
        text.configure(state = DISABLED)
    if answer == 'Ножницы':
        global w
        w += 1
        txt.set(str(w))        
        text.insert(END, "\nМой выбор: " + str(answer))
        text.insert(END, "\nЯ проиграл!")
        text.configure(state = DISABLED)
    if answer == 'Бумага':
        global l
        l += 1
        txt2.set(str(l))      
        text.insert(END, "\nМой выбор: " + str(answer))
        text.insert(END, "\nЯ победил!")
        text.configure(state = DISABLED)    
def scissors():
    answer = random.choice(list1)
    text.configure(state = NORMAL)
    text.delete("1.0", END)  
    text.insert("1.0", "Камень, ножницы, бумага!")
    text.insert(END, "\nРаз, два, три!")
    text.insert(END, "\nТвой выбор: Ножницы")
    if answer == 'Камень':
        global l
        l += 1 
        txt2.set(str(l))      
        text.insert(END, "\nМой выбор: " + str(answer))
        text.insert(END, "\nЯ победил!")
        text.configure(state = DISABLED)
    if answer == 'Ножницы':
        global d
        d +=1
        txt3.set(str(d))   
        text.insert(END, "\nМой выбор: " + str(answer))
        text.insert(END, "\nНичья!")
        text.configure(state = DISABLED)
    if answer == 'Бумага':
        global w
        w += 1
        txt.set(str(w))        
        text.insert(END, "\nМой выбор: " + str(answer))
        text.insert(END, "\nЯ проиграл!")
        text.configure(state = DISABLED)    
def paper():
    answer = random.choice(list1)
    text.configure(state = NORMAL)
    text.delete("1.0", END)  
    text.insert("1.0", "Камень, ножницы, бумага!")
    text.insert(END, "\nРаз, два, три!")
    text.insert(END, "\nТвой выбор: Бумага")
    if answer == 'Камень':
        global w
        w += 1 
        txt.set(str(w))      
        text.insert(END, "\nМой выбор: " + str(answer))
        text.insert(END, "\nЯ проиграл!")
        text.configure(state = DISABLED)
    if answer == 'Ножницы':
        global l
        l +=1
        txt2.set(str(l))   
        text.insert(END, "\nМой выбор: " + str(answer))
        text.insert(END, "\nТы проиграл")
        text.configure(state = DISABLED)
    if answer == 'Бумага':
        global d
        d += 1
        txt3.set(str(d))        
        text.insert(END, "\nМой выбор: " + str(answer))
        text.insert(END, "\nНичья!")
        text.configure(state = DISABLED)

l1 = Label(root, text = "Камень, ножницы, бумага!")
l1.grid(row = 0, column = 0, padx = 165, pady = 7, sticky = NW)

l5 = Label(root, text = "Выбери свой жест: ")
l5.grid(row = 5, column = 0, padx = 60,  pady = 7, sticky = NW)

text = Text(width = 36, height = 5)
text.grid(row = 1, column = 0, padx = 60,pady = 5, sticky = NW)

R = Button(root, width = 7, text = "Камень", command = lambda: rock())
R.grid(row = 6, column = 0, sticky = NW, padx = 60, pady = 7)

S = Button(root, width = 7, text = "Ножницы", command = lambda: scissors())
S.grid(row = 6, column = 0, sticky = NW, padx = 256, pady = 7)

P = Button(root, width = 7, text = "Бумага", command = lambda: paper())
P.grid(row = 6, column = 0, sticky = NW, padx = 452, pady = 7)

root.mainloop()
