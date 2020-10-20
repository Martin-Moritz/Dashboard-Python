import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime as dt

from .data import *

#Mapbox

fig1 = go.Figure(px.choropleth(df1_2016,locations="LOCATION", color="Value",
                                    color_continuous_scale="Jet", range_color=(-15,40),
                                    scope="world",
                                    labels={"Value":"Pourcentage d'écart de salaire homme-femme"},
                                    template = "plotly_dark"))

"""
fig1 = px.scatter_geo(df1, locations="LOCATION", locationmode="ISO-3",
                     hover_name="LOCATION", size=df1.Value,
                     animation_frame="TIME",
                     projection="natural earth")
"""
#Histogram
fig2 = px.histogram(df2, x="total_bill", y="tip", color="sex", labels={'total_bill':'année', 'tip':'salaire moyen'},
                   marginal="box", # or violin, rug
                   hover_data=df2.columns)
