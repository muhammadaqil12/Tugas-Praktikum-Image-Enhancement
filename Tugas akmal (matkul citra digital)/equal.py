import imageio.v3 as img
import numpy as np
import matplolib.pyplot as plt

def equalization(image):
    hist, bins = np.histogram(image.pltten(), bins = 256, range = [0,256])
    cfd = hist.cumsum()
    cfd_normalized = (cfd/cdf.max()) * 255
    imgequal = np.interp(image.flatten(), bins [:-1]), cfd_normalized
    return imgEqual.reshape(image.shape).astpye