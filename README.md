# liver-segmentation
LiTs Challenege Semantic Segmentation of Liver from CT Scans

# Steps To Get Predictions

- Process NIFTI Files
`python process_test_database.py dataset_folder_name`
Input - ‘volume_i_.nii’ files from the dataset_folder
Output - ‘/LiTS_database/test_image_volumes/’
 
- Create a File Containing Path to Test Images
`python Create_test.py test_image_volumes`

Input - "liverseg-2017-nipsws/LiTS_database/folder_name"

Output - liverseg-2017-nipsws/seg_DatasetList/test.txt

- Test the Trained Model 

`python  liverseg-2017-nipsws/seg_liver_test.py`
Input - ‘seg_DatasetList/test.txt'
Output - ‘liverseg-2017-nipsws/results’

- Convert Multiplce Images Slices into a 3D Volume
`python npy_2_volume.py`

Converts multiple .npy output slices into a single .npy volume for a particular case.
Input - "liverseg-2017-nipsws/results/seg_liver"
Output - “liverseg-2017-nipsws/results/output_volumes/”
