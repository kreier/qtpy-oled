# MicroPython i2c scanner
# Return decimal and hexa adress of each i2c device

import machine
#i2c = machine.SoftI2C(scl=machine.Pin(1), sda=machine.Pin(2))    # display at 35 or 0x23
i2c = machine.SoftI2C(scl=machine.Pin(40), sda=machine.Pin(41))   # STEMMA

print('Scan i2c bus...')
devices = i2c.scan()

if len(devices) == 0:
  print("No i2c device !")
else:
  print('i2c devices found:',len(devices))

  for device in devices:  
    print("Decimal address: ",device," | Hexa address: ",hex(device))