import customtkinter as ctk
from defs import *


class ProgressBar:
    def __init__(self, parent):
        self.count = 0
        self.parent = parent
        self.init_ui()

    def update_progress_bar(self, count, color):
        self.count = count
        self.progress_bar.configure(progress_color=color)
        self.progress_bar.set(self.count/self.whole_time_in_seconds)

    def set_max(self, whole_time_in_minutes):
        self.whole_time_in_seconds = whole_time_in_minutes

    def reposition(self, x, y):
        self.progress_bar.configure(width=self.parent.winfo_width()-self.parent.winfo_width()/15)
        self.progress_bar.place(x=x, y=y)

    def get_height(self):
        return self.progress_bar.winfo_height()
    
    def init_ui(self):
        self.progress_bar = ctk.CTkProgressBar(master=self.parent, height=70, border_width=10, border_color=COLOR_BASE_SECONDARY)
        self.progress_bar.configure(progress_color=COLOR_BLUE)
        self.progress_bar.grid(column=0, row=0, columnspan=2, padx=5, pady=5)
        return

    def update_ui():
        return
