import GAN
import os
import cv2
import numpy as np
from keras.models import load_model
import matplotlib.pyplot as plt

generator = load_model('gen_e_20.h5', compile=False)


def generateHr(path):
    img = convertImage(path)
    highres = generator.predict(img)

    # cv2.imwrite("test.jpg", highres[0])
    cv2.imshow('test', highres[0, :, :, ::-1])

    return highres[0, :, :, :]


def convertImage(path):
    lr_img = cv2.imread(path)
    lr_img = cv2.cvtColor(lr_img, cv2.COLOR_BGR2RGB)
    lr_img = lr_img / 255
    lr_img = np.expand_dims(lr_img, axis=0)
    return lr_img


