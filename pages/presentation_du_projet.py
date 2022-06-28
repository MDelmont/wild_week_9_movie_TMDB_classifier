#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dash import html,dcc,dash_table
import pandas as pd
import datetime
import logging

from dependancies.htmlCreate import HtmlCreate
from dependancies.conf import Conf

from pages.pages import Pages


class PresentationProject(Pages):
    def __init__(self,app):
        super().__init__(app)
        self.titre = "Présentation du projet"

        self.get_layout()

    def get_layout(self):


        try:
            self.part_of_page.append([])

        except Exception as error:
           print(f'in get_layout PresentationProject : {error}')

  
