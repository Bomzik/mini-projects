from tkinter import *
from tkinter import ttk

root = Tk()
root.title('ColorInfo')
root.geometry('300x300')

label = Label(text='ColorInfo', font=('Serif', 16))
label.pack()

clr_name = ttk.Label(text='#000000', background='#FFFFFF', padding=10, font=('Serif', 16))
clr_name.pack()

def update_label(color_code):
    clr_name.config(text=color_code, background=color_code)

def red_click():
    update_label('#FF0000')

def orange_click():
    update_label('#FFA500')

def yellow_click():
    update_label('#FFFF00')

def green_click():
    update_label('#008000')

def cyan_click():
    update_label('#00FFFF')

def blue_click():
    update_label('#0000FF')

def purple_click():
    update_label('#800080')


button_frame = Frame(root)
button_frame.pack()

red_btn = Button(button_frame, text='Red', bg='red', width=12, command=red_click)
red_btn.grid(row=0, column=0, padx=10, pady=15)

orange_btn = Button(button_frame, text='Orange', bg='orange', width=12, command=orange_click)
orange_btn.grid(row=0, column=1, padx=10, pady=15)

yellow_btn = Button(button_frame, text='Yellow', bg='yellow', width=12, command=yellow_click)
yellow_btn.grid(row=1, column=0, padx=10, pady=15)

green_btn = Button(button_frame, text='Green', bg='green', width=12, command=green_click)
green_btn.grid(row=1, column=1, padx=10, pady=15)

cyan_btn = Button(button_frame, text='Cyan', bg='cyan', width=12, command=cyan_click)
cyan_btn.grid(row=2, column=0, padx=10, pady=15)

blue_btn = Button(button_frame, text='Blue', bg='blue', width=12, command=blue_click)
blue_btn.grid(row=2, column=1, padx=10, pady=15)

purple_btn = Button(button_frame, text='Purple', bg='purple', width=29, command=purple_click)
purple_btn.grid(row=3, columnspan=2, padx=10, pady=15)

root.mainloop()

