import os
import cv2
import numpy as np
from keras.models import load_model

generator = load_model('gen_e_20.h5', compile=False)

HR = None


def generateHr(path):
    img = convertImage(path)
    #highres = generator.predict(img)
    global HR
    HR = img


def convertImage(path):
    lr_img = cv2.imread(path)
    lr_img = cv2.cvtColor(lr_img, cv2.COLOR_BGR2RGB)
    lr_img = cv2.resize(lr_img, (32, 32))
    lr_img = lr_img / 255
    lr_img = np.expand_dims(lr_img, axis=0)
    return lr_img


