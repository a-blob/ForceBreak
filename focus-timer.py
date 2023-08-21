import tkinter as tk
import time

focustime = 0
breaktime = 0

def break_window(breaktime):
    breakwindow = tk.Tk()
    breakwindow.attributes('-fullscreen', True)
    breakwindow.attributes('-topmost', True)
    breakwindow.title("It's time to take a break!")
    breakwindow['bg'] = '#FFFBE4'

    label = tk.Label(breakwindow, text = "It's time to take a break!", font = ("Times New Roman", 36), bg = '#FFFBE4')
    label.place(relx = 0.5, rely = 0.5, anchor = "center")

    breakwindow.after(breaktime, breakwindow.destroy)


def on_ok():
    focustime = (focusentry.get())
    breaktime = (breakentry.get())
    break_window(breaktime)
    input_window.destroy()
    

input_window = tk.Tk()

focus_label = tk.Label(input_window, text = "Focus time:")
focus_label.pack()
focusentry = tk.Entry(input_window)
focusentry.pack()

break_label = tk.Label(input_window, text = "Break time:")
break_label.pack()
breakentry = tk.Entry(input_window)
breakentry.pack()

ok_button = tk.Button(input_window, text = "Okay", command = on_ok)
ok_button.pack()

input_window.mainloop()

