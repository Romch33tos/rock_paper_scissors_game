import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
from PIL import ImageTk, Image
import random
import shutil
import os

list = ["Камень", "Ножницы", "Бумага"]

def choice1():
  l.configure(image="")
  l2.configure(image="")
  l4.configure(text="")
  l3.configure(text="Камень, ножницы, бумага!")
  root.after(1500, count)

def choice2():
  l.configure(image="")
  l2.configure(image="")
  l4.configure(text="")
  l3.configure(text="Камень, ножницы, бумага!")
  root.after(1500, count2)
  
def choice3():
  l.configure(image="")
  l2.configure(image="")
  l4.configure(text="")
  l3.configure(text="Камень, ножницы, бумага!")
  root.after(1500, count3)
    
def count():
  l3.configure(text="Раз, два, три!")
  root.after(1500, _rock)

def count2():
  l3.configure(text="Раз, два, три!")
  root.after(1500, _scissors)  
  
def count3():
  l3.configure(text="Раз, два, три!")
  root.after(1500, _paper)
  
def _rock():
  answer = random.choice(list)
  l.configure(image=rock)
  l.grid(padx=2, pady=20)
  l4.configure(text="Выбери новый жест:")
  if answer == "Камень":
    l2.configure(image=rock2)
    l2.grid(padx=410, pady=20)
    l3.configure(text="Ничья!")
  if answer == "Ножницы":
    l2.configure(image=scissors2)
    l2.grid(padx=380, pady=15)
    l3.configure(text="Ты победил!")
  if answer == "Бумага":
    l2.configure(image=paper2)
    l2.grid(padx=380, pady=0)
    l3.configure(text="Ты проиграл!")
    
def _scissors():
  answer = random.choice(list)
  l.configure(image=scissors)
  l.grid(padx=10, pady=15)
  l4.configure(text="Выбери новый жест:")
  if answer == "Камень":
    l2.configure(image=rock2)
    l2.grid(padx=410, pady=20)
    l3.configure(text="Ты проиграл!")
  if answer == "Ножницы":
    l2.configure(image=scissors2)
    l2.grid(padx=380, pady=15)
    l3.configure(text="Ничья!")
  if answer == "Бумага":
    l2.configure(image=paper2)
    l2.grid(padx=380, pady=0)
    l3.configure(text="Ты победил!")

def _paper():
  answer = random.choice(list)
  l.configure(image=paper)
  l.grid(padx=10, pady=0)
  l4.configure(text="Выбери новый жест:")
  if answer == "Камень":
    l2.configure(image=rock2)
    l2.grid(padx=410, pady=20)
    l3.configure(text="Ты победил!")
  if answer == "Ножницы":
    l2.configure(image=scissors2)
    l2.grid(padx=380, pady=15)
    l3.configure(text="Ты проиграл!")
  if answer == "Бумага":
    l2.configure(image=paper2)
    l2.grid(padx=380, pady=0)
    l3.configure(text="Ничья!")
    
def how_to_use(): 
  answer = mb.showinfo(title="Справка", message="Инструкция", detail="1. Нажми на любой жест, чтобы\nначать игру.\n2. Выбранный жест отобразится\nв левой части окна.\n3. Используй кнопку «Выйти»,\nчтобы закрыть игру.")

def game_rules(): 
  answer = mb.showinfo(title="Справка", message="Правила игры:", detail="1. Камень разбивает ножницы.\n2. Ножницы режут бумагу.\n3. Бумага оборачивает камень.")
  
def exit():
  answer = mb.askyesno(title="Выход", message="Ты действительно хочешь\n         выйти из игры?")
  if answer == True:
    shutil.rmtree("Жесты")
    root.quit()
  else:
    pass	
    
def delete():
  shutil.rmtree("Жесты")
  root.destroy()

root = Tk()
root.title("Камень-ножницы-бумага!")
root.geometry("560x360")
root.resizable(width=False, height=False)

if not os.path.exists("Жесты"):
  shutil.unpack_archive("Жесты.zip", "Жесты")

menubar = Menu(root)
helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Справка", menu=helpmenu)
menubar.add_command(label="Выйти", command=exit)
helpmenu.add_command(label="Инструкция", command=how_to_use)
helpmenu.add_command(label="Правила игры", command=game_rules)
root.config(menu=menubar)

l = Label(root)
l.grid(row=0, column=0, sticky=NW, padx=10)
l2 = Label(root)
l2.grid(row=0, column=0, sticky=NW, padx=380)

l3 = Label(root, text="", font=('Arial', 14))
l3.grid(row=0, column=0, padx=10, pady=180, sticky=NW)

l4 = Label(root, text="Выбери свой жест:", font=('Arial', 14))
l4.grid(row=0, column=0, padx=10, pady=220, sticky=NW)

R = Button(root, width=10, height=2, text="Камень", font=('Arial', 14), command=lambda: choice1())
R.grid(row=0, column=0, sticky=NW, padx=20, pady=270)

S = Button(root, width=10, height=2, text="Ножницы", font=('Arial', 14), command=lambda: choice2())
S.grid(row=0, column=0, sticky=NW, padx=220, pady=270)

P = Button(root, width=10, height=2, text="Бумага", font=('Arial', 14), command=lambda: choice3())
P.grid(row=0, column=0, sticky=NW, padx=420, pady=270)

def resize_image(path, size):
  img = Image.open(path)
  img = img.resize(size, Image.LANCZOS)
  return ImageTk.PhotoImage(img)

rock = resize_image("Жесты/rock.png", (140, 100))
scissors = resize_image("Жесты/scissors.png", (150, 150))
paper = resize_image("Жесты/paper.png", (150, 150))
rock2 = resize_image("Жесты/rock2.png", (140, 100))
scissors2 = resize_image("Жесты/scissors2.png", (150, 150))
paper2 = resize_image("Жесты/paper2.png", (150, 150))

root.protocol("WM_DELETE_WINDOW", delete)
root.mainloop()
