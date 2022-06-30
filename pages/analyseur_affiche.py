#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dash import html,dcc,dash_table
import pandas as pd
import datetime
import logging

from dependancies.htmlCreate import HtmlCreate
from dependancies.conf import Conf
from dash import html, dash_table
from pages.pages import Pages


class Analyseur_affiche(Pages):
    def __init__(self,app):
        super().__init__(app)
        self.titre = "Analyseur d'affiche"
        self.get_layout()

    def get_layout(self):


    
        self.part_of_page.append( self.part_of_load_img())
        self.part_of_page.append(self.part_of_see_images())
        return None

    def part_of_load_img(self):

        part_of_page=[

            html.H5('Charger vos images '),

        ]

        part_of_form = [

            self.make_case(self,dcc.Upload(id='upload-data',
            children=html.Div([
                'Drag and Drop or ',
                html.A('Select Files')
            ]),
            style={
              
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center',
            },

            # Allow multiple files to be uploaded
            multiple=True),' en local'),


            self.make_case(self,dcc.Input(id='in_url',className='form-control'),'en url')
        
    
        
        ]

        part_of_page.append(self.build_formulaire(2,1,part_of_form))


        part_of_page.append(html.Button("Envoyer",id='send_image',className='btn btn-light'))
        return html.Div(children=part_of_page,style=self.style_form)
        # return html.Div(children=[


            

        #     html.Div(children=[
        #         html.Div(children=[


        #         dcc.Upload(id='upload-data',
        #     children=html.Div([
        #         'Drag and Drop or ',
        #         html.A('Select Files')
        #     ]),
        #     style={
        #         'width': '50%',
        #         'lineHeight': '60px',
        #         'borderWidth': '1px',
        #         'borderStyle': 'dashed',
        #         'borderRadius': '5px',
        #         'textAlign': 'center',
        #     },

        #     # Allow multiple files to be uploaded
        #     multiple=True)],style= {'width': '50%', 'display': 'inline-block','textAlign': 'center'}),
        #         html.Div(children=[
        #             html.Div(children=[
                        

        #             ],style= {'width': '50%', 'display': 'inline-block','textAlign': 'center'})
        #         ]  ,style= {'width': '50%', 'display': 'inline-block','textAlign': 'center'})
        #     ],style= {'width': '50%', 'display': 'inline-block','textAlign': 'center','padding-right':'12px'})
        # ],style= {'width': '100%', 'display': 'inline-block','textAlign': 'center','padding-top':'25px'})


    def part_of_see_images(self):

        return html.Div(children=[


            html.H5('Resultat'),
            html.Div(id='image_contente',children=[
               

  
        # Allow multiple files to be uploaded
        ],style= {'width': '50%', 'display': 'inline-block','textAlign': 'center','padding-top':'12px'})
        ],style= {'width': '100%', 'display': 'inline-block','textAlign': 'center','padding-top':'25px'})
    
    def make_layout_for_images(self,titre_image):

        return html.Div(children=[
            html.H5(titre_image),
            html.Img(id='import_img_detect',src='https://image.tmdb.org/t/p/w342/ojDg0PGvs6R9xYFodRct2kdI6wC.jpg',style={'height':'20%', 'width':'20%'})
        ])