#! /usr/bin/python3

from matplotlib.pyplot import axis
import tensorflow as tf

mnist = tf.keras.datasets.mnist  #28 * 28 tensor containg image data as numbers between 0, 255

#distribute the total data in test and train
(trainX, trainy), (testX, testy) = mnist.load_data()

#we will normalize the data between 0, 1
trainX = tf.keras.utils.normalize(trainX, axis=1)
testX = tf.keras.utils.normalize(testX, axis=1)

#building the actual model
#model with feed forward network

model = tf.keras.models.Sequential()

#we need to flatten the input because a single image will be passed
#as a single vector in the input layer
model.add(tf.keras.layers.Flatten())

#now the actual neuron layers
#there will be 128 inputs , 128 output and the activation function to use is RectifiedLinear
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))

#for the second layer with 128 output
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))

#for our output we will have softmax as our activation function to spit out
#the  probability distribution for our 10 digits
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))

#the forward pass is almost done
#we will need the loss function  and also the optimizer
model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

model.fit(trainX, trainy, epochs=3)

model.save('Assets')

val_loss, val_acc = model.evaluate(testX, testy)