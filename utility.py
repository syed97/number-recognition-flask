import numpy as np
import cv2
import imutils

def transform_raw_image(img_data):
    '''
    Takes in a bytes object representing an image and applies the necessary 
    transformations on it for use in the prediction algorithm
    '''
    np_im = np.frombuffer(img_data, dtype=np.uint8)
    img = cv2.imdecode(np_im, flags=0)
    img = imutils.resize(img, width=28, height=28)
    img = cv2.bitwise_not(img) # invert color scheme, black bg for mnist data format
    img = img.reshape(1, 784) # reshape 28 x 28 matrices into 784-length vectors.
    img = img.astype('float32')   # change integers to 32-bit floating point numbers
    img /= 255 # normalize to bw 0 and 1
    return img
