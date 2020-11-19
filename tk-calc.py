

from tkinter import *
from tkinter import ttk


class Calculator:
    def __init__(self, master):
        self.master = master
        #Define buttons
        #self.c = lambda x: self.button_press(x)
        #self.num_buttons = [ttk.Button(master, text=str(i), command=self.c(str(i))) for i in range(10)]
        #self.extra_buttons = [ttk.Button(master, text=t) for t in ["+", "-", "/", "*", "Clear"]]
        #self.buttons = self.num_buttons + self.extra_buttons

        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=1)
        self.master.rowconfigure(2, weight=1)
        self.master.rowconfigure(3, weight=1)
        self.master.rowconfigure(4, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=1)
        self.master.columnconfigure(2, weight=1)
        self.master.columnconfigure(3, weight=1)

        self.b1 = ttk.Button(self.master, text="1", command=lambda: self.button_press("1"))
        self.b2 = ttk.Button(self.master, text="2", command=lambda: self.button_press("2"))
        self.b3 = ttk.Button(self.master, text="3", command=lambda: self.button_press("3"))
        self.b4 = ttk.Button(self.master, text="4", command=lambda: self.button_press("4"))
        self.b5 = ttk.Button(self.master, text="5", command=lambda: self.button_press("5"))
        self.b6 = ttk.Button(self.master, text="6", command=lambda: self.button_press("6"))
        self.b7 = ttk.Button(self.master, text="7", command=lambda: self.button_press("7"))
        self.b8 = ttk.Button(self.master, text="8", command=lambda: self.button_press("8"))
        self.b9 = ttk.Button(self.master, text="9", command=lambda: self.button_press("9"))
        self.b0 = ttk.Button(self.master, text="0", command=lambda: self.button_press("0"))
        self.bcomma = ttk.Button(self.master, text=",", command=lambda: self.button_press(","))
        self.badd = ttk.Button(self.master, text="+", command=lambda: self.button_press("+"))
        self.bsubt = ttk.Button(self.master, text="-", command=lambda: self.button_press("-"))
        self.bdiv = ttk.Button(self.master, text="/", command=lambda: self.button_press("/"))
        self.bmult = ttk.Button(self.master, text="*", command=lambda: self.button_press("*"))
        self.beq = ttk.Button(self.master, text="=", command=self.button_press_eq)
        self.b_clear = ttk.Button(self.master, text="Clear", command=self.clear)
        self.b_quit = ttk.Button(self.master, text="Quit", command=self.quit)
        
        self.e = ttk.Entry(master, width=35)
        self.e.grid(row=0, column=0, pady=5, columnspan=5, stick="nsew")
        
        self.b1.grid(row=3, column=0, stick="nsew")
        self.b2.grid(row=3, column=1, stick="nsew")
        self.b3.grid(row=3, column=2, stick="nsew")
        self.b4.grid(row=2, column=0, stick="nsew")
        self.b5.grid(row=2, column=1, stick="nsew")
        self.b6.grid(row=2, column=2, stick="nsew")
        self.b7.grid(row=1, column=0, stick="nsew")
        self.b8.grid(row=1, column=1, stick="nsew")
        self.b9.grid(row=1, column=2, stick="nsew")
        self.b0.grid(row=4, column=1, stick="nsew")
        self.bdiv.grid(row=1, column=3, stick="nsew")
        self.bmult.grid(row=2, column=3, stick="nsew")
        self.bsubt.grid(row=3, column=3, stick="nsew")
        self.badd.grid(row=4, column=3, stick="nsew")
        #self.bcomma.grid(row=4, column=0)
        self.beq.grid(row=4, column=2, stick="nsew")
        self.b_clear.grid(row=4, column=0, stick="nsew")
        self.b_quit.grid(row=5, column=0, columnspan=4, sticky="nsew")

    def button_press(self, num):
        #self.e.delete(0, END)
        #s = self.e.get()
        #self.e.insert(0, self.e.get() + num)
        self.e.insert(END, num)

    def button_press_eq(self):
        expression = self.e.get()
        self.e.delete(0, END)

        # TODO Refactor, do not use eval!!!
        self.e.insert(0, eval(expression))


    def clear(self):
        self.e.delete(0, END)

    def quit(self):
        self.master.destroy()


def main():
    root = Tk()
    root.title("Simple Calulator")
    app = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()


