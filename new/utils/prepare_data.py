'''
    File name: prepare_data.py
    Author: Ajeet Yadav
    Date created: 6/17/2018
'''

import numpy as np
import cv2
import os
import h5py
import pandas as pd

def video2frame(filepath, filename, path, nth_frame=25):
    cap = cv2.VideoCapture(path)
    if cap.isOpened() is False:
        print('Error opening video file '+str(filename))
    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if frame_count%nth_frame == 0:
            if ret is True:
                frame_name = filename+'_'+str(frame_count)
                frame_path = os.path.join(filepath,frame_name+'.'+'jpg')
                cv2.imwrite(frame_path,frame)
            else:
                break
        frame_count+=1
                
def loadImages(filepath):
    images = []
    for filename in os.listdir(filepath):
        img = cv2.imread(os.path.join(filepath, filename))
        if img is not None:
            images.append(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    return images

def resizeImages(images, width=224, height=224):
    new_images = []
    for image in images:
        new_image = cv2.resize(image,(width,height), interpolation = cv2.INTER_LINEAR)
        new_images.append(new_image)  
    data_set_X = np.stack(new_images, axis=0)
    return data_set_X

def readTextFile(filepath, filename):
    return pd.read_table(os.path.join(filepath, filename+'.txt'), delim_whitespace=True)
    
def getCombinedDataFrames(*argv):
    data_frames = []
    for arg in argv:
        data_frames.append(arg)
    data_set_y = pd.concat(data_frames)
    data_set_y.drop('Frame',1,inplace=True)
    data_set_y = np.array(data_set_y)
    return data_set_y

def saveData(filepath, filename, data_set_X, data_set_y, data_type = 'training'):
    with h5py.File(os.path.join(filepath,filename),'w') as hdf:
        if data_type == 'training':
            hdf.create_dataset('train_set_X', data=data_set_X)
            hdf.create_dataset('train_set_y', data=data_set_y)
        else:
            hdf.create_dataset('test_set_X', data=data_set_X)
            hdf.create_dataset('test_set_y', data=data_set_y)
            
def loadData(filepath, filename, data_type='training'):
    path = os.path.join(filepath,filename)
    if data_type == 'training':
        train_dataset = h5py.File(path, 'r')
        data_set_X_orig = np.array(train_dataset["train_set_X"][:])
        data_set_y_orig = np.array(train_dataset["train_set_y"][:])
    else:
        test_dataset = h5py.File(path, 'r')
        data_set_X_orig = np.array(test_dataset['test_set_X'][:])
        data_set_y_orig = np.array(test_dataset['test_set_y'][:])
    return data_set_X_orig, data_set_y_orig