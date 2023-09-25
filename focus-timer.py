import tkinter as tk
from tkinter import ttk
import time

focustime = 0
breaktime = 0
count = 0


def break_window(breaktime):
    breakwindow = tk.Tk()
    breakwindow.attributes('-fullscreen', True)
    breakwindow.attributes('-topmost', True)
    breakwindow.title("It's time to take a break!")
    breakwindow['bg'] = '#FFFBE4'

    label = tk.Label(breakwindow, text = "It's time to take a break!", font = ("Times New Roman", 36), bg = '#FFFBE4')
    label.place(relx = 0.5, rely = 0.5, anchor = "center")

    breakwindow.after(breaktime, lambda: on_close(breakwindow))

def on_close(window):
    window.destroy()
    on_ok(focusentry, breakentry, breaktime)


def on_ok(focusentry, breakentry, breaktime):
    focustime = (focusentry.get())
    breaktime = (breakentry.get())
    breaktime = int(breaktime)
    breaktime = breaktime * 60000
    focus_countdown(focustime, breaktime)


def focus_countdown(count, breaktime):
    count = int(count)
    print(count)
    if count > 0:
        count_label.config(text=str(count))
        inputwindow.after(60000, focus_countdown, count - 1, breaktime)
    else:
        break_window(breaktime)

inputwindow = tk.Tk()
inputwindow.resizable(width = False, height = False)
inputwindow.geometry("600x300")

style = ttk.Style()
style.theme_use("clam")
inputwindow.configure(background="#dcdad5")

focus_label = ttk.Label(inputwindow, text = "Focus time:")
focus_label.pack()
focusentry = ttk.Entry(inputwindow)
focusentry.pack()

break_label = ttk.Label(inputwindow, text = "Break time:")
break_label.pack()
breakentry = ttk.Entry(inputwindow)
breakentry.pack()

ok_button = ttk.Button(inputwindow, text = "Okay", command = lambda: on_ok(focusentry, breakentry, breaktime))
ok_button.pack()

count_label = ttk.Label(inputwindow, text = "")
count_label.pack()

inputwindow.mainloop()