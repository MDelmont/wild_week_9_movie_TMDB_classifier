#!/usr/bin/env python
# -*- coding: utf-8 -*-
import dash_bootstrap_components as dbc
from dash import html, dcc

class Header():
    def __init__(self):
        self.menu = dbc.NavbarSimple(
            
            brand="movie poster classifer",
            brand_href="/presentation_du_projet",
            color='dark',
            dark=True,
            links_left =True,
            children = [
                
         
                dbc.NavItem(
                    dbc.NavLink(
                        
                        "Présentation du projet",
                        href='/presentation_du_projet',
                       
                    )
                ),

                dbc.NavItem(
                    dbc.NavLink(
                        
                        "analyseur d'affiche",
                        href='/analyseur_affiche',
                       
                    )
                ),

                dbc.NavItem(
                    dbc.NavLink(
                        
                        "historique des recherches",
                        href='/historique_recherches',
                       
                    )
                ),
              
            ],
            
        )
