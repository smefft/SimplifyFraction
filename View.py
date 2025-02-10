from tkinter import *
import customtkinter as ctk


#TODO add clear button
#TODO put fraction in the middle of the screen
class App(Tk):
    def __init__(self, controller):
        super().__init__()
        self.title("Simplify")
        self.geometry("175x105")
        self.controller = controller

        self.main_canvas = Canvas(self, width=400, height=400)
        self.main_canvas.pack()

        self.numerator = Entry(self.main_canvas, width=5)
        self.numerator.place(x=10, y=10)
        self.main_canvas.create_line(10, 45, 65, 45, fill="black", width=1)
        self.denominator = Entry(self.main_canvas, width=5)
        self.denominator.place(x=10, y=50)

        equal_sign = Label(self.main_canvas, text="=")
        equal_sign.place(x=70, y=30)

        self.new_numerator = Label(self.main_canvas, text="")
        self.new_numerator.place(x=90, y=13)
        self.new_denominator = Label(self.main_canvas, text="")
        self.new_denominator.place(x=90, y=50)

        self.bind("<Return>", self.on_click)
    
    def on_click(self, event=None):
        (new_numerator, new_denominator) = self.controller.simplify(self.numerator.get(), self.denominator.get())
        self.new_numerator.config(text=new_numerator)
        self.new_denominator.config(text=new_denominator)

        #TODO line length doeesn't update as expected
        width = max(self.new_denominator.winfo_width(), self.new_numerator.winfo_width())
        self.main_canvas.create_line(90, 43, 90+width+8, 43, fill="black", width=1)

