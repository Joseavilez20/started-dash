# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from pages import home, test
from views import graph_ruth

app = Dash(__name__)




app.layout = html.Div(children=[
     dcc.Location(id='url', refresh=False),
    html.H1(children='Hello Dash'),

    html.Div(id='page-content', children='''
        Dash: A web application framework for your data.
    '''),
    dcc.Link('Home', href='/home'),
    dcc.Link('Test', href='/test'),

    dcc.Graph(
        id='example-graph',
        figure=graph_ruth.fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
