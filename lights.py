# Based on code from https://tutorials-raspberrypi.com/how-to-control-a-raspberry-pi-ws2801-rgb-led-strip/
# Need to enable SPI bus (sudo raspi-config)
# Need to install adafruit-ws2801: sudo apt-get update && sudo apt-get install python-pip -y && sudo pip install adafruit-ws2801
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
  "pink": [255, 105, 180]
}

teamColors = {
  "badgers": ["red", "white"],
  "packers": ["green", "yellow"],
  "brewers": ["yellow", "blue"],
  "bucks": ["purple", "green"],
  "hokies": ["maroon", "orange"],
  "christmas": ["red", "green"],
  "usa": ["red", "white", "blue"],
  "rainbow": ["red", "orange", "yellow", "green", "blue", "purple"]
}

colors = {}
for c in colorRgb:
  colors[c] = [Adafruit_WS2801.RGB_to_color(colorRgb[c][2], colorRgb[c][1], colorRgb[c][0])]
for c in teamColors:
  colors[c] = []
  for colorName in teamColors[c]:
    colors[c].append(colors[colorName][0])

def alternate(colAry, start = 0, end = pixels.count()):
    for i in range(start, end):
        if i >= 0 and i < pixels.count():
            pixels.set_pixel(i, colAry[i % len(colAry)])

def scroll(col1, col2):
    for length in range(1, pixels.count()):
        for rpos in range(pixels.count() + length):
            pixels.clear()
            alternate(col1, col2, rpos-length, rpos)
            pixels.show()
            time.sleep(0.08)
    
def run(input):
    allColors = []
    for i in range(0, len(input)):
        team = input[i].lower()
        if team in colors:
            allColors.extend(colors[team])
    
    if len(allColors) == 0:
        pixels.clear()
    else:
        alternate(allColors)
    
    pixels.show()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].lower() == "i":
        inputText = ""
        while inputText != "stop":
            inputText = raw_input("Enter colors {} --> ".format(colorRgb.keys()))
            run(inputText.split(' '))
    else:
        run(sys.argv)
