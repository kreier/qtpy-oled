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
oled.text("World!", 0, 10, 1)
oled.text("on in 9x4", 0, 20, 1)
oled.text("Display", 0, 30, 1)
oled.show()
time.sleep(5)
