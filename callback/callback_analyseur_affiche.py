#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dash.dependencies import Input, Output,State
from data.select_model import model
from pages.pages import Pages
from dash import html
def callback_analyseur_affiche(app):
    @app.callback(Output('image_contente', 'children'),
                Output('upload-data','contents'),
              Input('Button_send_new_demand','n_clicks'),
              State('new_demande_Client','value'),
              State('upload-data','contents'))
    def deplay_image_result(button,url,drag_drop):
        
        list__img_df = []
        if button:
            for name_model in ['model_VGG16_transfert_learning_20','model_1500_10']:
                if url:
               
                    list__img_df.append([model(name_model).select_model(url),url,name_model])

                if drag_drop:
                    for img in drag_drop:
                        list__img_df.append([model(name_model).select_model(img),img,name_model])

        
        list_build_df = []
        for couple in list__img_df:

            

            table = list_build_df.append(Pages(app).make_df_genre_to_html(couple))

           
            layout_img =  Pages(app).make_image_with_table(couple[1],table)

            list_build_df.append(layout_img)

        
        return html.Div(list_build_df),None

        pass


