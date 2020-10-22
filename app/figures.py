import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime as dt

from .data import *

#Mapbox

fig1 = px.choropleth(df1,locations="LOCATION", color="Value",
                                    color_continuous_scale="Jet",
                                    range_color=(0,50),
                                    scope="world",
                                    labels={"LOCATION":"Pays","TIME":"Année","Value":"Ecart salarial femmes-hommes (%)"},
                                    template="plotly_dark",
                                    animation_frame="TIME",
                                    title="Carte",
                                    height=700)

#Histogram
fig2 = px.histogram(df1, x="TIME", y="Value", color="LOCATION", labels={'TIME':'Année', 'Value':"Pourcentage d'écart de salaire homme-femme"},
                   marginal="box", # or violin, rug
                   hover_data=df1.columns)
