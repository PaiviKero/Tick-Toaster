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

    def select_time_option(self, selected_option):
        self.set_times(*SPEECH_OPTIONS[selected_option]["color_times"])

    def get_speech_type(self):
        return SPEECH_OPTIONS[self.clicked.get()]["type"]
    
    def get_speaker(self):
        return self.speaker_entry.get()

    def init_ui(self):
        self.button_frame = tk.Frame(self.parent)
        self.button_frame.grid()
        tk.Label(self.button_frame, text="Change to Green at (min): ").grid(row=2)
        self.green_entry = tk.Entry(self.button_frame)
        self.green_entry.grid(row=2, column=2)
        tk.Label(self.button_frame, text="Change to Yellow at (min): ").grid(row=3)
        self.yellow_entry = tk.Entry(self.button_frame)
        self.yellow_entry.grid(row=3, column=2)
        tk.Label(self.button_frame, text="Change to Red at (min): ").grid(row=4)
        self.red_entry = tk.Entry(self.button_frame)
        self.red_entry.grid(row=4, column=2)

        tk.Label(self.button_frame, text="Speaker: ").grid(row=1)
        self.speaker_entry = tk.Entry(self.button_frame)
        self.speaker_entry.grid(row=1, column=2)

        self.clicked = StringVar()
        self.clicked.set(list(SPEECH_OPTIONS.keys())[1])
        self.select_time_option(self.clicked.get())
    
        drop_options = OptionMenu( self.button_frame, self.clicked, *SPEECH_OPTIONS.keys(), command=self.select_time_option)
        drop_options.grid(column=0, row=0, padx=5, pady=5)


