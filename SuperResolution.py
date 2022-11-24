import GAN
import os
import cv2
import numpy as np
from keras.models import load_model
from keras.layers import Input


shape = (32, 32, 3)
ip = Input(shape=shape)
generator = GAN.create_gen(ip, num_res_block = 16)
generator.load_weights('gen_e_20.h5')

def generateHr(path):
    img = convertImage(path)
    cv2.imwrite('img.jpeg', img)
    highres = generator.predict(img)
    cv2.imwrite('high.jpeg', highres)
    return highres


def convertImage(path):
    lr_img = cv2.imread(path)
    lr_img = cv2.cvtColor(lr_img, cv2.COLOR_BGR2RGB)
    lr_img = cv2.resize(lr_img, (32, 32))
    lr_img = lr_img / 255
    lr_img = np.expand_dims(lr_img, axis=0)
    return lr_img


