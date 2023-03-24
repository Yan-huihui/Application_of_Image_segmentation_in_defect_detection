"""
2020.09.26:alian
改变图片的位深度
"""
from PIL import Image
import numpy as np
import cv2
import os


#  方法一：
# 单张图片
# img = Image.open(r'C:\Users\znjt\Desktop\huhui\40051.jpg')
# img = Image.fromarray(np.uint8(img))
# t = img.convert('L')
# img=Image.fromarray(np.uint8(t)*255)
# img.save(r'C:\Users\znjt\Desktop\huhui\40051(8).jpg')

# 批量转换图片位深度
path = r'./datasets/SegmentationClass/'
save_path = r'./VOCdevkit/VOC2007/SegmentationClass/'
for i in os.listdir(path):
    img = Image.open(path+i)
    img = Image.fromarray(np.uint8(img))
    t = img.convert('L')
    img = Image.fromarray(np.uint8(t))  # *255
    img.save(save_path + i)
    print(save_path + i)


# 方法二
# img = cv2.imread(r'C:\Users\znjt\Desktop\huhui\40051.jpg')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imwrite(r'C:\Users\znjt\Desktop\huhui\40051(8).jpg',img)