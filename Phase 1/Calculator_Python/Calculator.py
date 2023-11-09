import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        self.result_var = tk.StringVar()
        self.result_var.set("")

        self.result_entry = tk.Entry(master, textvariable=self.result_var, font=('Arial', 16), bd=10, insertwidth=4, width=14, justify='right')
        self.result_entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(master, text=text, padx=20, pady=20, font=('Arial', 16), command=lambda t=text: self.button_click(t))
            button.grid(row=row, column=col)

    def button_click(self, value):
        current_text = self.result_var.get()

        if value == 'C':
            self.result_var.set("")
        elif value == '=':
            try:
                result = str(eval(current_text))
                self.result_var.set(result)
            except:
                self.result_var.set("Error")
        else:
            self.result_var.set(current_text + value)

def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
