#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 19:09:13 2021

@author: MAAT
"""

"""
Dash template
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

stylesheet = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# pandas dataframe to html table
def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

app = dash.Dash(__name__, external_stylesheets=stylesheet)

df = pd.DataFrame({
    "University": ["Bentley", "Boston University", "Boston College",
                   "Harvard", "Brandeis", "Northeastern"],
    "Enrollment": [5314, 33720, 14171, 21015, 5825, 22207],
    "City": ["Waltham", "Boston", "Chestnut Hill", "Cambridge", "Waltham", "Boston"]
})


app.layout = html.Div([
    html.H1("Welcome! ")
    ])



if __name__ == '__main__':
    app.run_server(debug=True)
    




