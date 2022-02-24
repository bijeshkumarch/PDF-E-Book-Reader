from mimetypes import init
from tkinter import *
from threading import Thread
from time import sleep
from multiprocessing import Process

import tkinter.filedialog as filedialog
import tkinter as tk

from matplotlib.pyplot import cla


class GUI():
    variable = None

    def __init__(self) -> None:

        master = Tk()

        # Give a title to your app
        master.title("E-Book Reader")
        top_frame = tk.Frame(master)
        bottom_frame = tk.Frame(master)
        line = tk.Frame(master, height=1, width=400,
                        bg="grey80", relief='groove')

        input_path = tk.Label(top_frame, text="Select PDF file:")
        input_entry = tk.Entry(top_frame, text="", width=40)
        browse1 = tk.Button(top_frame, text="Browse", command=self.input)

        # Select language menu
        OPTIONS = [
            "Hindi",
            "English",
            "Gujrati",
            "Malyalam",
            "Marathi",
            "Odia",
            "Punjabi",
            "Tamil",
            "Telugu",
            "Urdu"
        ]

        self.variable = StringVar(bottom_frame)
        self.variable.set(OPTIONS[0])  # default value

        MenuLabel = tk.Label(bottom_frame, text="Select Language to convert:")
        w = OptionMenu(bottom_frame, self.variable, *OPTIONS)
        MenuOk = Button(bottom_frame, text="Play", command=self.ok)

        top_frame.pack(side=tk.TOP)
        line.pack(pady=10)
        bottom_frame.pack(side=tk.BOTTOM, pady=20)

        input_path.grid(row=0, column=1, pady=2)
        input_entry.grid(row=1, column=1, pady=2)
        browse1.grid(row=1, column=2, pady=2)

        MenuLabel.grid(row=2, column=1, pady=2)
        w.grid(row=2, column=2, pady=2)
        MenuOk.grid(row=2, column=3, pady=2)

        master.mainloop()

    def input(self):
        input_path = tk.filedialog.askopenfilename()
        # input_entry.delete(1, tk.END)  # Remove current text in entry
        # input_entry.insert(0, input_path)  # Insert the 'path'

    def output(self):
        path = tk.filedialog.askopenfilename()
        # input_entry.delete(1, tk.END)  # Remove current text in entry
        # input_entry.insert(0, path)  # Insert the 'path'

    def ok(self):
        print("value is:" + self.variable.get())


if __name__ == "__main__":

    GUI()

    print("E-Book reader stopped.")
