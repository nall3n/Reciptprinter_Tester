
from turtle import width
from escpos.printer import Serial

from tkinter import *

import configparser

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

# Config loading ===================================
config = configparser.ConfigParser()
config.read('config.ini')

standard_baud = int(config['SERIAL']['Baudrate'])
standard_port = config['SERIAL']['Port']
standard_bytesize = int(config['SERIAL']['bytesize'])
standard_parity = config['SERIAL']['parity']
standard_stopbits = int(config['SERIAL']['stopbits'])
standard_xonxoff = int(config['SERIAL']['xonxoff'])
#===================================================

def save_serial_config():
  config['SERIAL']['Baudrate'] = str(baudrate_list.index(int(baud_var.get())))
  config['SERIAL']['Port'] = port.get()

  with open('config.ini', 'w') as configfile:
    config.write(configfile)

  print(str(baudrate_list.index(int(baud_var.get()))))

def run_test():
  baudrate=baud_var.get()
  serial = port.get()
  run = int(loop.get())


  print(baudrate)
  print(serial)

  p = Serial(
    devfile=serial, 
    baudrate=baudrate, 
    bytesize=standard_bytesize, 
    timeout=5, 
    parity=standard_parity, 
    stopbits=standard_stopbits, 
    xonxoff=standard_xonxoff, 
    dsrdtr=1)

  i=0
  while i < run:
    p.text("HAJHAJ")
    p.text("HASEIFHEAIOUHAOawdaauwf hyiuef eiufheif eif uef h\n waiodjaiwdiowadj")
    p.text("HASEIFHEAIOUHAOawdaauwf hyiuef eiufheif eif uef h\n waiodjaiwdiowadj")
    p.text("HASEIFHEAIOUHAOawdaauwf hyiuef eiufheif eif uef h\n waiodjaiwdiowadj")
    p.barcode('1324354657687', 'EAN13', 48, 2, '', '')
    p.cut()
    i += 1


#=============================================================================


tk_font_size = 12 
tk_font = 'Times'

root = Tk()
root.title("PRINTER TESTER!!!!!")
root.geometry('500x500')


# Port entry =================================
port_lbl = Label(
  root,
  text='Set com port:',
  font=(tk_font, tk_font_size)
)
port_lbl.grid(column=1,row=0,pady=12)
port = Entry(
  root,
  width=15,
  font=(tk_font, tk_font_size)
)
port.insert(END,standard_port)
port.grid(column=2, row=0,pady=12)
#=============================================


# Baud list =================================
baud_lbl = Label(
  root,
  text = 'Baudrate:',
  font=(tk_font, tk_font_size)
)
baud_lbl.grid(column=1, row=1, pady=5) 

baud_var = StringVar(root)
baud_var.set(baudrate_list[standard_baud])
baud_opt = OptionMenu(root, baud_var, *baudrate_list)
baud_opt.grid(column=2, row=1, pady=5)

#=============================================

# Loop counter input =========================
loop_lbl = Label(
  root,
  text='loop counter:',
  font=(tk_font, tk_font_size)
)
loop_lbl.grid(column=3, row=0, padx=10)
loop = Entry(
  root,
  width=10,
  font=(tk_font, tk_font_size)
)
loop.insert(END, 10)
loop.grid(column=4, row=0)
#=============================================

# Run test button ============================
test_btn = Button(
  root,
  text="TEST",
  fg="black",
  font=(tk_font, tk_font_size),
  padx=5,
  pady=5,
  command=run_test
)
test_btn.grid(column=2, row=10, pady=5)
#=============================================

# Save config button =========================
save_btn = Button(
  root,
  text="Save Conf",
  fg="black",
  font=(tk_font, tk_font_size),
  command=save_serial_config,
)
save_btn.grid(column=1, row=10, pady=5)
#=============================================

root.mainloop()