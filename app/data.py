import pandas as pd
import plotly.express as px

#Data Mapbox

##Pourcentage d'écart salarial femmes-hommes
df1 = pd.read_csv("data/Ecart salarial femmes-hommes.csv")

##Valeurs utiles
#nombre total de pays différents dans la dataset
nb_pays = df1.drop_duplicates(subset=['LOCATION']).shape[0]

#Filtrage des données
#Suppression des années
deleted_years=[i for i in range(1970,1992)]
deleted_years.append(2019)
for i in deleted_years:
    df1 = df1.drop(df1[df1.TIME==i].index)
#Suppression des pays
deleted_countries=["OECD","HRV","TUR","BGR","ROU","CYP","MLT","CHL"]
for i in deleted_countries:
    df1 = df1.drop(df1[df1.LOCATION==i].index)

#Data Histogram
df2 = px.data.tips()
