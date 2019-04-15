# -*- coding: utf-8 -*
"""
Created by Xingxiangrui on 2019.4.15
This code is created to copy and rename images from the source_dir
 to the target_dir
"""

#import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import os

#image source directory
#---------------------here need to be changed---------dir location---------
source_dir="/Users/baidu/Desktop/苏州瑞图数据集/苏州瑞图数据集/images/单晶_暗域/"
target_dir="/Users/baidu/Desktop/苏州瑞图数据集/运行结果/单2多-lam5idt0/暗域/test_latest/"
if not os.path.isdir(target_dir):
    os.makedirs(target_dir)

#images list in source directory
source_imgs_list = os.listdir(source_dir)
print source_imgs_list

#for each image in the images list
for source_img_name in source_imgs_list:
    if '.jpg' in source_img_name:
        print(source_img_name)

        #read images
        path_source_img = os.path.join(source_dir, source_img_name)
        src_img = Image.open(path_source_img)
        #src_img.show()

        #---------------------here need to be changed---------rename--------
        target_img_name=source_img_name.replace('.jpg','_real_A.png')
        path_target_img=os.path.join(target_dir, target_img_name)
        print(path_target_img)
        #save new reanmed img to the target dir
        src_img.save(path_target_img)










