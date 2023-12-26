# qtpy-oled
Some software projects for the tiny Qt-Py copy from 01Space with 72x40 OLED display

## Projects

I wanted to get CircuitPython running, but get error messages for missing pull up resistors for the two I2C busses, both on the STEMMA/QUIIC connector and the display.

Solution: Got none so fare. But neopixel works

I connected a i2c light sensor to the STEMMA connector. It has measaburale 10 kOhm pull up resistors, but the warning still persists. The schematic does not show pull up on the connector to the display.

## Hardware

Producer 01Space has some github information

- [Repository from 01Space](https://github.com/01Space/ESP32-S3-0.42OLED)
- [Repository for the ESP32-C3-0.42LCD with MicroPython support](https://github.com/01Space/ESP32-C3-0.42LCD)

It has 4 MB RAM (confirmed with esptool)
It might have 2 MB PSRAM

- IO39 is board.NEOPIXEL
- Display is I2C: SCL1 SDA1 3.3V GND - IO40 IO41
- STEMMA is I2C: SCL SDA 3.3V GND - IO1 IO2
