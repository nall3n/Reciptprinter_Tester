from escpos.printer import Serial


p = Serial(devfile="COM1", 
baudrate=19200, 
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
