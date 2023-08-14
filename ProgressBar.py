import tkinter as tk
from tkinter import ttk
from defs import *


class ProgressBar:
    def __init__(self, parent):
        self.count = 0
        self.parent = parent
        self.init_ui()

    def update_progress_bar(self, count, color):
        self.count = count
        if color == COLOR_GREEN:
            self.progress_bar.config(style='green.Horizontal.TProgressbar')
        if color == COLOR_YELLOW:
            self.progress_bar.config(style='yellow.Horizontal.TProgressbar')
        if color == COLOR_RED:
            self.progress_bar.config(style='red.Horizontal.TProgressbar')
        if color == COLOR_BLUE:
            self.progress_bar.config(style='blue.Horizontal.TProgressbar')
        self.progress_bar['value'] = self.count

    def set_max(self, whole_time_in_minutes):
        whole_time_in_seconds = whole_time_in_minutes
        self.progress_bar.config(maximum=whole_time_in_seconds)

    def reposition(self, x, y):
        self.bar_frame.place(x=x, y=y)

    def init_ui(self):
        self.bar_frame = tk.Frame(self.parent)
        self.bar_frame.grid()
        style = ttk.Style()
        style.theme_use('alt')
        style.configure("blue.Horizontal.TProgressbar",
                        background=COLOR_BLUE, thickness=50)
        style.configure("green.Horizontal.TProgressbar",
                        background=COLOR_GREEN, thickness=50)
        style.configure("yellow.Horizontal.TProgressbar",
                        background=COLOR_YELLOW, thickness=50)
        style.configure("red.Horizontal.TProgressbar",
                        background=COLOR_RED, thickness=50)
        self.progress_bar = ttk.Progressbar(self.bar_frame, orient="horizontal", length=800,
                                            mode="determinate")
        self.progress_bar.config(style='blue.Horizontal.TProgressbar')
        self.progress_bar.grid(column=0, row=0, columnspan=2, padx=5, pady=5)
        return

    def update_ui():
        return
