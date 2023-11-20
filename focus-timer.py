# Import
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import time


# Define the variables
focustime = 0
breaktime = 0
count = 0


# Define the functions
def break_window(breaktime):
    breakwindow = tk.Tk()
    breakwindow.attributes('-fullscreen', True)
    breakwindow.attributes('-topmost', True)
    breakwindow.title("It's time to take a break!")
    breakwindow['bg'] = '#FFFBE4'

    count_label = tk.Label(breakwindow, text = "",
                     font = ("Times New Roman", 20), bg = '#FFFBE4')
    count_label.place(relx = 0.5, rely = 0.6, anchor = "center")

    label = tk.Label(breakwindow, text = "It's time to take a break!",
                     font = ("Times New Roman", 36, "bold"), bg = '#FFFBE4')
    label.place(relx = 0.5, rely = 0.5, anchor = "center")

    def break_countdown(count):
        print(count)
        if count > 0:
            count_label.config(text = str(count) + " minutes left")
            breakwindow.after(60000, break_countdown, count - 1)
        else:
            on_close(breakwindow)

    break_countdown(breaktime)

def on_close(window):
    window.destroy()
    on_ok(focusentry, breakentry, breaktime)


def on_ok(focusentry, breakentry, breaktime):
    focustime = (focusentry.get())
    breaktime = (breakentry.get())
    breaktime = int(breaktime)
    #breaktime = breaktime * 60000
    focus_countdown(focustime, breaktime)


def focus_countdown(count, breaktime):
    count = int(count)
    print(count)
    if count > 0:
        count_label.config(text = str(count) + " min. left")
        inputwindow.after(60000, focus_countdown, count - 1, breaktime)
    else:
        break_window(breaktime)


# Main window code
inputwindow = tk.Tk()
inputwindow.title("ForceBreak")
inputwindow.resizable(width = False, height = False)
inputwindow.geometry("650x300")
inputwindow.wm_attributes('-alpha', 0.97)

style = ttk.Style()
style.theme_use("clam")
inputwindow.configure(background="#dcdad5")

# Create a Frame
frame = ttk.Frame(inputwindow, relief="solid", borderwidth=2)
frame.place(x=75, y=55)

count_frame = ttk.Frame(inputwindow, relief="solid", borderwidth=2, width=200, height=200)
frame.pack_propagate(0)
count_frame.place(x=450, y=125)

frame.grid_rowconfigure(0, minsize=20)

focus_label = ttk.Label(frame, text = "Focus time:")
focus_label.grid(row=1, column=0, padx=30, pady=0, sticky='w')

focusentry = ttk.Entry(frame)
focusentry.grid(row=2, column=0, padx=30, pady=0)

frame.grid_rowconfigure(3, minsize=10)

break_label = ttk.Label(frame, text = "Break time:")
break_label.grid(row=4, column=0, padx=30, pady=0, sticky='w')

breakentry = ttk.Entry(frame)
breakentry.grid(row=5, column=0, padx=30, pady=0)

frame.grid_rowconfigure(6, minsize=20)

ok_button = ttk.Button(frame, text = "Start", command = lambda: on_ok(focusentry, breakentry, breaktime))
ok_button.grid(row=7, column=0, padx=30, pady=0)

frame.grid_rowconfigure(8, minsize=20)

img = Image.open("./temp.png")
photo = ImageTk.PhotoImage(img)
tk.Label(count_frame, image=photo).grid(row=0, column=0)

count_label = ttk.Label(count_frame, text = "")
count_label.grid(row=0, column=0)

inputwindow.mainloop()
