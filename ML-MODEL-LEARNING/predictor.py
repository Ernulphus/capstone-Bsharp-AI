import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import tensorflow_datasets as tfds
import matplotlib.pyplot as plt
from keras.preprocessing.image import load_img
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import pickle
import sys

instrumentList = ['FrenchHorn','Trombone','Trumpet','Tuba']
model = pickle.load(open('/root/capstone-Bsharp-AI/ML-MODEL-LEARNING/model.pkl','rb'))

file_path = sys.argv[1] 
img = Image.open(file_path)
newsize = (256,256)
img = img.resize(newsize)

prediction_img = tf.keras.utils.img_to_array(
    img, data_format=None, dtype=None
)

pred_image = np.array(prediction_img)


pred_image = np.expand_dims(pred_image, axis = 0)

pred_image = pred_image/255.0

predict_arr = model.predict_on_batch(pred_image)

predict_list = predict_arr[0].tolist()

#print(predict_list)

max_value = max(predict_list)

max_index = predict_list.index(max_value)

print(instrumentList[max_index], end='')
