import tkinter as tk
from tkinter import messagebox
import threading
import time

class BreakReminderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Break Reminder")

        self.label = tk.Label(root, text="Enter time (hours, minutes, or seconds):")
        self.label.pack()

        self.time_entry = tk.Entry(root)
        self.time_entry.pack()

        self.unit_var = tk.StringVar(value="seconds")
        self.unit_menu = tk.OptionMenu(root, self.unit_var, "seconds", "minutes", "hours")
        self.unit_menu.pack()

        self.set_button = tk.Button(root, text="Set Reminder", command=self.set_reminder)
        self.set_button.pack()

    def set_reminder(self):
        try:
            time_value = float(self.time_entry.get())
            unit = self.unit_var.get()
            if unit == "minutes":
                time_value *= 60
            elif unit == "hours":
                time_value *= 3600

            threading.Thread(target=self.remind_me_to_take_break, args=(time_value,)).start()
            messagebox.showinfo("Reminder Set", f"Reminder set for {self.time_entry.get()} {unit}.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

    def remind_me_to_take_break(self, seconds):
        time.sleep(seconds)
        messagebox.showinfo("Break Time!", "Time to take a break!")

if __name__ == "__main__":
    root = tk.Tk()
    app = BreakReminderApp(root)
    root.mainloop()
