import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from .data import *
from .figures import *

#Couleurs utilisées dans le Dashboard
colors = {
    'background': 'white',
    'text': '#49BBEE'
}

#'background': '#464A4D'

#Disposition des figures et autres composants
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

    html.Div(children=[
        #Menu déroulant pour le choix des pays
        dcc.Dropdown(
        id='selection-pays',
        placeholder='Selectionner un pays',
        options=options_selection_pays,
        multi=True,
        value=["USA","FRA","CAN","KOR","JPN","DEU"],
        style={'display': 'inline-block', 'width': '100%'}
        ),
    ], style={'display':'inline-block','width':'80%'}),

    html.Div(children=[
        #Choix entre salariés et non salariés
        dcc.RadioItems(
        id='selection-salarial',
        options=[
            {'label': 'Salariés', 'value': 'SAL'},
            {'label': 'Non-salariés', 'value': 'NSAL'}
        ],
        value='SAL',
        labelStyle={'backgroundColor':'white','width':'30%'}
        ),
    ], style={'display':'inline-block','width':'30%','position':'absolute','top':'70px','left':'1550px'}),


    #Figure Mapbox
    html.Div(children=[dcc.Graph(id='mapbox', figure=fig1)]),

    #Figure Histogram
    html.Div(children=[dcc.Graph(id='histogram', figure=fig2)]),

])
