import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime as dt

from .data import *

#Mapbox
from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

fig1 = go.Figure(go.Choroplethmapbox(geojson=counties, locations=df1.fips, z=df1.unemp,
                                    colorscale="Viridis", zmin=0, zmax=12,
                                    marker_opacity=0.5, marker_line_width=0))
fig1.update_layout(mapbox_style="carto-positron",
                  mapbox_zoom=3, mapbox_center = {"lat": 37.0902, "lon": -95.7129})
fig1.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

#Histogram
fig2 = px.histogram(df2, x="total_bill", y="tip", color="sex", labels={'total_bill':'année', 'tip':'salaire moyen'},
                   marginal="box", # or violin, rug
                   hover_data=df2.columns)
