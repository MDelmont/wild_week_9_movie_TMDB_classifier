#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import tensorflow as tf
from tensorflow.keras import models
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from keras.utils import load_img,img_to_array
from tensorflow.keras.preprocessing import image
import requests
import numpy as np
import base64
from dependancies.conf import Conf

class model():
    def __init__(self,name):
        self.conf = Conf()
        self.CHANNELS=3
        self.name = name
        if name == 'model_VGG16_transfert_learning_20':
            self.IMG_SIZE = 224
        else:
            self.IMG_SIZE = 400

   
    def select_model(self,image):

        model= models.load_model(f'E:\matth\Documents\Cours\Wild code school\Data Scientist\projet\projet_9\wild_week_9_movie_TMDB_classifier\data\models\{self.name}')
        img_prepross = self.parse_function_transfert(image)
        predict_value = model.predict(img_prepross)

        df = pd.DataFrame(predict_value,index=['Drama','Comedy',
                    'Crime',
                    'Action',
                    'Thriller',
                    'Documentary',
                    'Adventure',
                    'Science Fiction',
                    'Animation',
                    'Family',
                    'Romance',
                    'Mystery',
                    'Horror',
                    'Fantasy',
                    'War',
                    'Music',
                    'Western',
                    'History',
                    'TV Movie'],columns=['Proba'])
       

        df['proba'].sort_values(ascending = False, inplace=True)
        
        df = df[df['proba'] > 0.5]

        return df

    

    




  


    def parse_function_transfert(self,image):
        """Function that returns a tuple of normalized image array and labels array.
        Args:
            filename: string representing path to image
            label: 0/1 one-dimensional array of size N_LABELS
        """
        
        # print(url)
        
        image_decoded = tf.image.decode_jpeg(  requests.get(image).content if 'http' in image else image, channels=self.CHANNELS)

        ### Decode it into a dense vector (uint8 tensor)
        
        
        ### Resize it to fixed shape
        image_resized = tf.image.resize(image_decoded, [self.IMG_SIZE,self.IMG_SIZE])
        
        # ### Normalize it from [0, 255] to [0.0, 1.0]
        image_normalized = image_resized / 255.0
        
        return np.array(image_normalized)