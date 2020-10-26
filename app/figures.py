import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime as dt

from .data import *

##Données utilisées qui pourront être modifiées dans les graphiques
filtered_df = df1


##Figure Carte

#focus de la carte
focus = 'world'

#structure générale de la carte
carte_template = px.choropleth(filtered_df,locations="LOCATION", color="Value",
                                    color_continuous_scale="Jet",
                                    range_color=(0,50),
                                    scope=focus,
                                    labels={"LOCATION":"Pays","TIME":"Année","Value":"Ecart salarial femmes-hommes"},
                                    hover_name="PAYS",
                                    template="ggplot2",
                                    animation_frame="TIME",
                                    title="Carte - Écart de revenus liés entre les hommes et les femmes",
                                    height=700)

#fonction pour créer la carte
def create_carte():
    carte = carte_template
    carte.update_layout(paper_bgcolor='#DCE8FD', coloraxis={"colorbar":{"ticksuffix":"%"}})
    return carte

carte = create_carte()


##Figure Histogramme

#structure générale de l'histogramme
histogramme_template = px.histogram(filtered_df, title="Histogramme - Écart de revenus liés entre les hommes et les femmes", x="TIME", y="Value", color="PAYS", labels={'PAYS':'Pays','TIME':'Année', 'Value':"Ecart salarial femmes-hommes"}, template='simple_white', barmode='overlay', opacity=0.5, nbins=26, range_y=(0,60))

#fonction pour créer l'histogramme
def create_histogramme():
    histogramme = histogramme_template
    histogramme.update_layout(yaxis={'title':{'text':'Écart salarial femmes-hommes'},"ticksuffix":"%"}, paper_bgcolor='#DCE8FD')
    return histogramme

histogramme = create_histogramme()


##Figure Diagramme en barres

#structure générale du diagramme en barres
diagramme_template = px.histogram(filtered_df, title="Diagramme - Écart de revenus liés entre les hommes et les femmes", x="PAYS", y="Value", color="PAYS", labels={'PAYS':'Pays','TIME':'Année', 'Value':"Ecart salarial femmes-hommes"}, template='simple_white', range_y=(0,60))

#fonction pour créer le diagramme
def create_diagramme():
    diagramme = diagramme_template
    diagramme.update_layout(yaxis={'title':{'text':'Écart salarial femmes-hommes'},"ticksuffix":"%"}, paper_bgcolor='#DCE8FD')
    return diagramme

diagramme = create_diagramme()
