#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import tensorflow as tf

from tensorflow.keras import models
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.preprocessing import image
import requests
import numpy as np
import base64
import os
from dependancies.conf import Conf
import logging
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
        logging.info(self.name)
     
        path =os.getcwd()+'/data/models/'+self.name
        logging.info(path)
        model=  models.load_model(path)
        logging.info('loadok')
        
        img_prepross = self.parse_function_transfert(image)
        logging.info('img_prepross SHAPE:' + str(img_prepross.shape))
        logging.info('parseok')
        
        predict_value = model.predict(img_prepross)
        logging.info('predict ok')

        df = pd.DataFrame(predict_value, columns=['Drama','Comedy',
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
                    'TV Movie'], index=['proba'])

        logging.info(df)
        df_t = df.T
        logging.info(df_t)
        logging.info('df ok ')
        
        logging.info(type(df_t))
        logging.info(df_t.columns)
        df_t.sort_values(by=['proba'],ascending = False, axis=0,inplace=True)
  
        logging.info(type(df_t))
        df_t = df_t[df_t['proba'] > 0.5]

        return df_t

    


    def parse_function_transfert(self,image):
        """Function that returns a tuple of normalized image array and labels array.
        Args:
            filename: string representing path to image
            label: 0/1 one-dimensional array of size N_LABELS
        """
        logging.info('parse_function_transfert')
        # print(url)
        
        image_decoded = tf.image.decode_jpeg(  requests.get(image).content if 'http' in image else image, channels=self.CHANNELS)

        logging.info('image_decoded SHAPE:' + str(image_decoded.shape))

        ### Decode it into a dense vector (uint8 tensor)
        

        ### Resize it to fixed shape
        image_resized = tf.image.resize(image_decoded, [self.IMG_SIZE,self.IMG_SIZE])

        logging.info('image_resized SHAPE:' + str(image_resized.shape))
        
        # ### Normalize it from [0, 255] to [0.0, 1.0]
        image_normalized = image_resized / 255.0
        
        image_normalized = np.asarray([np.array(image_normalized)]).astype(np.float32)

        return image_normalized