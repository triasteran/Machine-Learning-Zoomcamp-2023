import numpy as np

import tensorflow as tf
from tensorflow import keras

from keras.models import Sequential

from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Activation, Dropout, BatchNormalization
from tensorflow.keras import regularizers


# Input and data preprocessing

train_gen = ImageDataGenerator(rescale=1./255)

train_ds = train_gen.flow_from_directory(
    '/home/alla/ML/CapstoneProject1/archive/C-NMC_Leukemia/training_data/fold_0/',
    target_size=(150, 150),
    batch_size=20,
    shuffle=True,  class_mode='binary'
)

val_gen = ImageDataGenerator(rescale=1./255)

val_ds = val_gen.flow_from_directory(
    '/home/alla/ML/CapstoneProject1/archive/C-NMC_Leukemia/training_data/fold_1/',
    target_size=(150, 150),
    batch_size=20,
    shuffle=True,  class_mode='binary'
)

test_gen = ImageDataGenerator(rescale=1./255)

test_ds = val_gen.flow_from_directory(
    '/home/alla/ML/CapstoneProject1/archive/C-NMC_Leukemia/training_data/fold_2/',
    target_size=(150, 150),
    batch_size=20,
    shuffle=True,  class_mode='binary'
)



# Model creation 
def create_CNN_model_advanced(learning_rate = 0.01,  droprate=0.5):
    #create model
    model = Sequential()

    #add model layers
    # 32 filters
    # kernel size (3,3)
    # relu activation
    model.add(Conv2D(32, kernel_size=3, activation='relu', input_shape=(150,150,3)))

    # pooling: MaxPooling2D 
    #Set the pooling size to (2, 2)
    model.add(MaxPooling2D(pool_size=(2, 2)))

    # Turn the multi-dimensional result into vectors using a Flatten layer
    model.add(Flatten())

    # Next, add a Dense layer with 64 neurons and 'relu' activation 
    model.add(Dense(64, activation='relu'))
    
    # Add a dropout layer 
    model.add(Dropout(droprate))

    # Finally, create the Dense layer with 1 neuron - this will be the output 
    model.add(Dense(1, activation='sigmoid'))

    # As optimizer use SGD with the following parameters:
    # 
    opt = keras.optimizers.SGD(learning_rate=learning_rate, momentum=0.8)
    loss = keras.losses.BinaryCrossentropy(from_logits=False)

    model.compile(optimizer=opt, loss=loss, metrics=['accuracy'])
    
    return model



checkpoint = keras.callbacks.ModelCheckpoint(
    'cnn_v1_{epoch:02d}_{test_accuracy:.3f}.h5',
    save_best_only=True,
    monitor='test_accuracy',
    mode='max'
)

# selected parameters in notebook 
learning_rate = 0.001
droprate = 0.2

model = create_CNN_model_advanced(learning_rate = learning_rate,  
                                  droprate=droprate)

# save the best model 
history = model.fit(
    train_ds,
    epochs=10,
    validation_data=val_ds,
    callbacks=[checkpoint]
)

model = keras.models.load_model('cnn_v1_03_0.834.h5') 

model.evaluate(test_ds)