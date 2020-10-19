import pandas as pd
import plotly.express as px

#Data Mapbox
df1 = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
                   dtype={"fips": str})

#Data Histogram
df2 = px.data.tips()
