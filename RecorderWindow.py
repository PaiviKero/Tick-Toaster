import customtkinter as ctk
from defs import *
import Table
import pyscreenshot as ImageGrab
import os
import datetime
import csv
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import PatternFill
from openpyxl.cell import Cell
from matplotlib import colors

class RecorderWindow(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.times = {key: {} for key in TIME_TYPES}
        self.configure(fg_color=COLOR_BASE_SECONDARY)

        self.geometry(str(RECORDER_WINDOW_WIDTH)+"x"+str(RECORDER_WINDOW_HEIGHT)+"+"+str(RECORDER_WINDOW_START_X)+"+"+str(RECORDER_WINDOW_START_Y))
        self.title('Timer Log')        
        self.tables_frame = ctk.CTkFrame(self, fg_color=COLOR_BASE_SECONDARY)
        self.tables_frame.grid()

    def addEntry(self, name, type, speech_length, time_in_milliseconds, color):
        self.times[type][name] = {
            "length": speech_length,
            "time": time_in_milliseconds,
            "color": color
        }
    
    def draw(self):
        self.tables_frame.destroy()
        self.tables_frame = ctk.CTkFrame(self, fg_color=COLOR_BASE_SECONDARY)
        self.tables_frame.grid()
        row_counter = 0
        for key in self.times.keys():
            if(key in LOGGED_TIME_TYPES):
                ctk.CTkLabel(self.tables_frame, text=key, font=('Arial',16)).grid(row=row_counter)
                row_counter += 1
                table_frame = ctk.CTkFrame(self.tables_frame, height=10, fg_color=COLOR_BASE_SECONDARY)
                table_frame.grid(row=row_counter)
                row_counter += 1
                Table.Table(table_frame, self.times[key])

    def grab(self):
        return ImageGrab.grab(bbox=(self.winfo_x()+8, self.winfo_y(), self.winfo_width()+62,self.winfo_height()+80))

    def save(self):
        self.save_image()
        #self.save_csv()
        self.save_xlsx()

    def get_file_name(self):
        date_time_string = datetime.datetime.now().strftime("%B_%d_%Y_%I_%M%p")
        return 'Timer_Report_'+date_time_string

    def save_image(self):
        im = self.grab()
        file_name = self.get_file_name()+'.png'
        im.save(file_name)
        os.startfile(file_name)

    def get_speech_length(self, type):  
        speech_length = ""
        if(type == TIME_TYPES[1]):
            speech_length = str(SPEECH_OPTIONS[TIME_TYPES[1]]["color_times"][0])+"-"+str(SPEECH_OPTIONS[TIME_TYPES[1]]["color_times"][2])+" min"
        if(type == TIME_TYPES[2]):
            speech_length = str(SPEECH_OPTIONS[TIME_TYPES[2]]["color_times"][0])+"-"+str(SPEECH_OPTIONS[TIME_TYPES[2]]["color_times"][2])+" min"
        return speech_length

    def save_csv(self):
        file_name = self.get_file_name()+'.csv'
        with open(file_name, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            field = ["Type", "Speaker", "Length", "Time"]
            
            writer.writerow(field)
            for key in self.times.keys():
                writer.writerow([key, "", ""])
                content_row = self.times[key]
                for speaker in content_row:
                    writer.writerow(["", speaker, content_row[speaker]["length"], content_row[speaker]["time"]])
        os.startfile(file_name)
    
    def save_xlsx(self):
        wb = Workbook()
        worksheet = wb.active

        worksheet.append(["Type", "Speaker", "Length", "Time"]);
        for key in self.times.keys():
            worksheet.append([key, "", ""])
            content_row = self.times[key]
            for speaker in content_row:
                time_cell = Cell(worksheet, value=content_row[speaker]["time"])
                hex_color = colors.cnames[content_row[speaker]["color"].lower().replace(" ", "")].replace("#", "FF")
                time_cell.fill = PatternFill(start_color=hex_color, end_color=hex_color, fill_type = "solid")
                worksheet.append(["", speaker, content_row[speaker]["length"], time_cell])

        dims = {}
        for row in worksheet.rows:
            for cell in row:
                if cell.value:
                    dims[cell.column_letter] = max((dims.get(cell.column_letter, 0), len(str(cell.value))))  
        for col, value in dims.items():
            worksheet.column_dimensions[col].width = value

        file_name = self.get_file_name()+'.xlsx'
        wb.save(file_name)
        os.startfile(file_name)
    
