from tkinter import *
from defs import *
 
class Table:
     
    def __init__(self, table_frame, content):
        # code for creating table
        rowCounter = 0
        for key in content.keys():
            self.createEntry(table_frame, rowCounter, 0, key, COLOR_BLACK)
            self.createEntry(table_frame, rowCounter, 1, content[key]["time"], content[key]["color"])
            rowCounter = rowCounter+1

    def createEntry(self, table_frame, row, column, content, color):
        self.e = Entry(table_frame, width=20, fg=color,
                    font=('Arial',16))
        
        self.e.grid(row=row, column=column)
        self.e.insert(END, content)