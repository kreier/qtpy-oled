# QT Py with 0.42 OLED from 01Space
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

## Circuitpython

Since there is a working MicroPython version and the USB-PID `0x8173 | 01Space ESP32-S3-0.42OLED - MicroPython` [since May 16, 2023](https://github.com/espressif/usb-pids/pull/96) it should be possible to write a pull request for circuitpython. The USB-PID for CircuitPython is `0x8172` - [see line 378](https://github.com/espressif/usb-pids/blob/main/allocated-pids.txt)

## MicroPython

No official version yet. Currently there are only [7 ports for the ESP32-S3](https://micropython.org/download/?mcu=esp32s3) on the website and none is working with the QT Py because it has only 4MB Flash, yet all the images are built for 8MB flash and can therefore not initiate the flash as storage for programs.

In May 2023 [Matt Trentini from Australia](https://github.com/mattytrentini/micropython/tree/add_01space_esp32s3_oled/ports/esp32/boards/01SPACE_ESP32S3_OLED) tried to add the board and could successfully compile a version of Micropython v1.19. It's available on the discord server.

## Arduino

Will follow ...
