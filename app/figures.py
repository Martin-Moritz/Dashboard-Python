import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime as dt

from .data import *

#Figure Mapbox
fig1 = px.choropleth(df1,locations="LOCATION", color="Value",
                                    color_continuous_scale="Jet",
                                    range_color=(0,50),
                                    scope="world",
                                    labels={"LOCATION":"Pays","TIME":"Année","Value":"Ecart salarial femmes-hommes (%)"},
                                    hover_name="PAYS",
                                    template="ggplot2",
                                    animation_frame="TIME",
                                    title="Carte",
                                    height=700)

fig1.update_layout(paper_bgcolor='#DCE8FD')

#Figure Histogram
fig2 = px.histogram(df1, x="TIME", y="Value", color="PAYS", labels={'TIME':'Année', 'Value':"Ecart salarial femmes-hommes (%)"}, histfunc='avg', barmode='overlay', opacity=0.5, nbins=26)

#Figure Diagramme en barres
fig3 = px.histogram(df1, x="PAYS", y="Value", color="PAYS", labels={'TIME':'Année', 'Value':"Ecart salarial femmes-hommes (%)"})
