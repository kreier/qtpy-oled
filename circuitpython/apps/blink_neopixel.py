# Test the neopixel

import time, board, neopixel

led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = 0.5
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)

while True:
    led[0] = RED
    time.sleep(1)
    led[0] = GREEN
    time.sleep(1)
    led[0] = BLUE
    time.sleep(1)
