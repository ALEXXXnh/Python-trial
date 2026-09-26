import tkinter as tk
from datetime import datetime

window = tk.Tk()
window.title("My Simple Page")
window.geometry("500x560")
window.minsize(400, 500)

font_size = 22
click_count = 0
dark_theme = True

# Header and live date/time
title_label = tk.Label(window, text="Welcome!", font=("Arial", 24, "bold"))
date_label = tk.Label(window, font=("Arial", 12))
clock_label = tk.Label(window, font=("Arial", 16))

# Name input and character counter
name_label = tk.Label(window, text="What's your name?", font=("Arial", 12))
name_entry = tk.Entry(window, font=("Arial", 14), justify="center")
count_label = tk.Label(window, text="Characters: 0", font=("Arial", 10))

# Greeting
greeting_label = tk.Label(
    window, text="Hello!", font=("Arial", font_size, "bold"), pady=10
)

window.mainloop()