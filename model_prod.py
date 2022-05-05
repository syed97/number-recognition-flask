from keras.models import load_model
import numpy as np
import imutils
import cv2

def predict_digit(img):
    '''
    Takes in image data, transformed for input to CNN. Loads the saved CNN model and 
    applies it to the inpuit data to return the predicted digit value and accuracy
    '''
    model = load_model('my_model.h5')
    # array of predicted model probabilities
    pred_arr = model.predict(img)[0] 
    # prediction proability as percentage accuracy
    accuracy = round(max(pred_arr), 5)
    percentage_accuracy = round(accuracy * 100, 3)
    percentage_accuracy = "{}".format(percentage_accuracy)
    # prediction value
    pred = np.where(pred_arr == max(pred_arr))[0][0]
    print("predict_digit ---------------------------")
    print({
        "predicted_value" : str(pred),
        "predicton_accuracy" : str(percentage_accuracy)
    })
    return {
        "predicted_value" : str(pred),
        "predicton_accuracy" : str(percentage_accuracy)
    }
