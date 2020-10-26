import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime as dt

from .data import *

#Figure Mapbox
fig1 = px.choropleth(df1,locations="LOCATION", color="Value",
                                    color_continuous_scale="Jet",
                                    range_color=(0,50),
                                    scope="world",
                                    labels={"LOCATION":"Pays","TIME":"Année","Value":"Ecart salarial femmes-hommes"},
                                    hover_name="PAYS",
                                    template="ggplot2",
                                    animation_frame="TIME",
                                    title="Carte",
                                    height=700)

fig1.update_layout(paper_bgcolor='#DCE8FD', coloraxis={"colorbar":{"ticksuffix":"%"}})

#Figure Histogram
fig2 = px.histogram(df1, title='Histogramme', x="TIME", y="Value", color="PAYS", labels={'PAYS':'Pays','TIME':'Année', 'Value':"Ecart salarial femmes-hommes"}, template='simple_white', barmode='overlay', opacity=0.5, nbins=26, range_y=(0,60))

fig2.update_layout(yaxis={'title':{'text':'Ecart salarial femmes-hommes'},"ticksuffix":"%"}, paper_bgcolor='#DCE8FD')

#Figure Diagramme en barres
fig3 = px.histogram(df1, x="PAYS", y="Value", color="PAYS", labels={'PAYS':'Pays','TIME':'Année', 'Value':"Ecart salarial femmes-hommes"}, template='simple_white', range_y=(0,60))

fig3.update_layout(yaxis={'title':{'text':'Ecart salarial femmes-hommes'},"ticksuffix":"%"}, paper_bgcolor='#DCE8FD')
