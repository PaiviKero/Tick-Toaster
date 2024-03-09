import customtkinter as ctk
import Timer
import ControlWindow
import ProgressBar
import RecorderWindow
from defs import *

ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

class display(ctk.CTk):

    def __init__(self):
        ctk.CTk.__init__(self)
        self.title("Tick-Toaster")
        self.geometry(str(MAIN_WINDOW_WIDTH)+"x"+str(MAIN_WINDOW_HEIGHT)+"+"+str(MAIN_WINDOW_START_X)+"+"+str(MAIN_WINDOW_START_Y))

        self.recorderWindow = RecorderWindow.RecorderWindow(self)
        self.controlWindow = ControlWindow.ControlWindow(self)
        
        self.timer = Timer.Timer(self)
        self.progress_bar = ProgressBar.ProgressBar(self)
        self.color=COLOR_BASE
        self.configure(fg_color=self.color)
        self.bind("<Configure>", self.reposition_ui)


    def record_time(self, time_as_string):
        self.recorderWindow.add_entry(self.controlWindow.get_speaker(), self.controlWindow.get_speech_type(), self.controlWindow.get_speech_length(), time_as_string, self.color)
        self.recorderWindow.draw()
        self.controlWindow.clear_speaker()

    def update_ui(self, count):
        color = self.controlWindow.get_color(count)
        if (color != self.color):
            self.color = color
            self.change_color(color)
        progress_bar_color = color
        if (progress_bar_color == COLOR_BASE):
            progress_bar_color = COLOR_BLUE
        self.progress_bar.update_progress_bar(count, progress_bar_color)

    def change_color(self, color):
        self.configure(fg_color=color)
        self.timer.change_color(color)

    def reposition_ui(self, something):
        width = self.winfo_width()
        height = self.winfo_height()
        self.progress_bar.reposition(x=(width*1)/21, y=(height*1)/20)
        self.timer.reposition_label(x=(width*1)/21+20, y=(height*2)/5+self.controlWindow.get_height()/3)
        self.timer.reposition_counter(x=(width*1)/21+20, y=(height*1)/20+self.progress_bar.get_height()+10)
        self.controlWindow.reposition(x=10, y=10)
        self.timer.reposition_button(x=10, y=self.controlWindow.get_height()+20)

    def reset_ui(self):
        self.progress_bar.set_max(self.controlWindow.get_whole_time())
        self.progress_bar.update_progress_bar(0, COLOR_BLUE)
        self.change_color(COLOR_BASE)


if __name__ == "__main__":
    root = display()
    root.mainloop()
