import customtkinter as ctk
from defs import *

class Table:
     
    def __init__(self, table_frame, content):
        # code for creating table
        rowCounter = 0
        for key in content.keys():
            self.createEntry(table_frame, rowCounter, 0, 300, key, COLOR_WHITE)
            self.createEntry(table_frame, rowCounter, 1, 80, content[key]["time"], content[key]["color"])
            rowCounter = rowCounter+1

    def createEntry(self, table_frame, row, column, width, content, color):
        self.e = ctk.CTkEntry(master=table_frame, width=width, fg_color=color,
                    text_color=COLOR_BLACK, font=('Arial',16))
        
        self.e.grid(row=row, column=column)
        self.e.insert(ctk.END, content)