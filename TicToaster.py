import tkinter as tk
import Timer
import Settings
import ProgressBar
from defs import *


class display(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Tic-Toaster")
        self.geometry('900x500')
        self.timer = Timer.Timer(self)
        self.settings = Settings.Settings(self)
        self.progress_bar = ProgressBar.ProgressBar(self)
        self.color = COLOR_WHITE
        self.bind("<Configure>", self.reposition_ui)

    def update_ui(self, count):
        color = self.settings.get_color(count)
        if (color != self.color):
            self.color = color
        self.progress_bar.update_progress_bar(count, color)
        self.change_color(color)

    def change_color(self, color):
        self['bg'] = color
        self.timer.change_color(color)

    def reposition_ui(self, something):
        width = self.winfo_width()
        height = self.winfo_height()
        self.progress_bar.reposition(x=(width*1)/20, y=(height*1)/20)
        self.timer.reposition_label(x=(width*1)/20, y=(height*2)/5)
        self.timer.reposition_counter(x=(width*1)/20, y=(height*2)/10)
        self.timer.reposition_button(x=(width*13)/20, y=(height*13)/20)
        self.settings.reposition(x=(width*6)/10, y=(height*2)/5)

    def reset_ui(self):
        self.progress_bar.set_max(self.settings.get_whole_time())
        self.progress_bar.update_progress_bar(0, COLOR_BLUE)
        self.change_color(COLOR_WHITE)


if __name__ == "__main__":
    root = display()
    root.mainloop()
