import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime as dt

from .data import *

##Figure Carte

#structure générale de la carte
def carte_template(df,focus='world'):
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
    return carte

#fonction pour créer la carte
def create_carte(df,focus='world'):
    carte = carte_template(df,focus)
    carte.update_layout(paper_bgcolor='#DCE8FD', coloraxis={"colorbar":{"ticksuffix":"%"}})
    return carte

carte = create_carte(df1)


##Figure Histogramme

#structure générale de l'histogramme
def histogramme_template(df):
    nbins = int(df["TIME"].max() - df["TIME"].min())+1
    histogramme = px.histogram(df, title="Histogramme - Écart de revenus liés entre les hommes et les femmes", x="TIME", y="Value", color="PAYS", labels={'PAYS':'Pays','TIME':'Année', 'Value':"Ecart salarial femmes-hommes"}, template='simple_white', barmode='overlay', opacity=0.5, nbins=nbins, range_y=(0,60))
    return histogramme

#fonction pour créer l'histogramme
def create_histogramme(df):
    histogramme = histogramme_template(df)
    histogramme.update_layout(yaxis={'title':{'text':'Écart salarial femmes-hommes'},"ticksuffix":"%"}, paper_bgcolor='#DCE8FD')
    return histogramme

histogramme = create_histogramme(df1)


##Figure Diagramme en barres

#structure générale du diagramme en barres
def diagramme_template(df,year):
    diagramme = px.histogram(df, title="Diagramme - Écart de revenus liés entre les hommes et les femmes - " + year, x="PAYS", y="Value", color="PAYS", labels={'PAYS':'Pays','TIME':'Année', 'Value':"Ecart salarial femmes-hommes"}, template='simple_white', range_y=(0,60))
    return diagramme

#fonction pour créer le diagramme
def create_diagramme(df,year):
    diagramme = diagramme_template(df,year)
    diagramme.update_layout(title={'font':{'size':15}}, xaxis={'title':{'text':''}}, yaxis={'title':{'text':'Écart salarial femmes-hommes'},"ticksuffix":"%"}, paper_bgcolor='#DCE8FD')
    return diagramme

diagramme = create_diagramme(df1,"Année")
