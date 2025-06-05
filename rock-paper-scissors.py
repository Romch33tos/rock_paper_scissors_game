import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
import random

#Списки для фукнций

list1 = [ 'Камень', 'Ножницы', 'Бумага']

list2 = ['Ура! Ты победил! :)', 'Ты выиграл! :D', 'Ура! Ты выиграл!', 'Эх! Я ещё выиграю!', 'В следующий раз, я выиграю!']

list3 = ['Ты проиграл! Не расстраивайся!', 'Ты проиграл! :(', 'В следующий раз, тебе повезёт!', 'Не расстраивайся! Давай сыграем ещё?']

list4 = ['Ничья!', 'Ого, а у нас ничья!', 'Ничья! Давай сыграем ещё!', 'Эх, ничья! Давай сыграем ещё!']

#Переменные для счётчика

w = 0
l = 0
d = 0
score = 10

def how_to_use(): 
	answer = mb.showinfo(title = "Справка", message = "Инструкция", detail = "1. Нажми на любой жест, чтобы\nначать!\n2. В окошках снизу отображается\nстатистка игры.\n3. Используй кнопку «Выйти»,\nчтобы закрыть игру.")

#Правила игры
def game_rules(): 
	answer = mb.showinfo(title = "Справка", message = "Правила игры", detail = "1. Камень разбивает ножницы.\n2. Ножницы режут бумагу.\n3. Бумага оборачивает камень.")
#Функция выхода

def exit():
    answer = mb.askyesno( title="Выход", message="Ты действительно хочешь\n         выйти из игры?")
    if answer == True:
        root.quit()
    else:
        pass

#Камень

def rock():
    global score 
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
        text.insert(END, "\n" + random.choice(list4))
        text.configure(state = DISABLED)
    if answer == 'Ножницы':      
        score += 10
        scr.set(str(score))
        global w
        w += 1
        txt.set(str(w))        
        text.insert(END, "\nМой выбор: " + str(answer))
        text.insert(END, "\n" + random.choice(list2))
        text.configure(state = DISABLED)
    if answer == 'Бумага':        
        score -= 10
        scr.set(str(score))       
        global l
        l += 1
        txt2.set(str(l))      
        text.insert(END, "\nМой выбор: " + str(answer))
        text.insert(END, "\n" + random.choice(list3))
        text.configure(state = DISABLED)
    if score < 0:
        R.configure(state = DISABLED)
        S.configure(state = DISABLED)
        P.configure(state = DISABLED)
        text.configure(state = NORMAL)
        text.delete("1.0", END)
        text.insert("1.0", "Игра окончена!")
        text.configure(state = DISABLED)
    if score == 100:
        R.configure(state = DISABLED)
        S.configure(state = DISABLED)
        P.configure(state = DISABLED)
        text.configure(state = NORMAL)
        text.delete("1.0", END)
        text.insert("1.0", "Ты победил!")
        text.configure(state = DISABLED)
            
#Ножницы
    
def scissors():
    global score 
    answer = random.choice(list1)
    text.configure(state = NORMAL)
    text.delete("1.0", END)  
    text.insert("1.0", "Камень, ножницы, бумага!")
    text.insert(END, "\nРаз, два, три!")
    text.insert(END, "\nТвой выбор: Ножницы")
    if answer == 'Камень':       
        score -= 10
        scr.set(str(score))
        global l
        l += 1 
        txt2.set(str(l))      
        text.insert(END, "\nМой выбор: " + str(answer))
        text.insert(END, "\n" + random.choice(list3))        
        text.configure(state = DISABLED)
    if answer == 'Ножницы':
        global d
        d +=1
        txt3.set(str(d))   
        text.insert(END, "\nМой выбор: " + str(answer))
        text.insert(END, "\n" + random.choice(list4))       
        text.configure(state = DISABLED)
    if answer == 'Бумага':        
        score += 10
        scr.set(str(score))
        global w
        w += 1
        txt.set(str(w))        
        text.insert(END, "\nМой выбор: " + str(answer))
        text.insert(END, "\n" + random.choice(list2))       
        text.configure(state = DISABLED) 
    if score < 0:
        R.configure(state = DISABLED)
        S.configure(state = DISABLED)
        P.configure(state = DISABLED)
        text.configure(state = NORMAL)
        text.delete("1.0", END)
        text.insert("1.0", "Игра окончена!")
        text.configure(state = DISABLED)
    if score == 100:
        R.configure(state = DISABLED)
        S.configure(state = DISABLED)
        P.configure(state = DISABLED)
        text.configure(state = NORMAL)
        text.delete("1.0", END)
        text.insert("1.0", "Ты победил!")
        text.configure(state = DISABLED)
                  
#Бумага
    
def paper():
    global score 
    answer = random.choice(list1)
    text.configure(state = NORMAL)
    text.delete("1.0", END)  
    text.insert("1.0", "Камень, ножницы, бумага!")
    text.insert(END, "\nРаз, два, три!")
    text.insert(END, "\nТвой выбор: Бумага")
    if answer == 'Камень':      
        score += 10
        scr.set(str(score))
        global w
        w += 1 
        txt.set(str(w))      
        text.insert(END, "\nМой выбор: " + str(answer))
        text.insert(END, "\n" + random.choice(list2))          
        text.configure(state = DISABLED)
    if answer == 'Ножницы':        
        score -= 10
        scr.set(str(score))
        global l
        l +=1
        txt2.set(str(l))   
        text.insert(END, "\nМой выбор: " + str(answer))
        text.insert(END, "\n" + random.choice(list3))             
        text.configure(state = DISABLED)
    if answer == 'Бумага':
        global d
        d += 1
        txt3.set(str(d))        
        text.insert(END, "\nМой выбор: " + str(answer))
        text.insert(END, "\n" + random.choice(list4))               
        text.configure(state = DISABLED)
    if score < 0:
        R.configure(state = DISABLED)
        S.configure(state = DISABLED)
        P.configure(state = DISABLED)
        text.configure(state = NORMAL)
        text.delete("1.0", END)
        text.insert("1.0", "Игра окончена!")
        text.configure(state = DISABLED)
    if score == 100:
        R.configure(state = DISABLED)
        S.configure(state = DISABLED)
        P.configure(state = DISABLED)
        text.configure(state = NORMAL)
        text.delete("1.0", END)
        text.insert("1.0", "Ты набрал 100 очков! Молодец!")
        text.configure(state = DISABLED)
        
#Окно

root = Tk()

menubar = Menu(root)

menubar = Menu(root)

helpmenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Справка", menu=helpmenu)

menubar.add_command(label = "Выйти", command = exit)

helpmenu.add_command(label="Инструкция", command=how_to_use)

helpmenu.add_command(label= "Правила игры", command=game_rules)

root.config(menu = menubar)

txt = StringVar()
txt2 = StringVar()
txt3 = StringVar()  
scr = StringVar()
#Текстовые надписи

l1 = Label(root, text = "Камень, ножницы, бумага!")
l1.grid(row = 0, column = 0, padx = 165, pady = 7, sticky = NW)

l2 = Label(root, text="Очки: ") 
l2.grid(row = 2, column = 0, sticky = NW, padx = 60, pady = 7)

l3 = Label(root, text="Количество побед: ") 
l3.grid(row = 3, column = 0, sticky = NW, padx = 60, pady = 7)

l4 = Label(root, text="Количество поражений:")
l4.grid(row = 4, column = 0, sticky = NW, padx = 60, pady = 7)

l5 = Label(root, text = "Количество ничьих: ")
l5.grid(row = 5, column = 0, padx = 60,  pady = 7, sticky = NW)

l6 = Label(root, text = "Выбери свой жест: ")
l6.grid(row = 6, column = 0, padx = 60,  pady = 7, sticky = NW)

#Текстовые поля

sc = Entry(root, width = 13, justify = CENTER, textvariable=scr)
sc.configure(disabledbackground="white", disabledforeground="black", state = DISABLED)
sc.grid(row = 2, column = 0, sticky = NW, padx = 415, pady = 7)
scr.set(str(score))       

win = Entry(root, width = 13, justify = CENTER, textvariable=txt)
win.configure(disabledbackground="white", disabledforeground="black", state = DISABLED)
win.grid(row = 3, column = 0, sticky = NW, padx = 415, pady = 7)

lose = Entry(root, width = 13, justify = CENTER, textvariable=txt2)
lose.configure(disabledbackground="white", disabledforeground="black", state = DISABLED)
lose.grid(row = 4, column = 0, sticky = NW, padx = 415, pady = 7)

draw = Entry(root, width = 13, justify = CENTER, textvariable=txt3)
draw.configure(disabledbackground="white", disabledforeground="black", state = DISABLED)
draw.grid(row = 5, column = 0, sticky = NW, padx = 415, pady = 7)

text = Text(width = 36, height = 5,wrap = WORD)
text.grid(row = 1, column = 0, padx = 60,pady = 5, sticky = NW)
text.insert("1.0", "Сыграем в камень-ножницы-бумагу?")
text.insert(END, "\nНажми на любой жест, чтобы начать!")

#Кнопки

R = Button(root, width = 7, text = "Камень", command = lambda: rock())
R.grid(row = 7, column = 0, sticky = NW, padx = 60, pady = 7)

S = Button(root, width = 7, text = "Ножницы", command = lambda: scissors())
S.grid(row = 7, column = 0, sticky = NW, padx = 256, pady = 7)

P = Button(root, width = 7, text = "Бумага", command = lambda: paper())
P.grid(row = 7, column = 0, sticky = NW, padx = 452, pady = 7)

root.mainloop()
