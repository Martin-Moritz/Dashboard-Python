import pandas as pd
import plotly.express as px

#Data Mapbox

df1 = pd.read_csv("data/Ecart salarial femmes-hommes.csv")
df1_2016 = df1.loc[(df1["TIME"]==2016) & (df1["SUBJECT"]=="EMPLOYEE")]
df1_emp = df1.loc[df1["SUBJECT"]=="EMPLOYEE"]

#Data Histogram
df2 = px.data.tips()
