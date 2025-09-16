import tkinter as tk
import random
import webbrowser

# CUSTOM SETTINGS:
BG_COLOR = "#7ec3c5"
LINK = "https://youtu.be/YpPfBaT-OAE"  # put your link here
QUESTION_TEXT = "Do you like the person who made this?"
LOADING_TEXT = "Loading your gift..."

def open_link_after_delay():
    webbrowser.open(LINK)

def open_link():
    question_label.config(text=LOADING_TEXT)
    window.after(5000, open_link_after_delay)

def move_no_button(event=None):
    window.update_idletasks()
    btn_w = no_button.winfo_width()
    btn_h = no_button.winfo_height()
    win_w = window.winfo_width()
    win_h = window.winfo_height()
    margin_x = 10
    margin_y_top = 150
    margin_y_bottom = 30
    x = random.randint(margin_x, win_w - btn_w - margin_x)
    y = random.randint(margin_y_top, win_h - btn_h - margin_y_bottom)
    no_button.place(x=x, y=y)

def block_no_click(event):
    return "break"

window = tk.Tk()
window.title("Important Question!")
window.geometry("600x400")
window.configure(bg=BG_COLOR)

question_label = tk.Label(
    window,
    text=QUESTION_TEXT,
    font=("Helvetica", 16, "bold"),
    bg=BG_COLOR,
    fg="white",
    wraplength=560,
    justify="center"
)
question_label.pack(pady=40)

yes_button = tk.Button(
    window,
    text="Yes!",
    font=("Helvetica", 14),
    bg="#4CAF50",
    fg="white",
    command=open_link,
    width=16
)
yes_button.pack(pady=10)

no_button = tk.Button(
    window,
    text="No, I hate you",
    font=("Helvetica", 14),
    bg="#C70039",
    fg="white",
    width=16
)
no_button.pack()
no_button.bind("<Enter>", move_no_button)
no_button.bind("<Button-1>", block_no_click)

window.mainloop()