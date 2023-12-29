import customtkinter as ctk
from defs import *
import os 

class Settings:
    minutes_to_milliseconds = 60

    def __init__(self, parent):
        self.parent = parent
        self.init_ui()

    def set_times(self, green, yellow, red):
        self.green_start = green
        self.yellow_start = yellow
        self.red_start = red
        self.green_entry.delete(0, ctk.END)
        self.yellow_entry.delete(0, ctk.END)
        self.red_entry.delete(0, ctk.END)
        self.green_entry.insert(0, green)
        self.yellow_entry.insert(0, yellow)
        self.red_entry.insert(0, red)

    def get_whole_time(self):
        return self.get_red_start_time()+0.5*Settings.minutes_to_milliseconds

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
        return COLOR_BASE

    def reposition(self, x, y):
        self.button_frame.place(x=x, y=y)

    def select_time_option(self, selected_option):
        self.set_times(*SPEECH_OPTIONS[selected_option]["color_times"])

    def select_speaker_option(self, selected_option):
        self.speaker_entry.delete(0, ctk.END)
        self.speaker_entry.insert(0, selected_option)

    def clear_speaker(self):
        self.select_speaker_option("")
        self.clicked_speaker.set("Select speaker")

    def get_speech_type(self):
        return SPEECH_OPTIONS[self.clicked.get()]["type"]
    
    def get_speaker(self):
        return self.speaker_entry.get()
    
    def add_speaker(self):
        new_speaker = self.get_speaker()
        self.speakers.append(new_speaker)
        self.speaker_drop_options.configure(values=self.speakers)
        cwd = os.getcwd()
        with open(cwd+SPEAKER_FILE, "a", encoding='utf-8') as f:
            f.write('\n'+new_speaker)

    def get_height(self):
        return self.button_frame.winfo_height()

    def init_ui(self):
        self.button_frame = ctk.CTkFrame(self.parent, fg_color=COLOR_BASE_SECONDARY)
        self.button_frame.grid()
        ctk.CTkLabel(self.button_frame, text="Change to Green at (min): ").grid(row=2, padx=(10, 0))
        self.green_entry = ctk.CTkEntry(self.button_frame)
        self.green_entry.grid(row=2, column=2, padx=(5, 0), pady=(0, 6))
        ctk.CTkLabel(self.button_frame, text="Change to Yellow at (min): ").grid(row=3, padx=(10, 0))
        self.yellow_entry = ctk.CTkEntry(self.button_frame)
        self.yellow_entry.grid(row=3, column=2, padx=(5, 0), pady=(0, 6))
        ctk.CTkLabel(self.button_frame, text="Change to Red at (min): ").grid(row=4, padx=(10, 0))
        self.red_entry = ctk.CTkEntry(self.button_frame)
        self.red_entry.grid(row=4, column=2, padx=(5, 0), pady=(0, 6))

        ctk.CTkLabel(self.button_frame, text="Speaker: ").grid(row=1, padx=(10, 0))
        self.speaker_entry = ctk.CTkEntry(self.button_frame)
        self.speaker_entry.grid(row=1, column=2, padx=(5, 0), pady=(0, 6))

        ctk.CTkButton(self.button_frame, text="+", command=self.add_speaker, width=20).grid(row=1, column=3, padx=(5, 10), pady=(0, 6))

        self.clicked = ctk.StringVar()
        self.clicked.set(list(SPEECH_OPTIONS.keys())[1])
        self.select_time_option(self.clicked.get())
    
        drop_options = ctk.CTkOptionMenu(master=self.button_frame, variable=self.clicked, values=list(SPEECH_OPTIONS.keys()), command=self.select_time_option)
        drop_options.grid(column=0, row=0, padx=5, pady=5)

        cwd = os.getcwd()
        with open(cwd+SPEAKER_FILE, encoding='utf-8') as f:
            self.speakers = f.read().splitlines()

        self.clicked_speaker = ctk.StringVar()
        self.clicked_speaker.set("Select speaker")
    
        self.speaker_drop_options = ctk.CTkOptionMenu(master=self.button_frame, variable=self.clicked_speaker, values=self.speakers, command=self.select_speaker_option)
        self.speaker_drop_options.grid(column=2, row=0, padx=(5, 0), pady=5)


    def get_speech_length(self): 
        lower_limit = self.get_green_start_time()/Settings.minutes_to_milliseconds
        upper_limit = self.get_red_start_time()/Settings.minutes_to_milliseconds
        if(lower_limit.is_integer()):
            lower_limit = int(lower_limit)
        if(upper_limit.is_integer()):
            upper_limit = int(upper_limit)
        return str(lower_limit)+"-"+str(upper_limit)+" min"