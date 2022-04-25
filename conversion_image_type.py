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
image = nb.load('/data/Data/data_release_gDL_benchmarking/Data/Regression/Native_Space/regression_native_space_features/sub-CC00051XX02_ses-7702_L.shape.gii')

#### Define number of channels in gifti ####
channels=4

img_array=[]


#### Iterate over each channel, extract array and append to img_array object/list ####  
for i in range(channels):
    array = image.darrays[i].data
    img_array.append(array)


#### Swap axes so that img_array dim is 40962,4 #### 
img_array = np.swapaxes(img_array, 0,1)


#### Create .mha image using sitk ####
mha_img = sitk.GetImageFromArray(img_array)

#### Write out .mha image ####
sitk.WriteImage(mha_img,'/home/sd20/workspace/SLCN_algorithm/test/sub-CC01215XX111_ses-14633_L.mha')

#### Read in .mha image again ####
mha_img1 = sitk.ReadImage('/home/sd20/workspace/SLCN_algorithm/test/sub-CC01215XX111_ses-14633_L.mha')


#### Get array from image using sitk ####
img1_array = sitk.GetArrayFromImage(mha_img1)
