import os
import random

'''Our plan here is to use the generated xml file containing the coordinates and put it in the main folder. 
The problem here is still the manually marked file. Maybe lablimg is helpful here, 
however, due to the huge manual processing and marking work , 
Do it here temporarily '''

trainval_percent = 2 #Validation set ratio
'''here, 80% of the pictures are the training set and 20% of the pictures are the validation set'''
train_percent = 1
xmlfilepath = '/Users/tia/Desktop/UE1_projet/dataset_train/Annotations'
txtsavepath = '/Users/tia/Desktop/UE1_projet/dataset_train/ImageSets/Main'
total_xml = os.listdir(xmlfilepath)

num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

# ftrainval = open('ImageSets/Main/trainval.txt', 'w')
ftest = open('./data/ImageSets/Main/test.txt', 'w')
ftrain = open('./data/ImageSets/Main/train.txt', 'w')
# fval = open('ImageSets/Main/val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        # ftrainval.write(name)
        if i in train:
            ftest.write(name)
        # else:
        # fval.write(name)
    else:
        ftrain.write(name)

# ftrainval.close()
ftrain.close()
# fval.close()
ftest.close()
