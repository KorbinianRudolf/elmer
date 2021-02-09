from PIL import Image


url = './animation/cropped/crpd_c1.png'

img = Image.open(url)

img_data = img.load()
width, height = img.size

mask = Image.new('RGBA', img.size, (255, 255, 255, 255))
mask_data = mask.load()

for i in range(width):
    for j in range(height):
        if img_data[i, j] == (0, 0, 0, 0):
            mask_data[i, j] = (0, 0, 0, 0)

mask.save('./animation/cropped/mask.png', 'PNG')