import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("500x400")

        self.expression = ""
        self.input_text = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Create input field
        input_frame = ttk.Frame(self.root)
        input_frame.pack(pady=10)

        input_field = ttk.Entry(input_frame, textvariable=self.input_text, font=('arial', 18, 'bold'), justify='right')
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10, padx=10, fill='x')

        # Create buttons frame
        buttons_frame = ttk.Frame(self.root)
        buttons_frame.pack()

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0)
        ]

        for (text, row, col) in buttons:
            self.create_button(text, row, col, buttons_frame)

    def create_button(self, text, row, col, frame):
        button = ttk.Button(frame, text=text, command=lambda: self.on_button_click(text))
        button.grid(row=row, column=col, ipadx=10, ipady=10, padx=5, pady=5, sticky="nsew")

    def on_button_click(self, char):
        if char == '=':
            self.calculate()
        elif char == 'C':
            self.clear()
        else:
            self.expression += str(char)
            self.input_text.set(self.expression)

    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except Exception as e:
            self.input_text.set("Error")
            self.expression = ""

    def clear(self):
        self.expression = ""
        self.input_text.set("")

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
