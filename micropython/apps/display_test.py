from machine import Pin, I2C
import time
from ssd1306 import SSD1306_I2C

# Init Display
# scl and sda can be any pin on i2c bus 1
i2c  = I2C(0, scl=Pin(40), sda=Pin(41), freq=40000)
oled = SSD1306_I2C(72, 40, i2c)
# Title Screen
oled.fill(0)

oled.text("Hello", 0, 0, 1)
oled.text("World! on", 0, 11, 1)
oled.text("a display", 0, 22, 1)
oled.text("9x4 72x40", 0, 33, 1)
oled.show()
time.sleep(5)

oled.fill(0)
oled.text("You can", 0, 0, 1)
oled.text("get up to", 0, 8, 1)
oled.text("9x5 chars", 0, 16, 1)
oled.text("on this", 0, 24, 1)
oled.text("-display-", 0, 32, 1)
oled.show()
time.sleep(5)
