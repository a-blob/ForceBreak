import tkinter as tk
from tkinter import ttk
import time


class ForceBreak:
    def __init__(self, focus_time, break_time, focus_window, focus_label):
        self.focus_time = int(focus_time.get())
        self.break_time = int(break_time.get())
        self.focus_window = focus_window
        self.focus_label = focus_label
        self.focus_timer()

    def break_timer(self):
        break_window = tk.Tk()
        break_window.attributes('-fullscreen', True)
        break_window.attributes('-topmost', True)
        break_window.title("")
        break_window['bg'] = '#FFFBE4'

        count_label = tk.Label(break_window, text="",
                               font=("Times New Roman", 20), bg='#FFFBE4')
        count_label.place(relx=0.5, rely=0.6, anchor="center")

        label = tk.Label(break_window, text="It's time to take a break!",
                         font=("Times New Roman", 36, "bold"), bg='#FFFBE4')
        label.place(relx=0.5, rely=0.5, anchor="center")

        break_count = self.break_time
        while break_count >= 0:
            count_label.config(text=str(break_count))
            break_window.update()
            time.sleep(1)
            break_count -= 1

        break_window.destroy()
        self.focus_timer()

    def focus_timer(self):
        focus_count = self.focus_time
        while focus_count >= 0:
            self.focus_label.config(text=str(focus_count) + " min. left")
            self.focus_window.update()
            time.sleep(1)
            focus_count -= 1
        self.break_timer()


def main():
    # Define the window
    input_window = tk.Tk()
    input_window.title("ForceBreak")
    input_window.resizable(width=False, height=False)
    input_window.geometry("650x300")
    input_window.wm_attributes('-alpha', 0.97)

    # Apply themes and colors
    style = ttk.Style()
    style.theme_use("clam")
    input_window.configure(background="#dcdad5")

    # Create input frame
    frame = ttk.Frame(input_window, relief="solid", borderwidth=2)
    frame.place(x=75, y=55)

    # Create counting frame
    count_frame = ttk.Frame(input_window, relief="solid", borderwidth=2, width=200, height=200)
    frame.pack_propagate(False)
    count_frame.place(x=450, y=125)

    frame.grid_rowconfigure(0, minsize=20)

    # Create label amd entry fields
    focus_label = ttk.Label(frame, text="Focus time:")
    focus_label.grid(row=1, column=0, padx=30, pady=0, sticky='w')

    focus_entry = ttk.Entry(frame)
    focus_entry.grid(row=2, column=0, padx=30, pady=0)

    frame.grid_rowconfigure(3, minsize=10)

    break_label = ttk.Label(frame, text="Break time:")
    break_label.grid(row=4, column=0, padx=30, pady=0, sticky='w')

    break_entry = ttk.Entry(frame)
    break_entry.grid(row=5, column=0, padx=30, pady=0)

    frame.grid_rowconfigure(6, minsize=20)

    # Create counting label
    count_label = ttk.Label(count_frame, text="")
    count_label.grid(row=0, column=0)

    # Create button
    ok_button = ttk.Button(frame, text="Start", command=lambda: ForceBreak(focus_entry, break_entry, input_window, count_label))
    ok_button.grid(row=7, column=0, padx=30, pady=0)

    frame.grid_rowconfigure(8, minsize=20)

    return input_window


main().mainloop()
