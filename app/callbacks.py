import dash
from dash.dependencies import *

from .data import *
from .figures import *

#Callbacks pour rafraichir et mettre à jour les différentes figures
def register_callbacks(dashapp):
    @dashapp.callback(
        [Output('mapbox', 'figure'), Output('selection-pays', 'disabled')],
        [Input('selection-pays', 'value'), Input('selection-salarial','value')])
    def update_figure(selected_countries, selected_salarial):

        #focus de la carte
        focus = 'world'

        #Filtrage des données en fonction du choix salariés ou non-salariés
        if selected_salarial == "SAL":
            filtered_df = df1.loc[df1["SUBJECT"]=="EMPLOYEE"]
        else:
            filtered_df = df1.loc[df1["SUBJECT"]=="SELFEMPLOYED"]

        if selected_salarial != "SAL":
            filtered_df = filtered_df.drop(filtered_df[filtered_df.LOCATION=="NZL"].index)
            fig1 = px.choropleth(filtered_df, locations="LOCATION", color="Value",
                                                color_continuous_scale="Jet",
                                                range_color=(0,50),
                                                scope=focus,
                                                labels={"LOCATION":"Pays","TIME":"Année","Value":"Ecart salarial femmes-hommes (%)"},
                                                hover_name="PAYS",
                                                template = "ggplot2",
                                                animation_frame="TIME",
                                                title="Carte",
                                                height= 700)
        else:
            #Mise à jour de la carte si aucun pays n'a été sélectionné (montre alors tous les pays disponibles)
            if selected_countries==[]:
                filtered_df = filtered_df.drop(filtered_df[filtered_df.TIME==1996].index)
                fig1 = px.choropleth(filtered_df, locations="LOCATION", color="Value",
                                                    color_continuous_scale="Jet",
                                                    range_color=(0,50),
                                                    scope=focus,
                                                    labels={"LOCATION":"Pays","TIME":"Année","Value":"Ecart salarial femmes-hommes (%)"},
                                                    hover_name="PAYS",
                                                    template = "ggplot2",
                                                    animation_frame="TIME",
                                                    title="Carte",
                                                    height= 700)

            #Mise à jour de la carte en fonction des pays sélectionnés
            else:
                frames = []
                for i in selected_countries:
                    frames.append(filtered_df[filtered_df["LOCATION"]==i])
                filtered_df = pd.concat(frames)

                #Ajuste le focus de la carte si un seul pays est sélectionné
                if len(selected_countries)==1:
                    if filtered_df.CONTINENT[filtered_df["LOCATION"]==selected_countries[0]].any()=="Asie":
                        focus='asia'
                    elif filtered_df.CONTINENT[filtered_df["LOCATION"]==selected_countries[0]].any()=="Europe":
                        focus='europe'
                    elif filtered_df.CONTINENT[filtered_df["LOCATION"]==selected_countries[0]].any()=="Amérique du Nord":
                        focus='north america'
                    elif filtered_df.CONTINENT[filtered_df["LOCATION"]==selected_countries[0]].any()=="Amérique du Sud":
                        focus='south america'
                    elif filtered_df.CONTINENT[filtered_df["LOCATION"]==selected_countries[0]].any()=="Afrique":
                        focus='africa'

                #Enlève les données qui ne peuvent être comparées (par ex. qu'une seule donnée/pays pour l'année 1975)
                for i in range(filtered_df["TIME"].min(),filtered_df["TIME"].max()+1):
                    if filtered_df.loc[filtered_df["TIME"]==i].shape[0] != len(frames):
                        filtered_df = filtered_df.drop(filtered_df[filtered_df.TIME==i].index)

                fig1 = px.choropleth(filtered_df,locations="LOCATION", color="Value",
                                                    color_continuous_scale="Jet",
                                                    range_color=(0,50),
                                                    scope=focus,
                                                    labels={"LOCATION":"Pays","TIME":"Année","Value":"Ecart salarial femmes-hommes (%)"},
                                                    hover_name="PAYS",
                                                    template = "ggplot2",
                                                    animation_frame="TIME",
                                                    title="Carte",
                                                    height=700)

        #Activation du menu déroulant
        if selected_salarial=="SAL":
            disabled=False
        else:
            disabled=True

        fig1.update_layout(paper_bgcolor='#DCE8FD')

        return fig1, disabled


    @dashapp.callback(
        Output('histogram', 'figure'),
        [Input('selection-pays', 'value'), Input('selection-salarial','value')])
    def update_figure(selected_countries, selected_salarial):

        #Filtrage des données en fonction du choix salariés ou non-salariés
        if selected_salarial == "SAL":
            filtered_df = df1.loc[df1["SUBJECT"]=="EMPLOYEE"]
        else:
            filtered_df = df1.loc[df1["SUBJECT"]=="SELFEMPLOYED"]

        if selected_salarial != "SAL":
            #filtered_df = filtered_df.drop(filtered_df[filtered_df.LOCATION=="NZL"].index)
            fig2 = px.histogram(filtered_df, x="TIME", y="Value", color="LOCATION", labels={'TIME':'Année', 'Value':"Ecart salarial femmes-hommes (%)"},
                               hover_name="PAYS",
                               hover_data=filtered_df.columns)
        else:
            #Mise à jour de la carte si aucun pays n'a été sélectionné (montre alors tous les pays disponibles)
            if selected_countries==[]:
                #filtered_df = filtered_df.drop(filtered_df[filtered_df.TIME==1996].index)
                fig2 = px.histogram(filtered_df, x="TIME", y="Value", color="LOCATION", labels={'TIME':'Année', 'Value':"Ecart salarial femmes-hommes (%)"},
                                   hover_name="PAYS",
                                   hover_data=filtered_df.columns)

            #Mise à jour de la carte en fonction des pays sélectionnés
            else:
                frames = []
                for i in selected_countries:
                    frames.append(filtered_df[filtered_df["LOCATION"]==i])
                filtered_df = pd.concat(frames)

                #Enlève les données qui ne peuvent être comparées (par ex. qu'une seule donnée/pays pour l'année 1975)
                for i in range(filtered_df["TIME"].min(),filtered_df["TIME"].max()+1):
                    if filtered_df.loc[filtered_df["TIME"]==i].shape[0] != len(frames):
                        filtered_df = filtered_df.drop(filtered_df[filtered_df.TIME==i].index)

                fig2 = px.histogram(filtered_df, x="TIME", y="Value", color="LOCATION", labels={'TIME':'Année', 'Value':"Ecart salarial femmes-hommes (%)"},
                                   hover_name="PAYS",
                                   hover_data=df1.columns)

        return fig2
