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
                                    title="Écart de revenus liés entre les hommes et les femmes",
                                    height=700)
    carte.update_layout(paper_bgcolor='#DCE8FD', coloraxis={"colorbar":{"ticksuffix":"%"}})
    return carte

carte = create_carte(df1)


##Figure Histogramme

#fonction pour créer l'histogramme
def create_histogramme(df, year):
    """
    Retourne un histogramme.

    Parameters:
        df : DataFrame or array-like or dict
        year : str

    Returns:
        Return type : plotly.graph_objects.Figure
    """

    histogramme = px.histogram(df, title="Nombre de pays en fonction de l'écart de revenus femmes-hommes - " + year,
                               x="Value", labels={'PAYS':'Pays','TIME':'Année', 'Value':"Écart salarial femmes-hommes"},
                               template='plotly', nbins=7, range_x=(0,60), range_y=(0,20), barmode='stack')
    histogramme.update_layout(title={'font':{'size':15}}, xaxis={"ticksuffix":"%"},
                              yaxis={'title':{'text':'Nombre de pays'}}, paper_bgcolor='#DCE8FD')
    return histogramme

histogramme = create_histogramme(df1,"Année")


##Figure Diagramme en barres

#fonction pour créer le diagramme
def create_diagramme(df, year):
    """
    Retourne un diagramme.

    Parameters:
        df : DataFrame or array-like or dict
        year : str

    Returns:
        Return type : plotly.graph_objects.Figure
    """

    diagramme = px.bar(df, title="Écart de revenus liés entre les hommes et les femmes - " + year, x="PAYS", y="Value",
                             color="PAYS", labels={'PAYS':'Pays','TIME':'Année', 'Value':"Écart salarial femmes-hommes"},
                             template='plotly', range_y=(0,60))
    diagramme.update_layout(title={'font':{'size':15}}, xaxis={'title':{'text':''}},
                            yaxis={'title':{'text':'Écart salarial femmes-hommes'},"ticksuffix":"%"}, paper_bgcolor='#DCE8FD')
    return diagramme

diagramme = create_diagramme(df1,"Année")

##Figure Graphe

#fonction pour créer le graphe
def create_graphe(df):
    """
    Retourne un graphique.

    Parameters:
        df : DataFrame or array-like or dict

    Returns:
        Return type : plotly.graph_objects.Figure
    """

    graphe = px.line(df, title="Évolution de l'écart de revenus femmes-hommes", x="TIME", y="Value",
                             color="PAYS", labels={'PAYS':'Pays','TIME':'Année', 'Value':"Écart salarial femmes-hommes"},
                             template='plotly', range_y=(0,55))
    graphe.update_layout(yaxis={'title':{'text':'Écart salarial femmes-hommes'},"ticksuffix":"%"}, paper_bgcolor='#DCE8FD')
    return graphe

graphe = create_graphe(df1)
