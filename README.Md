# Handwritten Digits Classifier

## This model uses three hidden layers.
## Rectified Linear, Softmax activaition functions are used along with sparse_categorical_crossentropy for loss, and Adam as the optimizer in backpropagation
## 
## The input layer has 28 * 28 tensor and output layer is a vector with 10 elements as highest value's index gives the predicted number

# To use this in local machine. Install the necessary packages first
### pip3 install tensorflow
### pip3 install numpy
### pip3 install opencv-python

## You can train the model yourself in local machine with the command:
### python3 model.py
##### You must be in the same directory with model.py to run.
## You can use the GUI to interact with the model with command:
### python3 main.py
## If you don't want GUI you can directly pass images for prediction with command:
### python3 test.py imagepath.jpg

###### The model does a preety bad job at prediction. The the model still has to be improved a lot.