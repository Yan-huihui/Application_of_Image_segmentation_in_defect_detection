import os
from PIL import Image

dirname_read="./datasets/JPEGImages/"
dirname_write="./VOCdevkit/VOC2007/JPEGImages/"
names=os.listdir(dirname_read)
count=0
for name in names:
    img=Image.open(dirname_read+name)
    name=name.split(".")
    if name[-1] == "png":
        name[-1] = "jpg"
        name = str.join(".", name)
        #r,g,b,a=img.split()
        #img=Image.merge("RGB",(r,g,b))
        to_save_path = dirname_write + name
        img.save(to_save_path)
        count+=1
        print(to_save_path, "------conut：",count)
    else:
        continue