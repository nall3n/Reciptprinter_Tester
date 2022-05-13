# Os imports
import os
from os import listdir
from os.path import isfile, join
import tkinter

# GUI Tkinter imports
from tkinter import * 
from tkinter import filedialog

# Tk layout and contents
#=================================================================================
tk_font_size = 12

root = Tk()
root.title('PRINTER TESTER!!!!!')
root.geometry('600x500')

#==========================================
# adding a label to the root window
lbl = Label(
    root, 
    text = "Enter Name", 
    font=('Times', tk_font_size)
)
lbl.grid(column=1, row=0, pady=15,)
#========================================== 
# adding Entry Field
txt = Entry(
    root, 
    width=20, 
    font=('Times', tk_font_size)
)
txt.grid(column =2, row =0,pady=15,)
#==========================================
#==========================================
font_listbox = Listbox(root,
    selectmode=SINGLE,
)
font_list = os.listdir('Fonts')
index = 1
for font in font_list:
    font_listbox.insert(index, font)
    index += 1
font_listbox.grid(column=1, row=3)
listbox_lbl = Label(root, text = "Leave blank to use Helvetica-Bold", font=('Times', tk_font_size))
listbox_lbl.grid(column=2, row=3)
#==========================================
# Buton to run test
btn = Button(
    root, 
    text = "TEST", 
    fg = "black",
    font=('Times', tk_font_size),
    padx=10,
    pady=10,
    command=generate_checker
)
btn.grid(column=1, row=5)

test = Label(
    fg='black',
    text='If no color or font is entered in the import file. The settings set here will be used'
)
test.grid(
    column=1, 
    row=6, 
    columnspan = 2,    
    padx=10,
    pady=15,
    sticky = tkinter.W+tkinter.E
)

preview_lbl = Label(
    root,
    text='COLOR Preview',
    font=('Times', 20),
    fg='#FFFFFF',
    bg='#496d89'
)
preview_lbl.grid(
    column = 1, 
    row = 10, 
    columnspan = 2,
    rowspan= 3,
    pady=10, 
    ipady=10,
    sticky = tkinter.W+tkinter.E,
)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(3, weight=1)
# Execute Tkinter
root.mainloop()
