
# coding: utf-8

import os
from nibabel.testing import data_path
import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt
import cv2
import sys 



#"liverseg-2017-nipsws/LiTS_database/liver_seg/"
RESULTS_PATH = "liverseg-2017-nipsws/results/seg_liver" # seg_liver_ck


for folder_no in os.listdir(RESULTS_PATH):
    path = os.path.join(RESULTS_PATH,folder_no)
    
    max_channel = max([int(idx[:-4]) for idx in os.listdir(path)])
    img_volume = np.zeros((512,512,max_channel+1))
    
    for img in os.listdir(path):
        idx = int(img[:-4])
        
        img = np.load(os.path.join(path,img))
        img_volume[:,:,idx] = img
        
    np.save("liverseg-2017-nipsws/results/output_volumes/"+folder_no+".npy",img_volume)

