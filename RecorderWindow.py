import tkinter as tk
from defs import *
import Table

class RecorderWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.times = {key: {} for key in TIME_TYPES}

        self.geometry('500x400')
        self.title('Recorder Window')        
        self.tables_frame = tk.Frame(self)
        self.tables_frame.grid()

    def addEntry(self, name, type, timeInMilliseconds, color):
        self.times[type][name] = {
            "time": timeInMilliseconds,
            "color": color
        }
    
    def draw(self):
        self.tables_frame.destroy()
        self.tables_frame = tk.Frame(self)
        self.tables_frame.grid()
        row_counter = 0
        for key in self.times.keys():
            tk.Label(self.tables_frame, text=key, font=('Arial',16)).grid(row=row_counter)
            row_counter += 1
            table_frame = tk.Frame(self.tables_frame)
            table_frame.grid(row=row_counter)
            row_counter += 1
            Table.Table(table_frame, self.times[key])
