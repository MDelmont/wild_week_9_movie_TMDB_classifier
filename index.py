#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dash import html, dcc
from dash.dependencies import Input, Output
from pages.header import Header
from app import App

from pages.presentation_du_projet import PresentationProject
from pages.analyseur_affiche import Analyseur_affiche
from pages.historique_recherche import Historyque_recherche
from callback import callback
from data.select_model import model
application = App()
app = application.app
server = application.server
header = Header()
callback.import_all_callback(app)
model(app,'temp').make_variable_app_model()

#layout rendu par l'application
app.layout = html.Div([
    dcc.Location(id='url', refresh=True),
    header.menu,
    html.Div(id='page-content')
    ])


def generate_variables(app):
    presProject = PresentationProject(app)

    analyseur_affiche = Analyseur_affiche(app)
    historique_recherche = Historyque_recherche(app)
    return presProject , analyseur_affiche, historique_recherche

presProject, analyseur_affiche, historique_recherche = generate_variables(app)

endpoints = {
         '/' : presProject.build_page(),
         '/presentation_du_projet' : presProject.build_page(),
         '/analyseur_affiche' : analyseur_affiche.build_page(),
         '/historique_recherches' : historique_recherche.build_page(),
}

#callback pour mettre à jour les pages
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    try:
        return endpoints[pathname]
    except Exception as error:
        return f"ERROR : {error}"

 
if __name__ == '__main__':
    app.run_server(debug=True)