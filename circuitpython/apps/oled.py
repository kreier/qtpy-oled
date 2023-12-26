# Test the 0.42 OLED 72x40

import time, board, neopixel, displayio, terminalio, busio, digitalio
import adafruit_displayio_ssd1306
from adafruit_display_text import label

#scl1 = digitalio.DigitalInOut(board.D40)
#scl1.pull = digitalio.Pull.UP
#sda1 = digitalio.DigitalInOut(board.D41)
#da1.pull = digitalio.Pull.UP

displayio.release_displays()
i2c = busio.I2C(board.D40, board.D41)  # SCL SDA   IO40 IO41
#i2c = board.I2C()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(
    display_bus, width=128, height=64, colstart=2
)

displaymenu = displayio.Group()
listitem = label.Label(terminalio.FONT, text="Hello world!")
listitem.x = 0
listitem.y = 5
displaymenu.append(listitem)
display.show(displaymenu)



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
