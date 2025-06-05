import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import random
import shutil
import os

GESTURES = ["Камень", "Ножницы", "Бумага"]

def reset_display():
    player_choice_label.configure(image="")
    computer_choice_label.configure(image="")
    prompt_label.configure(text="")
    status_label.configure(text="Камень, ножницы, бумага!")

def countdown_then_show(gesture_function):
    status_label.configure(text="Раз, два, три!")
    root.after(1500, gesture_function)

def prepare_gesture(gesture_function):
    reset_display()
    root.after(1500, lambda: countdown_then_show(gesture_function))

def show_result(player_gesture, player_image):
    computer_choice = random.choice(GESTURES)
    player_choice_label.configure(image=player_image)
    prompt_label.configure(text="Выбери новый жест:")

    if computer_choice == "Камень":
        computer_choice_label.configure(image=rock_img_computer)
        result = "Ничья!" if player_gesture == "Камень" else "Ты победил!" if player_gesture == "Бумага" else "Ты проиграл!"
    elif computer_choice == "Ножницы":
        computer_choice_label.configure(image=scissors_img_computer)
        result = "Ничья!" if player_gesture == "Ножницы" else "Ты победил!" if player_gesture == "Камень" else "Ты проиграл!"
    else:
        computer_choice_label.configure(image=paper_img_computer)
        result = "Ничья!" if player_gesture == "Бумага" else "Ты победил!" if player_gesture == "Ножницы" else "Ты проиграл!"

    status_label.configure(text=result)

def show_rock():
    show_result("Камень", rock_img_player)

def show_scissors():
    show_result("Ножницы", scissors_img_player)

def show_paper():
    show_result("Бумага", paper_img_player)

def show_instructions():
    messagebox.showinfo(
        title="Справка", 
        message="Инструкция", 
        detail="1. Нажми на любой жест, чтобы
начать игру.\n2. Выбранный жест отобразится
в левой части окна."
    )

def show_rules():
    messagebox.showinfo(
        title="Справка", 
        message="Правила игры:", 
        detail="1. Камень разбивает ножницы.\n2. Ножницы режут бумагу.\n3. Бумага оборачивает камень."
    )

def cleanup():
    if os.path.exists("Жесты"):
        shutil.rmtree("Жесты")
    root.destroy()

def resize_image(path, size):
    image = Image.open(path)
    image = image.resize(size, Image.LANCZOS)
    return ImageTk.PhotoImage(image)

root = tk.Tk()
root.title("Камень-ножницы-бумага!")
root.geometry("480x350")
root.resizable(width=False, height=False)

if not os.path.exists("Жесты"):
    shutil.unpack_archive("Жесты.zip", "Жесты")

menu_bar = tk.Menu(root)
help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Справка", menu=help_menu)
help_menu.add_command(label="Инструкция", command=show_instructions)
help_menu.add_command(label="Правила игры", command=show_rules)
root.config(menu=menu_bar)

gestures_frame = tk.Frame(root, height=150)
gestures_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=20)
gestures_frame.grid_propagate(False)

player_choice_label = tk.Label(gestures_frame)
player_choice_label.place(x=20, y=25)

computer_choice_label = tk.Label(gestures_frame)
computer_choice_label.place(x=320, y=25)

status_label = tk.Label(root, text="", font=('Arial', 14))
status_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

prompt_label = tk.Label(root, text="Выбери свой жест:", font=('Arial', 14))
prompt_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

buttons_frame = tk.Frame(root)
buttons_frame.grid(row=3, column=0, sticky="ew", pady=10)

rock_button = tk.Button(
    buttons_frame, 
    width=10, 
    height=2, 
    text="Камень", 
    font=('Arial', 14), 
    command=lambda: prepare_gesture(show_rock)
)
rock_button.pack(side="left", padx=20, expand=True)

scissors_button = tk.Button(
    buttons_frame, 
    width=10, 
    height=2, 
    text="Ножницы", 
    font=('Arial', 14), 
    command=lambda: prepare_gesture(show_scissors)
)
scissors_button.pack(side="left", padx=20, expand=True)

paper_button = tk.Button(
    buttons_frame, 
    width=10, 
    height=2, 
    text="Бумага", 
    font=('Arial', 14), 
    command=lambda: prepare_gesture(show_paper)
)
paper_button.pack(side="left", padx=20, expand=True)

rock_img_player = resize_image("Жесты/rock.png", (120, 100))
scissors_img_player = resize_image("Жесты/scissors.png", (120, 120))
paper_img_player = resize_image("Жесты/paper.png", (120, 120))
rock_img_computer = resize_image("Жесты/rock2.png", (120, 100))
scissors_img_computer = resize_image("Жесты/scissors2.png", (120, 120))
paper_img_computer = resize_image("Жесты/paper2.png", (120, 120))

root.protocol("WM_DELETE_WINDOW", cleanup)
root.mainloop()
