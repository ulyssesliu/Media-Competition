import numpy as np
import tensorflow as tf
from tensorflow import keras

def model_predict():
    new_model = keras.models.load_model('CNN ver.2.h5')

    probability_model = tf.keras.Sequential([new_model, tf.keras.layers.Softmax()])

    from keras.preprocessing.image import ImageDataGenerator
    import os

    predict_gen = ImageDataGenerator(rescale = 1./255)
    predict_path = 'D:\jupyter\美的校企赛\predict'

    predict_generator = predict_gen.flow_from_directory(
        predict_path,  
        target_size = (30, 30),
        batch_size = 1, 
        color_mode = 'rgb',
        class_mode = 'categorical'
    )

    # 预测
    prediction = probability_model.predict(predict_generator)
    propability = np.max(prediction[0])
    most_possible_class_index = np.argmax(prediction[0])

    folder = 'D:\\jupyter\\美的校企赛\\dataset\\dataset\\test'
    sub_folders = [name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name))]

    return most_possible_class_index
    
