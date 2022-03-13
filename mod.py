# /Users/bprakashputta/Library/Python/3.8/bin

import os
os.chdir(os.path.dirname('C:/python'))
import tensorflowjs as tfjs
import keras

vgg16 = keras.applications.vgg16.VGG16()
vgg16.loss
tfjs.converters.save_keras_model(vgg16, 'data/tfjs-models/VGG16')
