import cv2

filepath = 'data/m2cai16-tool/train_dataset/tool_video_01.mp4'

cap = cv2.VideoCapture(filepath)
print(cap.isOpened())