import numpy as np
import tensorflow as tf
from tensorflow import keras

# for loading and processing images 
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# CNN model organisation: models, layers, metrics, optimizers  
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam, Adamax
from tensorflow.keras.metrics import binary_crossentropy
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Activation, Dropout

# data preparation 

# setting parameters 

# training 

# saving the best model 