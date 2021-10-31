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


## 1. detection under ideal condition
This project started by realizing the tracking mission under ideal condition. We applied two basic methods to realize the detection of table tennis table and ball in the game environment.

### Color tracking
Run the file ‘1_1_Color_tracking .py’ to see that, in the game environment, color tracking can almost completely identify where are the ball and the table. At the same time, we record the coordinates of ball position and movement direction in each frame.
 ![image](https://github.com/blisstia/UE1_Advanced-Programming-table-tennis/blob/main/Documents/demo1.gif)
 
### Hough circle tracking
Run the file ‘1_2_Hough circle tracking.py’ to see that, in the game environment, the method of Hough circle tracking is less precise and powerful comparing with the first way. Approximately 38% of the coordinates of the ball's position can be correctly detected, then we also record the coordinates of ball position and movement direction in each frame.
 ![image]( https://github.com/blisstia/UE1_Advanced-Programming-table-tennis/blob/main/Documents/demo2.gif)
 
### Creation of database
Run the file ‘1_3_Creation of database.py’ to create a database in the format of CSV to contain all the information that we’ve recorded above to facilitate our possible analysis.

### Adaptation to reality
Run the file ‘1_4_Adaptation to reality.py’, we tried to adapt the tracking to a wider and more realistic table tennis match, and obviously, some issues raised:
1. Under more complicated lighting and background colors, the accuracy of detection cannot be guaranteed.
2. It is not possible to detect players in the game environment, while the detection of rackets and players is also of great value for possible analysis.

Therefore, we need to improve our project to improve these two problems.

## 2. extract images
This stage2 is to extract all the images in the test video for subsequent detection, after running '2_extract_images.py' you will get 7484 images in the imges folder. 

The limitation is that a lot of useless pictures will be intercepted, we are only use a small test video here, however if we want to realise all the machine learning process, We will need a lot of videos for mass crawling. Therefore, we provided the solution to run the code by GBU If the computer environment is feasible, meanwhile, in ordre to optimise our exact method, We originally wanted to use the smooth lab method, but the optimization conditions are limited here and have not been completed for the time being.

## 3. detect images
Here we use the yolov5 model to achieve video detection, and when asked to identify different categories of items by the classfication in the model. 

'3_1_detect_all.py' is in the case of all recognition by using yolov5s model, we can see that it deteced all persons, ball(sometimes), racket and chair, etc.


'3_2_detect_onlyball.py' is in the case of only detect the pingpong ball, but we can see that ping pong balls are recognized very rarely and yolov5 model could impove the recognsition if we'd like to optimise our detect results.


'3_3_detect_classes.py' is in the case that we want to detect person, racket and ball in ordre to the possibility of a more comprehensive analysis.

## 4. demo
We provided the code for making demo here (from detect images to video), please run 4_make_demo.py if needed.

## 5. train
As we said. yolov5 model regonise rarely the pingpong ball and we would like to train the yolo model to better recognize table tennis. However, We have encountered some difficulties with the original data of the training model. Hence, we assume that we can start part of the code with the labeled data, but it is not completed and is being continuously updated.

'5_1_voc_lab.py' is to transfes xml data to txt for the labeled data,'5_2_train_test_spllit.py ' is to set training conditions.
The problem here is still the manually marked file. Maybe lablimg(Software for manually identifying table tennis) is helpful here, however, due to the huge manual processing and marking work we've done it here temporarily



