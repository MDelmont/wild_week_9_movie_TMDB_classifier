#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from dash import html,dcc,dash_table


class HtmlCreate():
    def __init__(self):
        pass
   
        
    def dropdown(self,id=None, options=None, multi=False, className='form-select',value=None,clearable=True):
        return dcc.Dropdown(id=id, options=options, multi=multi,value=value, className=className,clearable=clearable)
    
    def input(self,id=None,className='form-control'):
        return dcc.Input(id=id,className=className)

    def make_case(self,page,html_item,titre,style_case = None):       #temporaire 
        if not style_case:
            style_case = page.style_case

        layout =  html.Div(children=[
                    html.H5(titre,className='form-label mt-4'),
                    html_item
                ],style=style_case)
        return layout

    def make_datatable_form(self,id,list_columns,dropdown=None,style_data_conditional=None,data=None):
        logging.info(f'Start make_datatable_form')
        logging.info(list_columns)
        logging.info(data)
        #columns = None#[ self.conf.dict_col_sql_to_col_datatable[col] if col in self.conf.dict_col_sql_to_col_datatable.keys() else logging.error(f'{col} not in dict_col_sql_to_col_datatable') for col in list_columns  ] 
        
        layout = dash_table.DataTable(
                        id = id,
                        data=data,
                        columns=list_columns,
                        page_size=30,
                        style_data={'wigth' :'auto','height' : 'auto'},
                        editable=True,
                        row_deletable=True,
                        sort_action='native',
                        filter_action='native',
                        row_selectable="multi",
                        dropdown=dropdown,
                        style_data_conditional=style_data_conditional          
                    )
        return layout
