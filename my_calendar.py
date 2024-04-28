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
        
        self.month_label = ttk.Label(root, text="Month:")
        self.month_label.grid(row=0, column=2)
        self.month_entry = ttk.Entry(root, width=10)
        self.month_entry.grid(row=0, column=3)
        
        self.show_button = ttk.Button(root, text="Show Calendar", command=self.show_calendar)
        self.show_button.grid(row=0, column=4)
        
        self.calendar_label = ttk.Label(root, text="Calendar", font=('Helvetica', 16))
        self.calendar_label.grid(row=1, column=0, columnspan=5)
        
        self.calendar = ttk.Treeview(root, columns=("Date", "Day"))
        self.calendar.heading("Date", text="Date")
        self.calendar.heading("Day", text="Day")
        self.calendar.grid(row=2, column=0, columnspan=5)
    
    def show_calendar(self):
        year_str = self.year_entry.get()
        month_str = self.month_entry.get()
        
        if not year_str.isdigit() or not month_str.isdigit():
            messagebox.showerror("Error", "Please enter valid year and month.")
            return
        
        year = int(year_str)
        month = int(month_str)
        
        if month < 1 or month > 12:
            messagebox.showerror("Error", "Please enter a valid month (1-12).")
            return
        
        self.calendar.delete(*self.calendar.get_children())
        
        cal_data = calendar.monthcalendar(year, month)
        
        for week in cal_data:
            if week[0] != 0:
                self.calendar.insert("", "end", values=(week[0], calendar.day_name[calendar.weekday(year, month, week[0])]))
            if week[1] != 0:
                self.calendar.insert("", "end", values=(week[1], calendar.day_name[calendar.weekday(year, month, week[1])]))
            if week[2] != 0:
                self.calendar.insert("", "end", values=(week[2], calendar.day_name[calendar.weekday(year, month, week[2])]))
            if week[3] != 0:
                self.calendar.insert("", "end", values=(week[3], calendar.day_name[calendar.weekday(year, month, week[3])]))
            if week[4] != 0:
                self.calendar.insert("", "end", values=(week[4], calendar.day_name[calendar.weekday(year, month, week[4])]))
            if week[5] != 0:
                self.calendar.insert("", "end", values=(week[5], calendar.day_name[calendar.weekday(year, month, week[5])]))
            if week[6] != 0:
                self.calendar.insert("", "end", values=(week[6], calendar.day_name[calendar.weekday(year, month, week[6])]))

def main():
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
