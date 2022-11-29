from PIL import Image
import glob
import sys
import os

img = Image.open('tree.jpg')
h, w = img.size
a, b = h, w
while a % 32 != 0:
    a = a + 1
while b % 32 != 0:
    b = b + 1
img2 = img.crop((0, 0, a, b))
h, w = img.size
x, y = 0, 0
for i in range(0, h, 32):
    for j in range(0, w, 32):
        c = img.crop((j, i, j + 32, i + 32))
        c.save('temp/' + str(x) + '-' + str(y) + '.jpg')
        y += 1
    x += 1

images = [Image.open(x) for x in glob.glob('temp/*.jpg')]
widths, heights = zip(*(i.size for i in images))

total_width = sum(widths)
max_height = sum(heights)

new_im = Image.new('RGB', (total_width, max_height))

x_offset = 0
for im in images:
    new_im.paste(im, (x_offset, 0))
    x_offset += im.size[0]
# TODO 2D-re megcsinálni
new_im.save('test.jpg')

# expands the image so it can be split into 32x32 subimages
def expand_image(path):
    img = Image.open(path)
    h, w = img.size
    a, b = h, w
    while a % 32 != 0:
        a = a + 1
    while b % 32 != 0:
        b = b + 1
    img2 = img.crop((0, 0, a, b))

    return img2


def crop(img):
    h, w = img.size
    x, y = 0, 0
    for i in range(0, h, 32):
        for j in range(0, w, 32):
            c = img.crop((j, i, j + 32, i + 32))
            c.save('temp/' + str(x) + '-' + str(y) + '.jpg')
            y += 1
        x += 1


def merge_images(path):
    images = [Image.open(x) for x in 'temp/*.jpg']
    widths, heights = zip(*(i.size for i in images))

    total_width = sum(widths)
    max_height = max(heights)

    new_im = Image.new('RGB', (total_width, max_height))

    x_offset = 0
    for im in images:
        new_im.paste(im, (x_offset, 0))
        x_offset += im.size[0]

    new_im.save('test.jpg')