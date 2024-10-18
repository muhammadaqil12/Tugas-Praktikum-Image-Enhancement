import imageio.v3 as img 
import numpy as np 
import matplotlib.pyplot as plt



def blend (image1,op1,image2,op2):
    img1 = image1.astype(np.float32)
    img2 = image2.astype(np.float32)
    imgBlend = (img1 * op1) + (img2 * op2)
    imgBlend = np.clip(imgBlend,0,255)

img1 = img.imread("C:\\Tugas akmal (matkul citra digital)\\download.jpg")
img2 = img.imread("C:\\Tugas akmal (matkul citra digital)\\images (3).jpg")

imgBlend = blend(img1,0.5,img2,0.5)

plt.figure(figsize=(10,10))
plt.subplot(3,2,1)
plt.imshow(img1)

plt.subplot(3,2,1)
plt.imshow(img1)

plt.subplot(3,2,1)
plt.imshow(img1)

plt.subplot(3,2,1)
plt.imshow(img1)

plt.subplot(3,2,1)
plt.imshow(img1)

plt.subplot(3,2,1)
plt.imshow(img1)

plt.show()