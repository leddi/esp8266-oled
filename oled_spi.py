# OLED an esp8266
#
#  D1 -- Pin -- OLED
#  D15 -  5  -- D/C  (feel free digitalPin)
#  D14 -  4  -- RST  (feel free digitalPin)
#  D13 - 14  -- SCL  (SCK)
#  D11 - 13  -- SDA  (MOSI)
#  ##  - 16  -- CS   (unused)
#  GND - GND
#  3v3 - VCC

from machine import Pin, SPI
#from machine import I2C
import ssd1306

dc_pin = Pin(5)
rst_pin = Pin(4)
cs_pin = Pin(16)

spi = SPI(sck=Pin(14), mosi=Pin(13), miso=Pin(12))
#i2c = I2C(sda=Pin(5), scl=Pin(4))
#oled_i2c = ssd1306.SSD1306_I2C(128, 64, i2c)
oled = ssd1306.SSD1306_SPI(128, 64, spi, dc_pin, rst_pin, cs_pin)
oled.fill(0)
oled.text("Hello world!", 0, 0)
oled.show()
