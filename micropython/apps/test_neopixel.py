# Test the neopixel

import machine, neopixel, time
np = neopixel.NeoPixel(machine.Pin(39), 1)  # 44 according to schematic does not work either

np[0] = (255, 0, 0)

RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)

while True:
    np[0] = RED
    print("red")
    time.sleep_ms(1000)
    np[0] = GREEN
    print("GREEN")
    time.sleep_ms(1000)
    np[0] = BLUE
    print("BLUE")
    time.sleep_ms(1000)
