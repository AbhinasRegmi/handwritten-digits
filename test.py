#! /usr/bin/python3

#here we will use custom images to classify them with our neural network

import tensorflow as tf
import numpy as np
import sys
import cv2

#warning!! the input data should be a matrix with 784 elements as grey scale values

#load the model
trainedModel = tf.keras.models.load_model('Assets')


def locateImage(imgpath):
    #location to the image
    img = cv2.imread(imgpath, cv2.IMREAD_GRAYSCALE)

    #now resize the image
    dim = (28, 28)

    imgResize = cv2.resize(img, dim)

    imgResize =  255 - imgResize

    #convert the input image to a matrix suitable for feeding to the network
    data_arr = []

    data_arr.append(imgResize)

    data = tf.keras.utils.normalize(data_arr, axis=1)

    prediction = np.argmax(trainedModel.predict(data), axis=1)

    print(f"\nThe predicted number is {prediction[0]}\n")


if __name__ == '__main__':

    if len(sys.argv) != 2:
            print("Please give path to a image..")
            exit()

    imgLocation = sys.argv[1]
    locateImage(imgLocation)