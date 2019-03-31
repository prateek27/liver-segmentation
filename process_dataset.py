import os
from nibabel.testing import data_path
import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt
import cv2

## Read .nii files and creates 3 folders 
import sys


# Read .nii Files from here
niftis_path = sys.argv[1] #'./Dataset/media/nas/01_Datasets/CT/LITS/Training Batch 2/'

# Write Database here
root_process_database = sys.argv[2] #'./LiTS_database/'

folder_volumes = os.path.join(root_process_database, 'images_volumes/')
folder_seg_liver = os.path.join(root_process_database, 'liver_seg/')
folder_seg_item = os.path.join(root_process_database, 'item_seg/')

#Create Directories if they don't exist
if(not os.path.isdir(folder_volumes)):
    os.mkdir(folder_volumes)

if(not os.path.isdir(folder_seg_liver)):
    os.mkdir(folder_seg_liver)

if(not os.path.isdir(folder_seg_item)):
    os.mkdir(folder_seg_item)
    
files_dir = (niftis_path)
copy_files_dir = files_dir
filenames = []
list_file_names = []

os.listdir(files_dir)

#Iterate in Batch Folder
for f in os.listdir(files_dir):
    if(f.endswith(".nii")):
        filenames.append(f)

        
for l in filenames:
    
    
    if(l[0]=='v'):
       
        path_file = os.path.join(niftis_path,l)
        idx = l.index('-')
        folder_volume = os.path.join(folder_volumes,l[idx+1:-4])
        #print(folder_volume)
        volume = nib.load(path_file)
        print("Processing Volume %s and saving at %s"%(l,folder_volume))
        #print(volume.dataobj.shape)
        imgs = volume.dataobj
        imgs = np.array(imgs).astype('float32')
        imgs[imgs<-150] = -150
        imgs[imgs>250] = 250
        #print(imgs.shape)
        #print(imgs.min(axis=(0,1)).shape)
        
        img_volume = 255*(imgs - imgs.min(axis=(0,1)))/(imgs.max(axis=(0,1))-imgs.min(axis=(0,1)))
        if(not os.path.isdir(folder_volume)):
            os.mkdir(folder_volume)
        #Iterate over image channels
        for section_id in range(imgs.shape[-1]):
            pass
            section_filename = os.path.join(folder_volume,str(section_id)+".npy")
            np.save(section_filename,img_volume[:,:,section_id])
        

        
        
    
    elif(l[0]=='s'):
        #this part will not be executed
        print("Processing Segmentation %s"%l)
        path_file = os.path.join(niftis_path, l)
        index = l.index('-')
        folder_seg_item_num = os.path.join(folder_seg_item, l[index+1:-4])
        folder_seg_liver_num = os.path.join(folder_seg_liver,l[index+1:-4])
        segmentation = nib.load(path_file)
        
    
        img_seg = np.array(segmentation.dataobj).astype('uint8')
        img_seg_item = np.copy(img_seg)
        img_seg_liver = np.copy(img_seg)
        
        
        #plt.imshow(img_seg[:,:,-20],cmap='gray')
        #plt.show()
        
        #Binary Classification
        img_seg_item[img_seg_item==1]=0
        img_seg_item[img_seg_item==2]=1
        
        #Treat tumour pixels as liver mass
        img_seg_liver[img_seg_item==1]=1
        
        #actually a liver
        img_seg_liver[img_seg_liver==2]=1
        
        
    
        #Create Directory for Lesions
        if not os.path.isdir(folder_seg_item_num):
            os.mkdir(folder_seg_item_num)
            
        #Create Directory for Liver
        if not os.path.isdir(folder_seg_liver_num):
            os.mkdir(folder_seg_liver_num)
         
        
        for j in range(img_seg.shape[-1]):
            
            item_seg_section = img_seg_item[:,:,j]*255
            liver_seg_section = img_seg_liver[:,:,j]*255
            filename_for_seg_item_section = os.path.join(folder_seg_item_num, str(j)+'.png')
            filename_for_seg_liver_section = os.path.join(folder_seg_liver_num,str(j)+'.png')
            cv2.imwrite(filename_for_seg_item_section,item_seg_section)
            cv2.imwrite(filename_for_seg_liver_section,liver_seg_section)
           
            