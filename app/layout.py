import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from .data import *
from .figures import *

colors = {
    'background': '#464A4D',
    'text': '#49BBEE'
}


layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    dbc.Row([html.H1(
        children='Dashboard Python',
        style={
            'textAlign': 'center',
            'color': colors['text'],
            'fontWeight': 'bold'
        }
    )]),

    #html.Label(["Mapbox", dcc.Dropdown(id="dropdown1")], style={'color':'white','display': 'inline-block', 'width': '20%', 'position':'absolute','top':'20px'}),

    html.Div(children=[dcc.Graph(id='mapbox', figure=fig1)]),

    dcc.Dropdown(
    id='selection-pays',
    options=[
        {'label': 'United-States', 'value': 'USA'},
        {'label': 'France', 'value': 'FRA'},
        {'label': 'Canada', 'value': 'CAN'},
        {'label': 'Belgique', 'value': 'BEL'},
        {'label': 'Allemagne', 'value': 'DEU'},
        {'label': 'Japon', 'value': 'JPN'},
        {'label': 'Corée', 'value': 'KOR'}
    ],
    multi=True,
    value=["USA","FRA","CAN","KOR"]
),

    html.Div(children=[dcc.Graph(id='histogram', figure=fig2)]),

])
