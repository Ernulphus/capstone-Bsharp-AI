
"""Model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JddBbUvhpm-Nb7IRLJWMCGpWm7R26Odc
"""

# Commented out IPython magic to ensure Python compatibility.
# %tensorflow_version 2.x
import tensorflow as tf

from tensorflow.keras import datasets, layers, models, backend
import tensorflow_datasets as tfds
import matplotlib.pyplot as plt
from keras.preprocessing.image import load_img
import numpy as np
from matplotlib import pyplot as plt
import pickle
from PIL import Image

"""

```
# This is formatted as code
```

# Setting up the Model
"""

print('Starting to get dataset')

width = 128

instruments_data = tf.keras.utils.image_dataset_from_directory('../music_instruments_images/Brass/', labels= 'inferred', batch_size=1, image_size=(width, width))

print('Done getting dataset')

#print(list(instruments_data.as_numpy_iterator()))

#print(type(instruments_data))
train_images, train_labels = tuple(zip(*instruments_data))
print('Done setting images and labels')
#print('tuple length: ', len(train_images))



train_images = np.array(train_images)
train_labels = np.array(train_labels)
train_images = np.resize(train_images, (train_images.shape[0], width, width, 3))
print('Done setting images/labels as numpy arrays')
print('ndim, shape, size: ', train_images.ndim, train_images.shape, train_images.size)

print('Scaling...')
train_images = train_images/255.0
print('Scaled')

class_names = ['FrenchHorn', 'Trombone', 'Trumpet', 'Tuba']

# validation data#
print('Fetching validation images...')
validation_data = tf.keras.utils.image_dataset_from_directory('/home/kaufmux/Documents/capstone/capstone-Bsharp-AI/validation_images/Brass/', labels= 'inferred', batch_size=1, image_size=(width, width))
val_images, val_labels = tuple(zip(*validation_data))

# validation images are the images to test the model on
val_images = np.array(val_images)
val_labels = np.array(val_labels)
val_images = np.resize(val_images, (val_images.shape[0], width, width, 3))

print('Scaling validation images...')
val_images = val_images/255.0
print('Scaled')

IMG_INDEX = 150
# plt.imshow(train_images[IMG_INDEX], cmap=plt.cm.binary)
# plt.xlabel(class_names[train_labels[IMG_INDEX]])
# plt.show()

"""POOLING AND CONVOLUTION"""

tf.keras.backend.clear_session()

model = models.Sequential()
# 32 is the amount of filters, (3, 3) is how large the filters are. the activation is what is being applied to the output of the matrix
# input shape is what the program should expect (128 by 128, 3 colors [RGB])
model.add(layers.Conv2D(32,(3,3), activation = 'relu', input_shape =(width,width,3))) # Adding the 1 here to match inputs (?)

# pooling will shrink the filter size by a factor of 2, with the stride length being 2
model.add(layers.MaxPooling2D((2,2)))
model.add(layers.Conv2D(64,(3,3), activation = 'relu'))
model.add(layers.MaxPooling2D((2,2)))
model.add(layers.Conv2D(64,(3,3), activation = 'relu'))
#FLATTENING THE LAYERS
# when we flatten the data, we are reshaping them into a single vector
model.add(layers.Flatten())
# 64 is for 64 filters
model.add(layers.Dense(64, activation = 'relu'))
# 5 for 5 classes
model.add(layers.Dense(5))

model.summary() # Print model layers

#TRAINING

# training portion of the code
model.compile(optimizer = 'adam',
              loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits = True),
              metrics = ['accuracy'])

# the more epochs, the longer it takes
# epoch is the same batch of data fed into a different order to make the model more familiar with features
history = model.fit(train_images, train_labels, epochs=5, validation_data = (val_images, val_labels), verbose=1)


# MAKING THE MODEL OUTPUT PREDICTIONS

#predictions = tf.keras.utils.image_dataset_from_directory('/Users/jonachen/Desktop/ML_Model/Model/Prediction', labels= 'inferred' ,batch_size= None)
#pred_images, pred_labels = tuple(zip(*predictions))

#pred_images = np.array(pred_images)
#pred_labels = np.array(pred_labels)

#pred_images = pred_images/255.0

#print(pred_images.shape)

#print(model.predict_on_batch(pred_images))
pickle.dump(model, open('brassmodel.pkl','wb'))