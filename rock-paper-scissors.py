import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
import random

#Списки для фукнций

list1 = [ 'Камень', 'Ножницы', 'Бумага']

list2 = ['Ты заработал 10 очков!', '+ 10 очков к твоему счёту!', '10 очков твои! Ура :D', 'Молодец! + 10 очков к твоему счёту!']

list3 = ['-10 очков от твоего счёта!', 'Жаль, но ты потерял 10 очков!', '-10 очков! Не расстраивайся!']

list4 = ['Ничья!', 'Ого, а у нас ничья!', 'Ничья! Давай сыграем ещё!', 'Эх, ничья! Давай сыграем ещё!']

list5 = ['Ура! Ты победил! :)', 'Ты выиграл! :D', 'Ура! Ты выиграл!', 'Молодец, ты набрал 100 очков!\nПобеда!']

list6 = ['Ты проиграл! Не расстраивайся!', 'Ты проиграл! :(', 'В следующий раз, тебе повезёт!', 'Не расстраивайся! Давай сыграем ещё?']

list7 = ['Играем! Выбери жест!', 'Начнем! Выбери жест!', 'Давай заново! Выбирай жест!']

#Переменные для счётчика

score = 20

#Инструкция

def how_to_use(): 
	answer = mb.showinfo(title = "Справка", message = "Инструкция", detail = "1. Нажми на любой жест, чтобы\nначать!\n2. Используй кнопку «Выйти»,\nчтобы закрыть игру.")
	
def restart():
    answer = mb.askyesno(title = "Новая игра", message = "Ты действительно хочешь\n     начать новую игру?")
    if answer == True:
        global score
        score = 10    
        scr.set(str(score))
        text.configure(state = NORMAL)        
        text.delete("1.0", END)
        text.insert("1.0", random.choice(list7))
        text.configure(state = DISABLED)
        R.configure(state = NORMAL)
        S.configure(state = NORMAL)
        P.configure(state = NORMAL)
       
#Правила игры

def game_rules(): 
	answer = mb.showinfo(title = "Справка", message = "Правила игры", detail = "1. Камень разбивает ножницы.\n2. Ножницы режут бумагу.\n3. Бумага оборачивает камень.\n4. За победу даётся + 10 очков,\nза поражение - 10 очков.\n5. Чтобы победить в игре, нужно\nнабрать 100 очков.\n6. Если число очков < 0, то игроку\nприсуждается поражение!")
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
        text.insert(END, "\nМой выбор: " + str(answer))
        text.insert(END, "\n" + random.choice(list4))
        text.configure(state = DISABLED)
        
    if answer == 'Ножницы':       
        score += 10
        scr.set(str(score))       
        text.insert(END, "\nМой выбор: " + str(answer))
        text.insert(END, "\n" + random.choice(list2))
        text.configure(state = DISABLED)
        
    if answer == 'Бумага':        
        score -= 10
        scr.set(str(score))       
        text.insert(END, "\nМой выбор: " + str(answer))
        text.insert(END, "\n" + random.choice(list3))
        text.configure(state = DISABLED)
        
    if score < 0:
        R.configure(state = DISABLED)
        S.configure(state = DISABLED)
        P.configure(state = DISABLED)
        text.configure(state = NORMAL)
        text.delete("1.0", END)
        text.insert("1.0", random.choice(list6))
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
        text.insert(END, "\nМой выбор: " + str(answer))
        text.insert(END, "\n" + random.choice(list3))        
        text.configure(state = DISABLED)
        
    if answer == 'Ножницы':   
        text.insert(END, "\nМой выбор: " + str(answer))
        text.insert(END, "\n" + random.choice(list4))       
        text.configure(state = DISABLED)
        
    if answer == 'Бумага':   
        score += 10
        scr.set(str(score))
        text.insert(END, "\nМой выбор: " + str(answer))
        text.insert(END, "\n" + random.choice(list2))       
        text.configure(state = DISABLED)
         
    if score < 0:
        R.configure(state = DISABLED)
        S.configure(state = DISABLED)
        P.configure(state = DISABLED)
        text.configure(state = NORMAL)
        text.delete("1.0", END)
        text.insert("1.0", random.choice(list6))
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
        text.insert(END, "\nМой выбор: " + str(answer))
        text.insert(END, "\n" + random.choice(list2))          
        text.configure(state = DISABLED)
        
    if answer == 'Ножницы': 
        score -= 10
        scr.set(str(score))        
        text.insert(END, "\nМой выбор: " + str(answer))
        text.insert(END, "\n" + random.choice(list3))             
        text.configure(state = DISABLED)
        
    if answer == 'Бумага':     
        text.insert(END, "\nМой выбор: " + str(answer))
        text.insert(END, "\n" + random.choice(list4))               
        text.configure(state = DISABLED)
        
    if score < 0:
        R.configure(state = DISABLED)
        S.configure(state = DISABLED)
        P.configure(state = DISABLED)
        text.configure(state = NORMAL)
        text.delete("1.0", END)
        text.insert("1.0", random.choice(list6))
        text.configure(state = DISABLED)
        
    if score == 100:
        R.configure(state = DISABLED)
        S.configure(state = DISABLED)
        P.configure(state = DISABLED)
        text.configure(state = NORMAL)
        text.delete("1.0", END)
        text.insert("1.0", random.choice(list5))
        text.configure(state = DISABLED)
        
#Окно

root = Tk()

menubar = Menu(root)

menubar = Menu(root)

helpmenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Справка", menu=helpmenu)

menubar.add_command(label = "Новая игра", command = restart)

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

l6 = Label(root, text = "Выбери свой жест: ")
l6.grid(row = 6, column = 0, padx = 60,  pady = 7, sticky = NW)

#Текстовые поля

sc = Entry(root, width = 13, justify = CENTER, textvariable=scr)
sc.configure(disabledbackground="white", disabledforeground="black", state = DISABLED)
sc.grid(row = 2, column = 0, sticky = NW, padx = 415, pady = 7)
scr.set(str(score))       

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
