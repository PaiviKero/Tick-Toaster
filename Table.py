import customtkinter as ctk
from defs import *

class Table:
     
    def __init__(self, table_frame, content, delete_entry, entry_type):
        # code for creating table
        rowCounter = 0
        for key in content.keys():
            self.create_entry(table_frame, rowCounter, 0, 220, key, COLOR_WHITE)
            self.create_entry(table_frame, rowCounter, 1, 80, content[key]["length"], COLOR_WHITE)
            self.create_entry(table_frame, rowCounter, 2, 80, content[key]["time"], content[key]["color"])
            self.add_delete_button(table_frame, rowCounter, 3, 20, lambda: delete_entry(entry_type, key))
            rowCounter = rowCounter+1

    def create_entry(self, table_frame, row, column, width, content, color):
        self.e = ctk.CTkEntry(master=table_frame, width=width, fg_color=color,
                    text_color=COLOR_BLACK, font=('Arial',16))
        
        self.e.grid(row=row, column=column, padx=(5,0), pady=(0,5))
        self.e.insert(ctk.END, content)
    
    def add_delete_button(self, table_frame, row, column, width, button_command):
        self.save_button = ctk.CTkButton(master=table_frame, width=width, text="x", command=button_command)
        self.save_button.grid(row=row, column=column, padx=(5,0), pady=(0,5))