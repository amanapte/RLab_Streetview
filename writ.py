from __future__ import division

import math
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

from keras.preprocessing.image import Iterator
from keras.utils.np_utils import to_categorical
import keras.backend as K

def save_image(o,r,c,i,di):
    f_name="orig"+str(i)+".jpg"
    os.chdir(di+"/Output/Orig")
    o=cv2.cvtColor(o, cv2.COLOR_RGB2BGR)
    cv2.imwrite(f_name,o)

    f_name="rotated"+str(i)+".jpg"
    os.chdir(di+"/Output/Rotated")
    r=cv2.cvtColor(r, cv2.COLOR_RGB2BGR)
    cv2.imwrite(f_name,r)

    f_name="correct"+str(i)+".jpg"
    os.chdir(di+"/Output/Corrected")
    c=cv2.cvtColor(c, cv2.COLOR_RGB2BGR)
    cv2.imwrite(f_name,c)
    
    os.chdir(di)
