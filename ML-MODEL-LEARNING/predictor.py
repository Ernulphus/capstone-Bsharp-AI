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

familyList = ['Brass', 'Woodwind', 'Percussion', 'Strings']
instList = ['FrenchHorn','Trombone','Trumpet','Tuba']
woodList = ['Bagpipes', 'Clarinet', 'Flute', 'Saxophone']
percList = ['BassDrum', 'Conga', 'Piano', 'SnareDrum']
stringList = ['Banjo', 'Guitar', 'Harp', 'Violin']

# Load root model first
model = pickle.load(open('/root/capstone-Bsharp-AI/ML-MODEL-LEARNING/brassmodelVold.pkl','rb'))

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

family = familyList[max_index]

print(family, end='')

# Load the correct new model
if family == 'Brass':
    model = pickle.load(open('/root/capstone-Bsharp-AI/ML-MODEL-LEARNING/brassmodel.pkl','rb'))
if family == 'Woodwind':
    model = pickle.load(open('/root/capstone-Bsharp-AI/ML-MODEL-LEARNING/woodwindmodel.pkl','rb'))
    instList = woodList
if family == 'Percussion':
    model = pickle.load(open('/root/capstone-Bsharp-AI/ML-MODEL-LEARNING/percmodel.pkl','rb'))
    instList = percList
if family == 'Strings':
    model = pickle.load(open('/root/capstone-Bsharp-AI/ML-MODEL-LEARNING/stringmodel.pkl','rb'))
    instList = stringList


predict_arr = model.predict_on_batch(pred_image)

predict_list = predict_arr[0].tolist()

#print(predict_list)

max_value = max(predict_list)

max_index = predict_list.index(max_value)

guess = instList[max_index]

print(guess, end='')
