import calendar
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox  # Importing messagebox directly

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calendar App")
        
        self.selected_date = tk.StringVar()
        
        self.year_label = ttk.Label(root, text="Year:")
        self.year_label.grid(row=0, column=0)
        self.year_entry = ttk.Entry(root, width=10)
        self.year_entry.grid(row=0, column=1)
        
