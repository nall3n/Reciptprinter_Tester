
from escpos.printer import Serial

from tkinter import *


baudrate_list = [
  110, 
  300, 
  600, 
  1200, 
  2400, 
  4800, 
  9600, 
  14400, 
  19200,  #Rongta
  38400, 
  57600, 
  115200, #SAM4S
  128000,
  256000
]



def run_test():
  baudrate=baud_listbox.get(baud_listbox.curselection())
  serial = port.get()

  print(baudrate)
  print(serial)

  p = Serial(
    devfile=serial, 
    baudrate=baudrate, 
    bytesize=8, 
    timeout=5, 
    parity='N', 
    stopbits=1, 
    xonxoff=0, 
    dsrdtr=1)

  i=0
  while i < 10:
    p.text("HAJHAJ")
    p.text("HASEIFHEAIOUHAOawdaauwf hyiuef eiufheif eif uef h\n waiodjaiwdiowadj")
    p.text("HASEIFHEAIOUHAOawdaauwf hyiuef eiufheif eif uef h\n waiodjaiwdiowadj")
    p.text("HASEIFHEAIOUHAOawdaauwf hyiuef eiufheif eif uef h\n waiodjaiwdiowadj")
    p.barcode('1324354657687', 'EAN13', 48, 2, '', '')
    p.cut()
    i += 1


tk_font_size = 12 
tk_font = 'Times'

root = Tk()
root.title("PRINTER TESTER!!!!!")
root.geometry('600x500')

# Port entry =================================
port_lbl = Label(
  root,
  text='Set com port',
  font=(tk_font, tk_font_size)
)
port_lbl.grid(column=1,row=0,pady=12)
port = Entry(
  root,
  width=20,
  font=(tk_font, tk_font_size)
)
port.grid(column=2, row=0,pady=12)

# Baud list =================================
baud_lbl = Label(
  root,
  text = 'Baudrate',
  font=(tk_font, tk_font_size)
)
baud_lbl.grid(column=1, row=1, pady=5) 
baud_listbox = Listbox(root,
    selectmode=SINGLE,
)
index = 1
for baud in baudrate_list:
  baud_listbox.insert(index, baud)
  index += 1
baud_listbox.grid(column=2, row=1, pady=5)




baud_listbox.insert(1,"1231")

test_btn = Button(
  root,
  text="TEST",
  fg="black",
  font=(tk_font, tk_font_size),
  padx=10,
  pady=10,
  command=run_test
)
test_btn.grid(column=2, row=10)


root.mainloop()


