import tkinter as tk
import time
from defs import *


class Timer:
    def __init__(self, parent):
        self.seconds = 0
        self.minutes = 0
        self.parent = parent
        self.interrupt = False
        self.init_ui()

    def tick(self):
        current_timestamp = time.time()
        time_passed_since_last_tick = current_timestamp - \
            self.start_timestamp - self.minutes*60 - self.seconds
        if (time_passed_since_last_tick > 1):
            self.seconds += 1
            if (self.seconds > 60):
                self.seconds = 0
                self.minutes += 1
            self.update_ui()
        if (self.interrupt):
            return
        self.parent.after(1, self.tick)

    def start(self):
        self.start_timestamp = time.time()
        self.start_button.configure(text='Stop', command=self.stop)
        self.parent.reset_ui()
        self.time_label['text'] = "00:00"
        self.seconds = 0
        self.minutes = 0
        self.interrupt = False
        self.parent.after(1, self.tick)

    def stop(self):
        self.interrupt = True
        self.copy_time()
        self.start_button.configure(text='Start!', command=self.start)

    def update_ui(self):
        seconds_passed = self.minutes*60+self.seconds
        self.parent.update_ui(seconds_passed)
        self.update_time()

    def update_time(self):
        if (self.seconds < 10):
            seconds_str = "0" + str(self.seconds)
        else:
            seconds_str = str(self.seconds)
        if (self.minutes < 10):
            minutes_str = "0" + str(self.minutes)
        else:
            minutes_str = str(self.minutes)
        self.time_label['text'] = minutes_str + ":" + seconds_str

    def copy_time(self):
        # copy time to clipboard
        return

    def reposition_label(self, x, y):
        self.label.place(x=x, y=y)

    def reposition_counter(self, x, y):
        self.time_label.place(x=x, y=y)

    def reposition_button(self, x, y):
        self.start_button.place(x=x, y=y)

    def change_color(self, color):
        self.label['bg'] = color

    def init_ui(self):
        self.label = tk.Label(
            self.parent, text="Timer", font=("Arial", 75))
        self.label.grid(column=0, row=1, padx=5, pady=5)
        self.time_label = tk.Label(
            self.parent, text="00:00", font=("Arial", 25))
        self.time_label.grid(column=0, row=0, padx=5, pady=5)

        self.start_button = tk.Button(
            self.parent, text="Start!", command=self.start)
        self.start_button.grid(column=1, row=6, padx=5, pady=5)
