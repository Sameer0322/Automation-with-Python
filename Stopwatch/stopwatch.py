import tkinter as tk
from datetime import datetime, timedelta

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")
        
        # Make the window full screen
        self.root.attributes('-fullscreen', True)
        self.root.bind("<Escape>", self.exit_fullscreen)

        self.running = False
        self.time_elapsed = timedelta(0)
        self.last_time = None

        self.label = tk.Label(root, text="00:00:00", font=("Helvetica", 160), fg="black")
        self.label.pack(expand=True)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack()

        self.start_button = tk.Button(self.button_frame, text="Start", command=self.start, width=10, font=("Helvetica", 24))
        self.start_button.grid(row=0, column=0, padx=5, pady=5)

        self.stop_button = tk.Button(self.button_frame, text="Stop", command=self.stop, width=10, font=("Helvetica", 24))
        self.stop_button.grid(row=0, column=1, padx=5, pady=5)

        self.reset_button = tk.Button(self.button_frame, text="Reset", command=self.reset, width=10, font=("Helvetica", 24))
        self.reset_button.grid(row=0, column=2, padx=5, pady=5)

        self.update_clock()

    def exit_fullscreen(self, event=None):
        self.root.attributes('-fullscreen', False)

    def start(self):
        if not self.running:
            self.running = True
            self.last_time = datetime.now()
            self.update_clock()

    def stop(self):
        if self.running:
            self.running = False
            self.update_clock()

    def reset(self):
        self.running = False
        self.time_elapsed = timedelta(0)
        self.label.config(text="00:00:00")

    def update_clock(self):
        if self.running:
            now = datetime.now()
            self.time_elapsed += now - self.last_time
            self.last_time = now
            self.label.config(text=str(self.time_elapsed).split('.')[0])
        
        self.root.after(1000, self.update_clock)

if __name__ == "__main__":
    root = tk.Tk()
    stopwatch = Stopwatch(root)
    root.mainloop()
