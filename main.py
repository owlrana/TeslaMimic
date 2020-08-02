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
