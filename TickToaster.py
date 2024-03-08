import customtkinter as ctk
import Timer
import Settings
import ProgressBar
import RecorderWindow
from defs import *
from PIL import Image
import os

ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

class display(ctk.CTk):

    def __init__(self):
        ctk.CTk.__init__(self)
        self.title("Tick-Toaster")
        self.geometry(str(MAIN_WINDOW_WIDTH)+"x"+str(MAIN_WINDOW_HEIGHT)+"+"+str(MAIN_WINDOW_START_X)+"+"+str(MAIN_WINDOW_START_Y))

        self.color=COLOR_BASE
        # load and create background image
        try:
            current_path = os.path.dirname(os.path.realpath(__file__))
            self.image = Image.open(current_path + "/background.png");
            self.bg_image = ctk.CTkImage(self.image, size=self.calculate_background_image_size(MAIN_WINDOW_HEIGHT, self.image.size))
            self.bg_image_label = ctk.CTkLabel(self, text="", image=self.bg_image)
            self.bg_image_label.grid(row=0, column=0)
        except:
            self.bg_image = False
        
        #self.wm_attributes("-transparentcolor", "white")

        self.timer = Timer.Timer(self)
        self.settings = Settings.Settings(self)
        self.progress_bar = ProgressBar.ProgressBar(self)
        self.configure(fg_color=self.color)
        self.bind("<Configure>", self.reposition_ui)

        self.recorderWindow = RecorderWindow.RecorderWindow(self)

        self.save_button = ctk.CTkButton(self, text="Save", command=self.recorderWindow.save)
        self.save_button.grid(column=2, row=6, padx=5, pady=5)

    def calculate_background_image_size(self, height, original_size):
        new_height = height*BACKGROUND_IMAGE_SCALING_PERCENTAGE
        original_width, original_height = original_size
        new_width = original_width*(new_height/original_height)
        return (int(new_width), int(new_height))

    def record_time(self, time_as_string):
        self.recorderWindow.addEntry(self.settings.get_speaker(), self.settings.get_speech_type(), self.settings.get_speech_length(), time_as_string, self.color)
        self.recorderWindow.draw()
        self.settings.clear_speaker()

    def update_ui(self, count):
        color = self.settings.get_color(count)
        if (color != self.color):
            self.color = color
        progress_bar_color = color
        if (progress_bar_color == COLOR_BASE):
            progress_bar_color = COLOR_BLUE
        self.progress_bar.update_progress_bar(count, progress_bar_color)
        self.change_color(color)

    def change_color(self, color):
        self.configure(fg_color=color)
        self.timer.change_color(color)

    def reposition_ui(self, something):
        width = self.winfo_width()
        height = self.winfo_height()
        if(self.bg_image):
            self.bg_image = ctk.CTkImage(self.image, size=(self.calculate_background_image_size(height, self.image.size)))
            self.bg_image_label.configure(image=self.bg_image)
            self.bg_image_label.place(x=(width*1)/21, y=((height*1)/20+self.progress_bar.get_height()+10))
            timer_y_pos = (height*1)/20+self.progress_bar.get_height()+self.bg_image_label.winfo_height()
            #add another layer under so color is cool
            #self.bg_image_label.configure(bg_color="black")
        else:
            timer_y_pos = (height*2)/5+self.settings.get_height()/3

        self.progress_bar.reposition(x=(width*1)/21, y=(height*1)/20)
        self.timer.reposition_label(x=(width*1)/21+20, y=(timer_y_pos))
        self.timer.reposition_counter(x=self.progress_bar.get_width()-self.timer.get_counter_width(), y=(height*1)/20+self.progress_bar.get_height()+100)
        self.timer.reposition_button(x=(width*13)/23, y=(height*2)/5+self.settings.get_height()+10)
        self.settings.reposition(x=(width*6)/11, y=(height*2)/5)
        self.save_button.place(x=(width*13)/23+self.timer.get_button_width()+10, y=(height*2)/5+self.settings.get_height()+10)

    def reset_ui(self):
        self.progress_bar.set_max(self.settings.get_whole_time())
        self.progress_bar.update_progress_bar(0, COLOR_BLUE)
        self.change_color(COLOR_BASE)


if __name__ == "__main__":
    root = display()
    root.mainloop()
