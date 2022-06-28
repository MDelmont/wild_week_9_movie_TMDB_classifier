#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dash import html,dcc,dash_table
import pandas as pd
import datetime
import logging

from dependancies.htmlCreate import HtmlCreate
from dependancies.conf import Conf

from pages.pages import Pages


class Analyseur_affiche(Pages):
    def __init__(self,app):
        super().__init__(app)
        self.titre = "Analyseur d'affiche"
        self.get_layout()

    def get_layout(self):


        layout = html.Div(children=[

            self.part_of_load_img()
        ])
        self.part_of_page.append(layout)
        return None

    def part_of_load_img(self):

        return html.Div(children=[


            html.H5('charger votre fichier '),
            dcc.Upload(id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '50%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True)


        ])