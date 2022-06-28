#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dash
import logging
from datetime import datetime
import pytz

class App():
    def __init__(self):
  
        
        self.start_time = datetime.now()
        self.launch_time = pytz.timezone('Europe/Paris').localize(datetime.now()).strftime('%Y-%m-%d_%H_%M')

        logging.basicConfig(filename=f"outlogs_{self.launch_time}.log",level=logging.INFO)

        logging.info(f"[ INITIALISATION : APP for Back office {self.launch_time} ]")
        
    # meta_tags are required for the app layout to be mobile responsive
    app = dash.Dash(__name__, suppress_callback_exceptions=True,
                    meta_tags=[{'name': 'viewport',
                                'content': 'width=device-width, initial-scale=1.0'}]
                    )
    server = app.server
