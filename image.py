from PIL import Image
import numpy as np

img = Image.open('sigyo.jpg')
width, height = img.size

print(img.size)

img_pixels = []

for y in range(height):
	for x in range(width):
		img_pixels.append(img.getpixels((x,y)))

img_pixels = np.array(img_pixels)
img2 = Image.new('RGB',(width,height))

img.show()