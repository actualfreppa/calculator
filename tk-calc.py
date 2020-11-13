

from tkinter import *
from tkinter import ttk


class Calculator:
    def __init__(self, master):
        self.master = master
        self.num_buttons = [ttk.Button(master, text=str(i), command=lambda: self.button_press(str(i))) for i in range(10)]
        self.extra_buttons = [ttk.Button(master, text=t) for t in ["+", "-", "/", "*", "Clear"]]
        self.buttons = self.num_buttons + self.extra_buttons
        self.e = ttk.Entry(self.master, width=35)
        self.e.grid(row=0, column=0, columnspan=3)
        for button in self.num_buttons:
            button.grid()

    def button_press(self, num):
        self.e.delete(0, END)
        self.e.insert(0, num)

def main():
    root = Tk()
    root.title("Simple Calulator")
    app = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()


