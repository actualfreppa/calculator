

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
        self.bsubt = ttk.Button(self.master, text="-", command=lambda: self.button_press("+"))
        self.bdiv = ttk.Button(self.master, text="/", command=lambda: self.button_press("+"))
        self.bmult = ttk.Button(self.master, text="*", command=lambda: self.button_press("+"))
        self.beq = ttk.Button(self.master, text="=", command=lambda: self.button_press("="))
        self.b_clear = ttk.Button(self.master, text="Clear", command=self.clear)
        self.b_quit = ttk.Button(self.master, text="Quit", command=self.quit)
        
        self.e = ttk.Entry(master, width=35)
        self.e.grid(row=0, column=0, columnspan=5)
        
        self.b1.grid(row=3, column=0)
        self.b2.grid(row=3, column=1)
        self.b3.grid(row=3, column=2)
        self.b4.grid(row=2, column=0)
        self.b5.grid(row=2, column=1)
        self.b6.grid(row=2, column=2)
        self.b7.grid(row=1, column=0)
        self.b8.grid(row=1, column=1)
        self.b9.grid(row=1, column=2)
        self.b0.grid(row=4, column=1)
        self.bdiv.grid(row=1, column=3)
        self.bmult.grid(row=2, column=3)
        self.bsubt.grid(row=3, column=3)
        self.badd.grid(row=4, column=3)
        self.bcomma.grid(row=4, column=0)
        self.beq.grid(row=4, column=2)
        #self.b_clear.grid(row=4, column=1)
        #self.b_quit.grid(row=4, column=2)

    def button_press(self, num):
        #self.e.delete(0, END)
        #s = self.e.get()
        #self.e.insert(0, self.e.get() + num)
        self.e.insert(END, num)

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


