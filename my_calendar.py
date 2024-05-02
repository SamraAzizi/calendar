import calendar
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calendar App")
        
        # Display today's year and month as default
        self.current_year = datetime.datetime.now().year
        self.current_month = datetime.datetime.now().month
        
        self.year_label = ttk.Label(root, text="Year:")
        self.year_label.grid(row=0, column=0)
        self.year_entry = ttk.Entry(root, width=10)
        self.year_entry.grid(row=0, column=1)
        self.year_entry.insert(0, str(self.current_year))
        
        self.month_label = ttk.Label(root, text="Month:")
        self.month_label.grid(row=0, column=2)
        self.month_entry = ttk.Entry(root, width=10)
        self.month_entry.grid(row=0, column=3)
        self.month_entry.insert(0, str(self.current_month))
        
        self.show_button = ttk.Button(root, text="Show Calendar", command=self.show_calendar)
        self.show_button.grid(row=0, column=4)
        
        self.calendar_label = ttk.Label(root, text="", font=('Helvetica', 16), justify=tk.LEFT)
        self.calendar_label.grid(row=1, column=0, columnspan=5, sticky="w")
        
        # Buttons to navigate between months
        self.prev_button = ttk.Button(root, text="<< Previous", command=self.show_previous_month)
        self.prev_button.grid(row=2, column=1)
        self.next_button = ttk.Button(root, text="Next >>", command=self.show_next_month)
        self.next_button.grid(row=2, column=3)

        # Show current month calendar on start
        self.show_calendar()

    def show_calendar(self):
        try:
            year = int(self.year_entry.get())
            month = int(self.month_entry.get())
            if 1 <= month <= 12:
                cal = calendar.month(year, month)
                self.calendar_label.config(text=cal)
            else:
                messagebox.showerror("Error", "Month must be between 1 and 12")
