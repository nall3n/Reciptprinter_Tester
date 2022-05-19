
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

standard_baud =     int(config['SERIAL']['Baudrate'])
standard_port =     config['SERIAL']['Port']
standard_bytesize = int(config['SERIAL']['bytesize'])
standard_parity =   config['SERIAL']['parity']
standard_stopbits = int(config['SERIAL']['stopbits'])
standard_xonxoff =  int(config['SERIAL']['xonxoff'])
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
  try:
    test = tests_listbox.curselection()[0]
  except:
    test = 9999

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

  if test == 0:
    print("Running test 1")
    test_print(p, run)
  elif test == 1:
    print("Running test 2")
    test_feed_and_cut(p, run)
  elif test == 2:
    print("Running test 3")
    test_qr_code(p, run)
  else: 
    error_txt.set("Plz select a test type")

  print("Test done")


def test_print(p:Serial, run:int):
  i = 0
  while i < run:
    p.text("ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ ")
    p.text('abcdefghijklmnopqrstuvwxyzåäö ')
    p.text('1234567890 ')
    p.text(',;.:-_*^¨!"#¤%&/()=?`` ')
    p.text("ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ ")
    p.text('abcdefghijklmnopqrstuvwxyzåäö ')
    p.text('1234567890 ')
    p.text(',;.:-_*^¨!"#¤%&/()=?``')
    p.barcode('1324354657687', 'EAN13', 48, 2, '', '')
    p.cut()
    i += 1

def test_feed_and_cut(p:Serial, run:int):
  i = 0
  while i < run:
    p.text(' ')
    p.cut()
    i += 1


def test_qr_code(p:Serial, run:int):
  i = 0
  while i < run:
    p.qr(content="http://notes.nallen.tech", ec=0, size=16, model=2, native=False)
    p.text('QR Test')
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

# Select test type List box ==================
tests_listbox = Listbox(root,
  selectmode=SINGLE,
  width=20,
)
tests_listbox.insert(0,"TEXT PRINT")
tests_listbox.insert(1,"FEED AND CUT TEST")
tests_listbox.insert(2,"TEST QR CODE")

tests_listbox.grid(column=3, row=1,columnspan=2,)
#=============================================

# Error display lable ========================
error_txt = StringVar()
error_txt.set('')
error_lbl = Label(
  root, 
  textvariable=error_txt,
  font=(tk_font,tk_font_size),
)
error_lbl.grid(column=3,row=10, columnspan=2)
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