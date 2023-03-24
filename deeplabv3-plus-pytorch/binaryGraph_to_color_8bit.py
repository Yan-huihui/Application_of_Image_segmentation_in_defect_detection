from PIL import Image
import numpy as np
#img = Image.open("./VOCdevkit/VOC2007/SegmentationClass/0.png")
img = Image.open("./datasets/SegmentationClass/0.png")
#img.show()
img_array = np.array(img) #把图像转成数组格式img = np.asarray(image)
shape = img_array.shape
print(img_array.shape)
# for i in range(0,shape[0]):
#     for j in range(0,shape[1]):
#         value = img_array[i, j]
#         #print("",value)
#         if value[0] != 0:
#            print("", value)
height = shape[0]
width = shape[1]
dst = np.zeros((height,width,3))
for h in range(0,height):
    for w in range (0,width):
        (b,g,r) = img_array[h,w]
        # if (b,g,r)==(255,255,255):#白色
        #     img_array[h,w] = (255,0,0)#红
        # elif (b, g, r) == (0, 0, 0):  # 黑色
        #     pass
        #     #img_array[h, w] = (255, 0, 0)  # 红色
        # else:
        #     img_array[h,w] = (255, 255, 255)
        if np.mean(img_array[h, w]) >= 128: # 白
            img_array[h, w] = (150, 50, 50)  # 红
        else:                               # 黑
            img_array[h, w] = (0, 0, 0)     # 纯黑
        dst[h,w] = img_array[h,w]
img2 = Image.fromarray(np.uint8(dst))
t = img2.convert('L')
img2 = Image.fromarray(np.uint8(t))  # *255
img2.show(img2)
img2.save("after.png","png")
