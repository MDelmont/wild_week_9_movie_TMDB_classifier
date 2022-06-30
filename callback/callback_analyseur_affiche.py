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
    def deplay_image_result(button,url,drag_drop):
        logging.info('deplay_image_result')
        list__img_df = []
        if button:
            for name_model in ['model_VGG16_transfert_learning_20','model_1500_10']:
                try:
                    
                    if url:
                        logging.info(f"{name_model} {url}")
                
                        list__img_df.append([model(name_model).select_model(url),url,name_model])

                    if drag_drop:
                        for img in drag_drop:
                            list__img_df.append([model(name_model).select_model(img),img,name_model])
                except Exception as error:
                    logging.error(error, exc_info=True)
        logging.info('list__img_df')
        logging.info(list__img_df)
        list_build_df = []
        for couple in list__img_df:

            

            table = list_build_df.append(Pages(app).make_df_genre_to_html(couple))
            logging.info('table is good')
           
            layout_img =  Pages(app).make_image_with_table(couple[1],table)
            logging.info('layout_img is good')
            list_build_df.append(layout_img)

            logging.info(list_build_df)
        return html.Div(children=list_build_df),[],0




