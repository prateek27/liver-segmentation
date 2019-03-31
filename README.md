# liver-segmentation
LiTs Challenege Semantic Segmentation of Liver from CT Scans

# Steps To Set Up

- **Clone The Repository** 
https://github.com/imatge-upc/liverseg-2017-nipsws  
Put in inside the current directory as shown here.
Replace the 'seg_liver.py', 'seg_liver_train.py', seg_liver.py' files inside the cloned repository by the files provided here.

- Create a Folder 
  - LiTS_database inside liverseg folder.
  -  create a results folder insider liverseg folder
  - Download the weights from [here](https://drive.google.com/file/d/1pBfXQgCp-KxUBs9fYX7kB2mfpZHE-b10/view?usp=sharing) and add them to train_files folder.

  
# Steps To Get Predictions

- **Process NIFTI Files**
`python process_test_database.py dataset_folder_name`  
Input - ‘volume_i_.nii’ files from the dataset_folder  
Output - ‘/LiTS_database/test_image_volumes/’   
 
- **Create a File Containing Path to Test Images**
`python Create_test.py test_image_volumes`  
Input - "liverseg-2017-nipsws/LiTS_database/folder_name"
Output - liverseg-2017-nipsws/seg_DatasetList/test.txt  


- **Test the Trained Model** 
Download the weights from [here](https://drive.google.com/file/d/1pBfXQgCp-KxUBs9fYX7kB2mfpZHE-b10/view?usp=sharing) 

`python  liverseg-2017-nipsws/seg_liver_test.py`
Input - ‘seg_DatasetList/test.txt'  
Output - ‘liverseg-2017-nipsws/results’  

**Convert Multile Images Slices into a 3D Volume**
`python npy_2_volume.py`

Converts multiple .npy output slices into a single .npy volume for a particular case. 
Input - "liverseg-2017-nipsws/results/seg_liver"  
Output - “liverseg-2017-nipsws/results/output_volumes/”
