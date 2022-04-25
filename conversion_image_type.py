#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 22:14:40 2022

@author: lw19
"""


import SimpleITK as sitk
import numpy as np 
import nibabel as nb


#### Load gifti image using nibabel ####
filename = '' ### Participant to modify
image = nb.load(filename)

#### Define number of channels in gifti ####
channels=4 ### Each channel represents a structural cortical metric (myelin, curvature, cortical thickness and sulcal depth - in that order) 

img_array=[]


#### Iterate over each channel, extract array and append to img_array object/list ####  
for i in range(channels):
    array = image.darrays[i].data
    img_array.append(array)


#### Swap axes so that img_array dim is 40962,4 - this will depend on how participants want to work with the image arrays #### 
img_array = np.swapaxes(img_array, 0,1) 


#### Create .mha image using sitk ####
mha_img = sitk.GetImageFromArray(img_array)

new_filename='' ### Participant to modify

#### Write out .mha image ####
sitk.WriteImage(mha_img, new_filename)

#### Read in .mha image again ####
mha_img1 = sitk.ReadImage(new_filename)


#### Get array from image using sitk ####
img1_array = sitk.GetArrayFromImage(mha_img1)
