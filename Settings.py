import tkinter as tk
from tkinter import *
from defs import *


class Settings:
    minutes_to_milliseconds = 60

    def __init__(self, parent):
        self.parent = parent
        self.init_ui()

    def set_times(self, green, yellow, red):
        self.green_start = green
        self.yellow_start = yellow
        self.red_start = red
        self.green_entry.delete(0, END)
        self.yellow_entry.delete(0, END)
        self.red_entry.delete(0, END)
        self.green_entry.insert(0, green)
        self.yellow_entry.insert(0, yellow)
        self.red_entry.insert(0, red)

    def get_whole_time(self):
        return self.get_red_start_time()

    def get_green_start_time(self):
        return int(float(self.green_entry.get())*Settings.minutes_to_milliseconds)

    def get_red_start_time(self):
        return int(float(self.red_entry.get())*Settings.minutes_to_milliseconds)

    def get_yellow_start_time(self):
        return int(float(self.yellow_entry.get())*Settings.minutes_to_milliseconds)

    def get_color(self, count):
        if count >= self.get_red_start_time():
            return COLOR_RED
        if count >= self.get_yellow_start_time():
            return COLOR_YELLOW
        if count >= self.get_green_start_time():
            return COLOR_GREEN
        return COLOR_WHITE

    def reposition(self, x, y):
        self.button_frame.place(x=x, y=y)

    def init_ui(self):
        self.button_frame = tk.Frame(self.parent)
        self.button_frame.grid()
        tk.Label(self.button_frame, text="Change to Green at (min): ").grid(
            row=2, columnspan=2)
        self.green_entry = tk.Entry(self.button_frame)
        self.green_entry.grid(row=2, column=2)
        self.green_entry.insert(0, "0.05")
        tk.Label(self.button_frame, text="Change to Yellow at (min): ").grid(
            row=3, columnspan=2)
        self.yellow_entry = tk.Entry(self.button_frame)
        self.yellow_entry.grid(row=3, column=2)
        self.yellow_entry.insert(0, "0.1")
        tk.Label(self.button_frame, text="Change to Red at (min): ").grid(
            row=4, columnspan=2)
        self.red_entry = tk.Entry(self.button_frame)
        self.red_entry.grid(row=4, column=2)
        self.red_entry.insert(0, "0.15")

        speech_button = tk.Button(self.button_frame, text="5, 6, 7",
                                  command=lambda: self.set_times(5, 6, 7))
        speech_button.grid(column=0, row=0, padx=5, pady=5)

        evaluation_button = tk.Button(
            self.button_frame, text="2, 2.5, 3", command=lambda: self.set_times(2, 2.5, 3))
        evaluation_button.grid(column=1, row=0, padx=5, pady=5)

        tabletopics_button = tk.Button(
            self.button_frame, text="1, 1.5, 2", command=lambda: self.set_times(1, 1.5, 2))
        tabletopics_button.grid(column=2, row=0, padx=5, pady=5)

        # test_button = tk.Button(
        #    self.button_frame, text="0.05, 0.1, 0.15", command=lambda: self.set_times(0.05, 0.10, 0.15))
        # test_button.grid(column=3, row=0, padx=5, pady=5)
