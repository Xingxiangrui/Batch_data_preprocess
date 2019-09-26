# -*- coding: utf-8 -*
"""
Created by Xingxiangrui on 2019.4.8
This code is created to augment pix2pix image pairs by rotate
"""

#import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import os

#image source directory
#---------------------here need to be changed---------dir location---------
source_dir="/Users/Desktop/trainingSet/pired-images/lambda_10_idt_0.5/tear/"
target_dir="/Users/Desktop/trainingSet/pired-images/lambda_10_idt_0.5/tear/augmented-tear/"
if not os.path.isdir(target_dir):
    os.makedirs(target_dir)

#images list in source directory
source_imgs_list = os.listdir(source_dir)
print source_imgs_list

#for each image in the images list
for source_img_name in source_imgs_list:
    if '.png' in source_img_name:
        print(source_img_name)

        #read images
        path_source_img = os.path.join(source_dir, source_img_name)
        src_img = Image.open(path_source_img)  # 读取的图像显示的<matplotlib.image.AxesImage object at 0x7f9f0c60f7f0>
        #src_img.show()

        #rotate 0
        rotated_img = src_img.rotate(0)
        #---------------------here need to be changed---------prefix--------
        target_img_name="tear_r0_"+source_img_name
        path_target_img=os.path.join(target_dir, target_img_name)
        print(path_target_img)
        rotated_img.save(path_target_img)
        # rotate 90
        rotated_img = src_img.rotate(90)
        target_img_name="tear_r90_"+source_img_name
        path_target_img=os.path.join(target_dir, target_img_name)
        print(path_target_img)
        rotated_img.save(path_target_img)
        # rotate 180
        rotated_img = src_img.rotate(180)
        target_img_name="tear_r180_"+source_img_name
        path_target_img = os.path.join(target_dir, target_img_name)
        print(path_target_img)
        rotated_img.save(path_target_img)
        # rotate 270
        rotated_img = src_img.rotate(270)
        target_img_name="tear_r270_"+source_img_name
        path_target_img = os.path.join(target_dir, target_img_name)
        print(path_target_img)
        rotated_img.save(path_target_img)









