#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd


import base64
class Datas():
    def __init__(self, app):
        self.app = app
    

    def get_image_good_format(self,image):
        
        
        encoded_image = base64.b64encode(image)

        trendImage = 'data:image/jpg;base64,{}'.format(encoded_image.decode())

        return trendImage