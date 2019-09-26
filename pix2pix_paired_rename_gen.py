# -*- coding: utf-8 -*
"""
Created by Xingxiangrui on 2019.4.9
This code is created to make pix2pix image pairs to
folder A and B with the same filename
"""
#import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import os

#iamge paths
#------------here need to be changed--------source image dir--------------------
dir_paired_images="/Users/Desktop/trainingSet/pired-images/lambda_10_idt_0.5/tear/augmented-tear/"
dir_train_A="/Users/Desktop/trainingSet/pix2pix-nor2cott/A/train/"
dir_train_B="/Users/Desktop/trainingSet/pix2pix-nor2cott/B/train/"

#for each image
paired_imgs_list = os.listdir(dir_paired_images)
print paired_imgs_list
for source_image_name in paired_imgs_list:
    if '.png' in source_image_name:
        path_source_img = os.path.join(dir_paired_images, source_image_name)
        src_img = Image.open(path_source_img)
        # ------------here need to be changed------iamge filename prefix-------------------
        full_image_name="lam10_"+source_image_name
        # fake B in /B/train
        if '_fake_B' in full_image_name:
            target_image_name=full_image_name.replace('_fake_B','')
            path_train_B=os.path.join(dir_train_B, target_image_name)
            print(path_train_B)
            src_img.save(path_train_B)
        # real_A in /A/train
        if '_real_A' in full_image_name:
            target_image_name = full_image_name.replace('_real_A', '')
            path_train_A = os.path.join(dir_train_A, target_image_name)
            print(path_train_A)
            src_img.save(path_train_A)



















