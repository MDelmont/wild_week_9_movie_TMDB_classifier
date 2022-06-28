#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dash import html,dcc,dash_table
import pandas as pd
import datetime
import logging

from dependancies.htmlCreate import HtmlCreate
from dependancies.conf import Conf

from pages.pages import Pages


class Historyque_recherche(Pages):
    def __init__(self,app):
        super().__init__(app)
        self.titre = "Historique de recherches"
        self.get_layout()

    def get_layout(self):
        return None

