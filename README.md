# UE1_Advanced-Programming-table-tennis

>├── dataset  
>>├── test  
>>>├── demo_images  
>>>├── images  
>>>├── videos  
>>>>├── Pingpong.mp4  
>>>>├── test_1.mp4  
>>>>├── test.mp4  
            
>├── dataset_train  
>>├── Annotations  
>>├── Images  
>>├── ImageSets  
>>>├── Main  

...  

>├── 0_prepare_dataset.py  
>├── 1_1_color tracking .py  
>├── 1_2_hough circle tracking.py  
>├── 1_3_creation of database.py  
>├── 1_4_adaptation to reality.py   
>├── 2_extract_images.py  
>├── 3_1_detect_all.py  
>├── 3_2_detect_onlyball.py  
>├── 3_3_detect_classes.py  
>├── 4_make_demo.py  
>├── 5_1_voc_lab.py  
>├── 5_2_train_test_spllit.py  

>├── README.md  


### Tip: Please download and unzip the yo lov5 package first, then put all the python files into the yolov5 folder to run.


## Prepare dataset
Please download the video file from the following link after running '0_prepare_dataset.py' and put it in this path:  

'../dataset/test/videos/' (you need to pay attention to the path of the floder of youlov5)

link:
https://drive.google.com/drive/folders/14szmzVKyERyuCk3bkHPh1rVtuXtgg4IM?usp=sharing


## 1 Detection under Ideal condition
This project started by realizing the tracking mission under ideal condition. We applied two basic methods to realize the detection of table tennis table and ball in the game environment.

### Color tracking
Run the file ‘1_1_Color_tracking .py’ to see that, in the game environment, color tracking can almost completely identify where are the ball and the table. At the same time, we record the coordinates of ball position and movement direction in each frame.
 
### Hough circle tracking
Run the file ‘1_2_Hough circle tracking.py’ to see that, in the game environment, the method of Hough circle tracking is less precise and powerful comparing with the first way. Approximately 38% of the coordinates of the ball's position can be correctly detected, then we also record the coordinates of ball position and movement direction in each frame.
 
### Creation of database
Run the file ‘1_3_Creation of database.py’ to create a database in the format of CSV to contain all the information that we’ve recorded above to facilitate our possible analysis.

### Adaptation to reality
Run the file ‘1_4_Adaptation to reality.py’, we tried to adapt the tracking to a wider and more realistic table tennis match, and obviously, some issues raised:
1. Under more complicated lighting and background colors, the accuracy of detection cannot be guaranteed.
2. It is not possible to detect players in the game environment, while the detection of rackets and players is also of great value for possible analysis.

Therefore, we need to improve our project to improve these two problems.


## 2 Extract images
This stage2 is to extract all the images in the test video for subsequent detection, after running '2_extract_images.py' you will get 7484 images in the imges folder. 

The limitation is that a lot of useless pictures will be intercepted, we are only use a small test video here, however if we want to realise all the machine learning process, We will need a lot of videos for mass crawling. Therefore, we provided the solution to run the code by GBU If the computer environment is feasible, meanwhile, in ordre to optimise our exact method, We originally wanted to use the smooth lab method, but the optimization conditions are limited here and have not been completed for the time being.
