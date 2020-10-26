import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime as dt

from .data import *

##Figure Carte

#fonction pour créer la carte
def create_carte(df,focus='world'):
    """
    Retourne une carte choroplèthe.

    Parameters:
        df : DataFrame or array-like or dict
        focus : str

    Returns:
        Return type : plotly.graph_objects.Figure
    """
    carte = px.choropleth(df,locations="LOCATION", color="Value",
                                    color_continuous_scale="Jet",
                                    range_color=(0,50),
                                    scope=focus,
                                    labels={"LOCATION":"Pays","TIME":"Année","Value":"Ecart salarial femmes-hommes"},
                                    hover_name="PAYS",
                                    template="ggplot2",
                                    animation_frame="TIME",
                                    title="Carte - Écart de revenus liés entre les hommes et les femmes",
                                    height=700)
    carte.update_layout(paper_bgcolor='#DCE8FD', coloraxis={"colorbar":{"ticksuffix":"%"}})
    return carte

carte = create_carte(df1)


##Figure Histogramme

#fonction pour créer l'histogramme
def create_histogramme(df):
    """
    Retourne un histogramme.

    Parameters:
        df : DataFrame or array-like or dict

    Returns:
        Return type : plotly.graph_objects.Figure
    """
    nbins = int(df["TIME"].max() - df["TIME"].min())+1
    histogramme = px.histogram(df, title="Histogramme - Écart de revenus liés entre les hommes et les femmes", x="TIME", y="Value",
                               color="PAYS", labels={'PAYS':'Pays','TIME':'Année', 'Value':"Ecart salarial femmes-hommes"},
                               template='simple_white', barmode='overlay', opacity=0.5, nbins=nbins, range_y=(0,60))
    histogramme.update_layout(yaxis={'title':{'text':'Écart salarial femmes-hommes'},"ticksuffix":"%"}, paper_bgcolor='#DCE8FD')
    return histogramme

histogramme = create_histogramme(df1)


##Figure Diagramme en barres

#fonction pour créer le diagramme
def create_diagramme(df,year):
    """
    Retourne un diagramme.

    Parameters:
        df : DataFrame or array-like or dict
        year : str

    Returns:
        Return type : plotly.graph_objects.Figure
    """
    diagramme = px.histogram(df, title="Diagramme - Écart de revenus liés entre les hommes et les femmes - " + year, x="PAYS", y="Value",
                             color="PAYS", labels={'PAYS':'Pays','TIME':'Année', 'Value':"Ecart salarial femmes-hommes"},
                             template='simple_white', range_y=(0,60))
    diagramme.update_layout(title={'font':{'size':15}}, xaxis={'title':{'text':''}},
                            yaxis={'title':{'text':'Écart salarial femmes-hommes'},"ticksuffix":"%"}, paper_bgcolor='#DCE8FD')
    return diagramme

diagramme = create_diagramme(df1,"Année")
