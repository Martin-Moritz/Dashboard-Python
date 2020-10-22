import flask
import dash

from . import app

from .callbacks import register_callbacks
from .layout import layout

#style de page utilisé pour le dashboard
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#Création de l'application Dash
dashapp = dash.Dash(__name__, external_stylesheets=external_stylesheets, server=app,
    routes_pathname_prefix='/dashapp/')

dashapp.layout = layout
register_callbacks(dashapp)
