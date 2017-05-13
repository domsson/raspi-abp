#!/usr/bin/env python3
import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Raspberry Pi pin configuration:
RST = 24

# 128x64 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3C)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
#draw.rectangle((0,0,width,height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
#padding = 2
#shape_width = 20
#top = padding
#bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
#x = padding
# Draw an ellipse.
#draw.ellipse((x, top , x+shape_width, bottom), outline=255, fill=0)
#x += shape_width+padding
# Draw a rectangle.
#draw.rectangle((x, top, x+shape_width, bottom), outline=255, fill=0)
#x += shape_width+padding
# Draw a triangle.
#draw.polygon([(x, bottom), (x+shape_width/2, top), (x+shape_width, bottom)], outline=255, fill=0)
#x += shape_width+padding
# Draw an X.
#draw.line((x, bottom, x+shape_width, top), fill=255)
#draw.line((x, top, x+shape_width, bottom), fill=255)
#x += shape_width+padding

# Load default font.
#font = ImageFont.load_default()

# Alternatively load a TTF font.  Make sure the .ttf font file is in the same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
#font = ImageFont.truetype('cellphone_varwidth.ttf', 16)
font = ImageFont.truetype('cellphone_6px.ttf', 16)

# Write two lines of text.
#draw.text((x, top),    'Hello',  font=font, fill=255)
#draw.text((x, top+20), 'World!', font=font, fill=255)

#draw.line((0, 10, 128, 10), fill=255)
#draw.line((0, 54, 128, 54), fill=255)
#draw.point((64,32), fill=255)

draw.text((2, -4), "0123456789 !@#$%^&*()-=", font=font, fill=255)
draw.text((2,  4), "abcdefghijklmnopqrstuvwxyz", font=font, fill=255)
draw.text((2, 12), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", font=font, fill=255)
draw.text((2, 20), "012345678901234567890123456789", font=font, fill=255)
draw.text((2, 28), "Stephen King - The Dark Tower", font=font, fill=255)
draw.text((2, 36), "GODDAMN HOW MANY LINES?", font=font, fill=255)
draw.text((2, 44), "The seventh line already", font=font, fill=255)
draw.text((2, 52), "Finally, the last line!", font=font, fill=255)

# Display image.
disp.image(image)
disp.display()
