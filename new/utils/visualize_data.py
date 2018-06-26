'''
    File name: visualize_data.py
    Author: Ajeet Yadav
    Date created: 6/17/2018
'''

import matplotlib.pyplot as plt
import numpy as np
import cv2

def displayVideo(path, nth_frame):
    cap = cv2.VideoCapture(path)
    if cap.isOpened() is False:
        print('Error opening video file '+str(path))
    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if frame_count%nth_frame == 0:
            if ret is True:
                cv2.imshow("Video",frame)
                if cv2.waitKey(25) & 0xFF == 27:
                    break
            else:
                break
        frame_count+=1
        
def displayImages(images, rows = 5, columns=5):
    plt.figure(figsize=(20,10))
    max_images = rows * columns;
    step = int(len(images)/max_images)
    image_list = np.arange(0,len(images),step)
    i=0
    for idx in image_list:
        plt.subplot(max_images / columns + 1, columns, i+1)
        plt.imshow(images[idx])
        i+=1
        
def plotFramesPerVideo(*argv):
    frames_per_video = []
    for arg in argv:
        frames_per_video.append(arg)
    video_number= ['tool_video_01', 'tool_video_02', 'tool_video_03', 'tool_video_04', 'tool_video_05', 'tool_video_06',\
                   'tool_video_07', 'tool_video_08', 'tool_video_09', 'tool_video_10']
    width = 1/1.5
    fig, ax=plt.subplots(figsize=(7,8))
    plt.bar(video_number, frames_per_video, width, color="orange")
    plt.xticks(video_number, rotation='vertical')
    plt.title('Number of frames to train per video')
    plt.ylabel('number of frames')
    plt.xlabel('tool video number')
    rects = ax.patches
    for rect, value in zip(rects,frames_per_video):
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height + 5, value, ha='center', va='bottom')
        
def plotToolsPresence(tool_video_df, number_of_frames_video, title='tool_video'):
    fig, axes = plt.subplots(nrows=4, ncols=2, figsize=(20,20))
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.5)
    fig.suptitle(title, fontsize=16)
    tool_video_df.plot(ax=axes[0,0], x='Frame', y ='Grasper'); axes[0,0].set_title('Grasper');
    tool_video_df.plot(ax=axes[0,1], x='Frame', y ='Bipolar'); axes[0,1].set_title('Bipolar');
    tool_video_df.plot(ax=axes[1,0], x='Frame', y ='Hook'); axes[1,0].set_title('Hook');
    tool_video_df.plot(ax=axes[1,1], x='Frame', y ='Scissors'); axes[1,1].set_title('Scissors');
    tool_video_df.plot(ax=axes[2,0], x='Frame', y ='Clipper'); axes[2,0].set_title('Clipper');
    tool_video_df.plot(ax=axes[2,1], x='Frame', y ='Irrigator'); axes[2,1].set_title('Irrigator');
    tool_video_df.plot(ax=axes[3,0], x='Frame', y ='SpecimenBag'); axes[3,0].set_title('SpecimenBag');
    tool_video_present = [tool_video_df['Grasper'].sum(), tool_video_df['Bipolar'].sum(), tool_video_df['Hook'].sum(),\
                             tool_video_df['Scissors'].sum(), tool_video_df['Clipper'].sum(),\
                             tool_video_df['Irrigator'].sum(), tool_video_df['SpecimenBag'].sum()]
    tool_video_not_present = np.subtract(number_of_frames_video,tool_video_present)
    tool_names = ['Grasper', 'Bipolar', 'Hook', 'Scissors', 'Clipper', 'Irrigator', 'SpecimenBag']
    x_axis = np.arange(len(tool_names))
    x_axis_1 = [x+0.25 for x in x_axis]
    bar1 = plt.bar(x_axis, tool_video_present, width=0.25, color="green")
    bar2 = plt.bar(x_axis_1, tool_video_not_present, width=0.25, color="red")
    plt.legend(['present', 'not present'], loc='upper left')
    plt.xticks(x_axis,tool_names, rotation='vertical')
    plt.ylabel('Number of frames')
    for rect in bar1+bar2:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height + 5, '%d' % int(height), ha='center', va='bottom')
    return tool_video_present, tool_video_not_present
        
def plotPercentageOfToolPresence(tool_video_present, number_of_frames_video, title = 'tool_video'):
    percentage_presence_tool_video = np.divide(tool_video_present,number_of_frames_video)
    tool_names = ['Grasper', 'Bipolar', 'Hook', 'Scissors', 'Clipper', 'Irrigator', 'SpecimenBag']
    x_axis = np.arange(len(tool_names))
    plt.plot(x_axis, percentage_presence_tool_video, marker='o', color ='orange')
    plt.xticks(x_axis,tool_names, rotation='vertical')
    for i,j in zip(x_axis,percentage_presence_tool_video):
        plt.annotate(str(round((j*100),2))+'%',xy=(i,j))
    plt.xlabel('Tools')
    plt.ylabel('Percentage of precence')
    plt.title('Percentage of precence of each tool in '+ title)
    plt.grid()
    return percentage_presence_tool_video
    
def plotCombinedPercentageOfToolPresence(percentage_presence_tool_video_list, colors, legend_list, tool_video_present_list, total_number_of_frames):
    fig, axes = plt.subplots(nrows=1, ncols=2, sharey=True, figsize=(15,7))
    fig.suptitle('Tools presence percentage', fontsize=16)
    tool_names = ['Grasper', 'Bipolar', 'Hook', 'Scissors', 'Clipper', 'Irrigator', 'SpecimenBag']
    x_axis = np.arange(len(tool_names))
    plt.subplot(121)
    for pptv, clr in zip(percentage_presence_tool_video_list, colors):
        plt.plot(x_axis, pptv*100, marker='o', color =clr)
    plt.legend(legend_list)
    plt.xlabel('Tools')
    plt.ylabel('Percentage')
    plt.title('percentage of tool presence in each video')
    plt.xticks(x_axis,tool_names, rotation='vertical')
    plt.grid()
    ## for all videos
    tool_present_in_all_videos = [sum(x) for x in zip(*tool_video_present_list)]
    percentage_presence_of_tool_in_all_videos = np.divide(tool_present_in_all_videos,total_number_of_frames) * 100
    plt.subplot(122)
    plt.plot(x_axis, percentage_presence_of_tool_in_all_videos, marker='x', color ='red')
    plt.legend(['tools in all videos'])
    plt.xlabel('Tools')
    plt.ylabel('Percentage')
    plt.title('percentage of tool presence in all videos')
    plt.xticks(x_axis,tool_names, rotation='vertical')
    for i,j in zip(x_axis,percentage_presence_of_tool_in_all_videos):
        plt.annotate(str(round(j,2))+'%',xy=(i,j))
    plt.grid()
    return percentage_presence_of_tool_in_all_videos
    

