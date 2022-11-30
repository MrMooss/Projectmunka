import glob

import GAN
import os
import cv2
import numpy as np
from keras.models import load_model
import matplotlib.pyplot as plt
import ImageSplitAndMerge as ism
from PIL import Image
import tempfile

generator = load_model('gen_e_20.h5', compile=False)


def generateHr(path):
    with tempfile.TemporaryDirectory() as temp:
        img = Image.open(path)
        h, w = img.size
        if h != 32 or w != 32:
            img = ism.expand_image(img)
            w, h = img.size
            ism.crop(img)
            images = glob.glob('temp/*.jpg')
            for im in images:
                img2 = convertImage(im)
                hr = generator.predict(img2)
                img3 = Image.fromarray(hr)
                img3.save('temp/' + os.path.basename(im))
            imagehigh = ism.merge_images('temp', w, h)
            return imagehigh
            # TODO convertálás PyQtra Pillow imageből
        else:
            img = convertImage(path)
            highres = generator.predict(img)
            return highres[0, :, :, :]


def convertImage(path):
    lr_img = cv2.imread(path)
    lr_img = cv2.cvtColor(lr_img, cv2.COLOR_BGR2RGB)
    lr_img = lr_img / 255
    lr_img = np.expand_dims(lr_img, axis=0)
    return lr_img


