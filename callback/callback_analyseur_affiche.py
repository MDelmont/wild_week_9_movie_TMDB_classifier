#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dash.dependencies import Input, Output,State
from data.select_model import model
from pages.pages import Pages
from dash import html
import logging
def callback_analyseur_affiche(app):
    @app.callback(Output('image_contente', 'children'),
                Output('upload-data','contents'),
                Output('send_image','n_clicks'),
              Input('send_image','n_clicks'),
              State('in_url','value'),
              State('upload-data','contents'))
    def deplay_image_result(button, url, drag_drop):
        logging.info('deplay_image_result')
        list__img_df = []
        
        tablesList = []

        if button:
            ### getting the different images
            allImages = []

            if url:
                allImages.append(url)

            # if drag_drop:
            #     allImages.append(url)

            ### loop on the images
            for tmpImage in allImages:

                listModels = []

                for name_model in ['model_VGG16_transfert_learning_20', 'model_1500_10']:
                # for name_model in ['model_1500_10']:
                   
                    ### creating the DF for the tmp model
                    contentModel = [model(app,name_model).select_model(tmpImage), name_model]
                    listModels.append(contentModel)

                
                table = Pages(app).make_df_genre_to_html(tmpImage, listModels)

                tablesList.append(table)

        return html.Div(children=tablesList),[],0




