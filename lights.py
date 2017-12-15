# Based on code from https://tutorials-raspberrypi.com/how-to-control-a-raspberry-pi-ws2801-rgb-led-strip/
import sys
import time
import RPi.GPIO as GPIO
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI
 
PIXEL_COUNT = 32
 
SPI_PORT   = 0
SPI_DEVICE = 0
pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE), gpio=GPIO)

GREEN = Adafruit_WS2801.RGB_to_color(0, 255, 0)
YELLOW = Adafruit_WS2801.RGB_to_color(0, 255, 255)
RED = Adafruit_WS2801.RGB_to_color(0, 0, 255)
BLUE = Adafruit_WS2801.RGB_to_color(255, 0, 0)
WHITE = Adafruit_WS2801.RGB_to_color(255, 255, 255)
PURPLE = Adafruit_WS2801.RGB_to_color(138, 55, 92)

def alternate(col1, col2, start = 0, end = pixels.count()):
    for i in range(start, end):
        if i >= 0 and i < pixels.count():
            if (end - i) % 2 == 1:
                pixels.set_pixel(i, col1)
            else:
                pixels.set_pixel(i, col2)
    pixels.show()

def scroll(col1, col2):
    for length in range(1, pixels.count()):
        for rpos in range(pixels.count() + length):
            pixels.clear()
            alternate(col1, col2, rpos-length, rpos)
            pixels.show()
            time.sleep(0.08)
    
if __name__ == "__main__":
    if sys.argv[1] == "Badgers":
	alternate(RED, WHITE)
    elif sys.argv[1] == "Packers":
        alternate(GREEN, YELLOW)
    elif sys.argv[1] == "Brewers":
        alternate(YELLOW, BLUE)
    elif sys.argv[1] == "Bucks":
        alternate(PURPLE, GREEN)
    else:
        pixels.clear()
	pixels.show()
