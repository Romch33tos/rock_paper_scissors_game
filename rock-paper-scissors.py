import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
import random

list1 = [ 'Камень', 'Ножницы', 'Бумага']

root = Tk()

#Текстовый виджет

def rock():
    text.delete("1.0", END)  
    text.configure(state = NORMAL)
    answer = random.choice(list1)
    if answer == 'Камень':
        text.insert("1.0", "Твой выбор: Камень")
        text.insert(END, "\nМой выбор: " + str(answer))
        text.insert(END, "\nНичья!")
    if answer == 'Ножницы':
        text.insert("1.0", "Твой выбор: Камень")
        text.insert(END, "\nМой выбор: " + str(answer))
        text.insert(END, "\nЯ проиграл!")
    if answer == 'Бумага':
        text.insert("1.0", "Твой выбор: Камень")
        text.insert(END, "\nМой выбор: " + str(answer))
        text.insert(END, "\nЯ победил!")
    
def scissors():
    text.delete("1.0", END)  
    text.configure(state = NORMAL)
    answer = random.choice(list1)
    if answer == 'Камень':
        text.insert("1.0", "Твой выбор: Ножницы")
        text.insert(END, "\nМой выбор: " + str(answer))
        text.insert(END, "\nЯ победил!")
    if answer == 'Ножницы':
        text.insert("1.0", "Твой выбор: Ножницы")
        text.insert(END, "\nМой выбор: " + str(answer))
        text.insert(END, "\nНичья!")
    if answer == 'Бумага':
        text.insert("1.0", "Твой выбор: Ножницы")
        text.insert(END, "\nМой выбор: " + str(answer))
        text.insert(END, "\nЯ проиграл!")
    
def paper():
    text.delete("1.0", END)  
    text.configure(state = NORMAL)
    answer = random.choice(list1)
    if answer == 'Камень':
        text.insert("1.0", "Твой выбор: Бумага")
        text.insert(END, "\nМой выбор: " + str(answer))
        text.insert(END, "\nЯ проиграл!")
    if answer == 'Ножницы':
        text.insert("1.0", "Твой выбор: Бумага")
        text.insert(END, "\nМой выбор: " + str(answer))
        text.insert(END, "\nЯ победил")
    if answer == 'Бумага':
        text.insert("1.0", "Твой выбор: Бумага")
        text.insert(END, "\nМой выбор: " + str(answer))
        text.insert(END, "\nНичья!")
    
l1 = Label(root, text = "Камень, ножницы, бумага!")
l1.grid(row = 0, column = 0, padx = 165, pady = 7, sticky = NW)

text = Text(width = 36, height = 4)
text.grid(row = 1, column = 0, padx = 60,pady = 5, sticky = NW)

R = Button(root, width = 7, text = "Камень", command = lambda: rock())
R.grid(row = 4, column = 0, sticky = NW, padx = 60, pady = 7)

S = Button(root, width = 7, text = "Ножницы", command = lambda: scissors())
S.grid(row = 4, column = 0, sticky = NW, padx = 256, pady = 7)

P = Button(root, width = 7, text = "Бумага", command = lambda: paper())
P.grid(row = 4, column = 0, sticky = NW, padx = 452, pady = 7)

root.mainloop()