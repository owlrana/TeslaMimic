import matplotlib.pyplot as plt

import numpy as np
import cv2
import os
import matplotlib.image as mpimg
from moviepy.editor import VideoFileClip
import math

#I am confortable with Adobe After Effects, I made a script to remove portions of videos I do not want, then filtered video using frame masking here
def interested_region(img, vertices):
    if len(img.shape) > 2: 
        mask_color_ignore = (255,) * img.shape[2]
    else:
        mask_color_ignore = 255
        
    cv2.fillPoly(np.zeros_like(img), vertices, mask_color_ignore)
    return cv2.bitwise_and(img, np.zeros_like(img))

#conversion of pizels into line; Hough Transform Spce
def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):
    lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]), minLineLength=min_line_len, maxLineGap=max_line_gap)
    line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    lines_drawn(line_img,lines)
    return line_img

#create two lines in each frame after Hough T
def lines_drawn(img, lines, color=[255, 0, 0], thickness=6):
    global cache
    global first_frame
    slope_l, slope_r = [],[]
    lane_l,lane_r = [],[]
    α =0.2 
  for line in lines:
        for x1,y1,x2,y2 in line:
            slope = (y2-y1)/(x2-x1)
            if slope > 0.4:
                slope_r.append(slope)
                lane_r.append(line)
            elif slope < -0.4:
                slope_l.append(slope)
                lane_l.append(line)
        img.shape[0] = min(y1,y2,img.shape[0])
    if((len(lane_l) == 0) or (len(lane_r) == 0)):
        print ('no lane detected')
        return 1
    slope_mean_l = np.mean(slope_l,axis =0)
    slope_mean_r = np.mean(slope_r,axis =0)
    mean_l = np.mean(np.array(lane_l),axis=0)
    mean_r = np.mean(np.array(lane_r),axis=0) # currently not working, space is empty
