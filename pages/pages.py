#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from dash import html, dash_table
from dependancies.style import default_style_page
from dependancies.htmlCreate import HtmlCreate
from dependancies.conf import Conf
import pandas as pd
import base64

class Pages():
    def __init__(self,app):
        self.app = app
        self.conf = Conf()
        self.titre = ''
        self.part_of_page = []
        self.defaut_style = default_style_page()
        self.style_part_of_page, self.style_part_of_form ,self.style_form, self.style_col, self.style_case = self.defaut_style.get_default_style()

    def build_page(self):
        logging.info(f'Start to build page {self.titre}')
        layout_page=[]
        try:
            layout_page = html.Div([
            

                html.Div([
                    html.H1(self.titre,  style={'textAlign': 'center'}
                )],self.style_part_of_page),

                html.Div(self.make_part_of_page(self.part_of_page,self.style_part_of_page))
            
            ])
        except Exception as error:
            logging.error(f'in build_page {self.titre} : {error}')


        return layout_page

    
    def make_part_of_page(self,list_part,style):
        logging.info('Start make_part_of_page')
        part_of_build=[]
        if list_part:
       
            part_of_build.extend(html.Div([part],style=style) for part in list_part)
         
        return html.Div(part_of_build)

    def build_formulaire(self,nb_col,nb_ligne,list_case):
        logging.info('Start build_formulaire')
        list_layout_by_col = []
        i=0
        
        for col in range(nb_col):
            try:
                if col+1 == nb_col:
                    list_layout_by_col.append(self.make_col(col,nb_col,list_case[i:]))
                else:
                
                    list_layout_by_col.append(self.make_col(col,nb_col,list_case[i:i+nb_ligne]))
                
            except Exception as error:
                logging.error(f'in build_formulaire for build col: error{error}')
                
            i+=nb_ligne
            
        return html.Div(list_layout_by_col,style=self.style_part_of_form)

    def make_col(self,num_col,nb_col,list_layout):
        logging.info('Start make_col')

        style_col = {'width': f'{int(100/nb_col)}%', 'display': 'inline-block','textAlign': 'center','vertical-align':'top'}
        return html.Div(id=f'Col-{num_col}',children=[*list_layout],style = style_col)

    def make_case(self,page,html_item,titre):        
        logging.info('Start make_case')
        layout =  html.Div(children=[
                    html.H5(titre,className='form-label mt-4'),
                    html_item
                ],style=self.style_case)
        return layout

    def get_layout_for_modify_table(self,name,id_table,list_col,id_button):

        self.part_of_page.append(self.get_layout_table(name,id_table,list_col))
        self.part_of_page.append(html.Div([
                    html.Button(f"Modifier les {name}",id=id_button,className='btn btn-primary')
                ],style=self.defaut_style.style['style_form']))


    def get_layout_table(self,name,id_table,list_col):
        try:

            part_of_form = [html.H3(f"Table des {name}",
                            style=self.defaut_style.style['text_align_center']),

                        self.build_formulaire(1,1,[HtmlCreate().make_datatable_form(id_table,
                            list_col)]),
                        ]
        
        except Exception as error:
            logging.error(f'in get_layout_table_of_demande : {error}')
        return self.make_part_of_page(part_of_form,self.defaut_style.style['style_part_of_form'])

    def make_image_with_table(self,img,table):
        image = img if 'http' in img else 'data:image/jpg;base64,{}'.format( base64.b64encode(img).decode())


        return html.Div(children=[

            html.Div(children=[

                     html.Img(id='import_img_detect',src=image,style={'height':'20%', 'width':'20%'})

            ],style={'width':'50%'}),

            html.Div(children=[

                    table

            ],style={'width':'50%'})

        ],style = {'width':'100%', 'display': 'inline-block','textAlign': 'center'})

    def make_df_genre_to_html(self, img, couple):
        
        logging.info('make_df_genre_to_html')
        
        # modelsTable = html.Div(
        #     children=[

        #     ]
        # )

        listModelsTables = []

        ### loop on the models
        for tmpModel in couple:

            tmpListRows = []
            
            tmpDF = tmpModel[0]
            tmpDF['genre'] = tmpDF.index
            tmpDF['proba'] = tmpDF['proba'].apply(lambda x : round(x,2))
            tmpDF['proba'] = tmpDF['proba'].apply(str)
            # data = tmpDF.to_dict('records') if tmpDF.to_dict('records') else None
            
            logging.info(str(tmpDF))

            for tmpIndex in tmpDF.index:
                logging.info('Index:'+str(tmpIndex))
                rowToAppend = html.Tr(
                    children=[
                        html.Td(
                            children=[
                                tmpDF.loc[tmpIndex]['genre']         ### genre name
                            ],
                            style={'width':'50%'}
                        ),
                        html.Td(
                            children=[
                                tmpDF.loc[tmpIndex]['proba']         ### probability value
                            ],
                            style={'width':'50%'}
                        )
                    ]
                )

                tmpListRows.append(rowToAppend)

            
            tmpTable = html.Table(
                className='table table-hover',
                children=[
                    html.Tr(
                        children=[
                            html.Th(
                                children=[
                                    tmpModel[1]         ### model name
                                ],
                                colSpan=2,
                                style={'text-align':'center'}
                            )      
                        ]
                    ),
                    html.Tr(
                        children=[
                            html.Td(
                                children=[
                                    'Genre'             ### genre header
                                ],
                                style={'width':'50%'}
                            ),
                            html.Td(
                                children=[
                                    'Probability'       ### probability header
                                ],
                                style={'width':'50%'}
                            )     
                        ]
                    ),
                    *tmpListRows
                ]
            )

            listModelsTables.append(tmpTable)



        ### creating the image
        image = img if 'http' in img else 'data:image/jpg;base64,{}'.format( base64.b64encode(img).decode())

        fullTable = html.Table(
            children=[
                html.Tr(
                    children=[
                        html.Td(
                            children=[
                                ## movie poster
                                html.Img(id='import_img_detect', src=image, style={'width':'400px'})
                            ],
                            style={'width':'10%'}
                        ),
                        html.Td(
                            children=[
                                # html.Table(
                                #     children=[
                                #         ### headers
                                #         html.Tr(
                                #             children=[
                                #                 html.Th('Genre'),
                                #                 html.Th('Probability')
                                #             ]
                                #         ),

                                #         ### all the rows about the probabilities
                                #         html.Tr(
                                #             children=[
                                #                 # html.Td('Genre')
                                #             ]
                                #         )
                                #     ]
                                # )
                                *listModelsTables
                            ],
                            style={'width':'90%'}
                        )
                    ],
                    style={'height':'90%'}
                )
            ],
            style={'border':'solid 2px #fefefe','width':'100%'}
        )


        # list_lign = [
        #     html.Div(children=[ html.H6(model_name,style={'width':'100%','textAlign': 'center'})],style={'width':'100%','display': 'inline-block'}),
        #    ]
        # logging.info(data)
        # if data:
        #     list_lign.append( html.Div(children=[
        #             html.Div(children=[html.H6('genre')],style={'width':'50%'}),
        #             html.Div(children=[html.H6('Proba')],style={'width':'50%'}),
                
        #         ],style={'width':'100%'}))
        #     for line in data:
        #         list_lign.append(  html.Div(children=[
        #             html.Div(children=[html.H6(line['genre'])],style={'width':'50%'}),
        #             html.Div(children=[html.H6(line['proba'])],style={'width':'0%'}),
                
        #         ],style={'width':'100%'}))
        #     return html.Div(children=list_lign)
        # else:
       
        #     list_lign.append(html.Div(children=[ html.H6('Not predict',style={'width':'100%','textAlign': 'center'})],style={'width':'100%','display': 'inline-block'}))
        #     return html.Div(children=list_lign)

        return fullTable




    
    def make_row(self,genre,proba):
        return html.Div(children=[
                html.Div([genre
                ],style={'width':'50%'}),

                html.Div([proba
                ],style={'width':'50%'})

        ],style={'width':'100%'})
