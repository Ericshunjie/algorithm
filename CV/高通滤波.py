
import cv2
import matplotlib.pyplot as plt
import numpy as np

img_path = '/Users/yuanshunjie/Downloads/11.jpg'
img = cv2.imread(img_path)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
## GaussianBlur
gaus_img = cv2.GaussianBlur(img_rgb, (5,5), sigmaX=10)
## laplacian
lapla_img = cv2.Laplacian(gaus_img, cv2.CV_64F,ksize=3)
## sobel

## scharr

plt.figure()
plt.subplot(1,3,1)
plt.imshow(img_rgb)
plt.subplot(1,3,2)
plt.imshow(gaus_img)
plt.subplot(1,3,3)
plt.imshow(lapla_img)
plt.show()



