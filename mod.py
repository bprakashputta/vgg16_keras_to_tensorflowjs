# /Users/bprakashputta/Library/Python/3.8/bin

import os
os.chdir(os.path.dirname('/Users/bprakashputta/Library/Python/3.8/bin'))
import tensorflowjs as tfjs
import keras

vgg16 = keras.applications.vgg16.VGG16()
tfjs.converters.save_keras_model(vgg16, 'data/tfjs-models/VGG16')
