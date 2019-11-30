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

colorRgb = {
  "green": [0, 255, 0],
  "yellow": [255, 255, 0],
  "red": [255, 0, 0],
  "blue": [0, 0, 255],
  "white": [255, 255, 255],
  "purple": [92, 55, 138],
  "cream": [238, 255, 198],
  "maroon": [138, 0, 7],
  "orange": [255, 120, 0],
  "pink": [255, 105, 180],
}

colors = {}
for c in colorRgb:
  colors[c] = [Adafruit_WS2801.RGB_to_color(colorRgb[c][2], colorRgb[c][1], colorRgb[c][0])]

colors["badgers"] = [colors["red"], colors["white"]]
colors["packers"] = [colors["green"], colors["yellow"]]
colors["brewers"] = [colors["yellow"], colors["blue"]]
colors["bucks"] = [colors["purple"], colors["green"]]
colors["hokies"] = [colors["maroon"], colors["orange"]]
colors["christmas"] = [colors["red"], colors["green"]]

def alternate(col1, col2, start = 0, end = pixels.count()):
    for i in range(start, end):
        if i >= 0 and i < pixels.count():
            if (end - i) % 2 == 1:
                pixels.set_pixel(i, col1)
            else:
                pixels.set_pixel(i, col2)

def scroll(col1, col2):
    for length in range(1, pixels.count()):
        for rpos in range(pixels.count() + length):
            pixels.clear()
            alternate(col1, col2, rpos-length, rpos)
            pixels.show()
            time.sleep(0.08)
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        team = ""
    else:
        team = sys.argv[1].lower()

    if team in colors:
        c = colors[team]
        if len(c) == 1:
            alternate(c[0], c[0])
        else:
            alternate(c[0][0], c[1][0]) 
    else:
        pixels.clear()

    pixels.show()
