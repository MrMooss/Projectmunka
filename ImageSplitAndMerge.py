from PIL import Image, ImageDraw


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
