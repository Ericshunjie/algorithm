

import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import scipy.signal as ss

def medianFilter(img,kernel=3):
    h,w,_ = img.shape
    target = np.zeros(img.shape)
    for i in range(h):
        for j in range(w):
            top = max(0,i - kernel // 2)
            bottom = min(i + kernel // 2, h-1)
            left = max(j - kernel // 2,0)
            right = min(j + kernel // 2, w-1)
            target[i,j] = np.median(img[top:bottom+1, left:right+1], axis=(0,1))
    return target


img_path = '/Users/yuanshunjie/Downloads/11.jpg'
# img = cv2.imread(img_path)
img = plt.imread(img_path).astype(float)/255
img_0 = img.copy()
rand = np.random.rand(*img.shape)
rand = rand * (rand > 0.9)
img += rand
plt.figure('11')
plt.subplot(1,3,1)
plt.imshow(img_0)
plt.subplot(1,3,2)
plt.imshow(img)
# 自己写的逐点遍历太慢
# img_f = medianFilter(img)

## cv2 
# img1 = cv2.imread(img_path)
# img1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
# img_cvmf = cv2.medianBlur(img1,3)
# print(img_cvmf.shape)
# cv2.imshow('dst',img_cvmf)

## scipy.single 也不算块 会自动pad0
img1 = img + 0
for i in range(3):
    img1[:,:,i] = ss.medfilt2d(img1[:,:,i],[3,3])

plt.subplot(1,3,3)
plt.imshow(img1)
plt.show()