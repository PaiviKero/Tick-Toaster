import customtkinter as ctk
from defs import *
import Table
from CTkTable import *

class RecorderWindow(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.times = {key: {} for key in TIME_TYPES}
        self.configure(fg_color=COLOR_BASE_SECONDARY)

        self.geometry(RECORDER_WINDOW_SIZE)
        self.title('Recorder Window')        
        self.tables_frame = ctk.CTkFrame(self, fg_color=COLOR_BASE_SECONDARY)
        self.tables_frame.grid()

    def addEntry(self, name, type, timeInMilliseconds, color):
        self.times[type][name] = {
            "time": timeInMilliseconds,
            "color": color
        }
    
    def draw(self):
        self.tables_frame.destroy()
        self.tables_frame = ctk.CTkFrame(self, fg_color=COLOR_BASE_SECONDARY)
        self.tables_frame.grid()
        row_counter = 0
        for key in self.times.keys():
            ctk.CTkLabel(self.tables_frame, text=key, font=('Arial',16)).grid(row=row_counter)
            row_counter += 1
            table_frame = ctk.CTkFrame(self.tables_frame, height=10, fg_color=COLOR_BASE_SECONDARY)
            table_frame.grid(row=row_counter)
            row_counter += 1
            Table.Table(table_frame, self.times[key])
