import pandas as pd
import plotly.express as px

##Pourcentage d'écart salarial femmes-hommes
df1 = pd.read_csv("data/Ecart salarial femmes-hommes.csv")

##Data utilisée pour l'ajout des continents et noms de pays correspondants dans la dataset principale
#liste des continents
df_continent=pd.read_csv("https://pkgstore.datahub.io/JohnSnowLabs/country-and-continent-codes-list/country-and-continent-codes-list-csv_csv/data/b7876b7f496677669644f3d1069d3121/country-and-continent-codes-list-csv_csv.csv",sep=",")
#liste des pays en français
df_pays=pd.read_csv("data/pays.csv",sep=',')

##Filtrage des données
#Suppression des années avec peu de données
deleted_years=[i for i in range(1970,1992)]
deleted_years.append(2019)
for i in deleted_years:
    df1 = df1.drop(df1[df1.TIME==i].index)
#Suppression des pays avec peu de données
deleted_countries=["OECD","HRV","TUR","BGR","ROU","CYP","MLT","CHL","NZL"]
for i in deleted_countries:
    df1 = df1.drop(df1[df1.LOCATION==i].index)


#Ajout d'une colonne "CONTINENT"
continents=[]

for i in range(df1.LOCATION.size):
    found = False
    j=0
    while j<df_continent.Three_Letter_Country_Code.size and found==False:
        if df1.LOCATION.iloc[i]==df_continent.Three_Letter_Country_Code.iloc[j]:
            continents.append(df_continent.Continent_Name.iloc[j])
            found=True
        else:
            j=j+1

#Renommage des continents en français
for i in range(len(continents)):
    if continents[i]=="Asia":
        continents[i]="Asie"
    elif continents[i]=="Oceania":
        continents[i]="Océanie"
    elif continents[i]=="North America":
        continents[i]="Amérique du Nord"
    elif continents[i]=="South America":
        continents[i]="Amérique du Sud"
    elif continents[i]=="Africa":
        continents[i]="Afrique"

df1['CONTINENT']=continents

#Ajout d'une colonne "PAYS"
pays=[]

for i in range(df1.LOCATION.size):
    found = False
    j=0
    while j<df_pays.AFG.size and found==False:
        if df1.LOCATION.iloc[i]==df_pays.AFG.iloc[j]:
            pays.append(df_pays.Afghanistan.iloc[j])
            found=True
        else:
            j=j+1

df1['PAYS']=pays

#nombre total de pays différents dans la dataset
nb_pays = df1.drop_duplicates(subset=['LOCATION']).shape[0]
#liste des codes à trois lettres des différents pays de la dataset
liste_code_pays = df1.drop_duplicates(subset=['LOCATION']).LOCATION
#liste des noms en français des différents pays
liste_noms_pays = df1.drop_duplicates(subset=['LOCATION']).PAYS

##Liste des pays à sélectionner dans le menu déroulant
options_selection_pays = []
for i in range(liste_code_pays.size):
    option = {}
    option['label']=liste_noms_pays.iloc[i]
    option['value']=liste_code_pays.iloc[i]
    options_selection_pays.append(option)
