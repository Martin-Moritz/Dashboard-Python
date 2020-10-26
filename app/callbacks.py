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
                                                    labels={"LOCATION":"Pays","TIME":"Année","Value":"Ecart salarial femmes-hommes"},
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

        fig1.update_layout(paper_bgcolor='#DCE8FD', coloraxis={"colorbar":{"ticksuffix":"%"}})

        return fig1, disabled


    @dashapp.callback(
        Output('histogram', 'figure'),
        [Input('selection-pays', 'value'), Input('selection-salarial','value')])
    def update_figure2(selected_countries, selected_salarial):

        #Filtrage des données en fonction du choix salariés ou non-salariés
        if selected_salarial == "SAL":
            filtered_df = df1.loc[df1["SUBJECT"]=="EMPLOYEE"]
        else:
            filtered_df = df1.loc[df1["SUBJECT"]=="SELFEMPLOYED"]

        if selected_salarial != "SAL":

            bins = int(filtered_df["TIME"].max() - filtered_df["TIME"].min())+1

            fig2 = px.histogram(filtered_df, title='Histogramme', x="TIME", y="Value", color="PAYS", labels={'PAYS':'Pays','TIME':'Année', 'Value':"Ecart salarial femmes-hommes"}, template='simple_white', barmode='overlay', opacity=0.5, nbins=bins, range_y=(0,60))
        else:
            #Mise à jour de la carte si aucun pays n'a été sélectionné (montre alors tous les pays disponibles)
            if selected_countries==[]:

                bins = int(filtered_df["TIME"].max() - filtered_df["TIME"].min())+1

                fig2 = px.histogram(filtered_df, title='Histogramme',  x="TIME", y="Value", color="PAYS", labels={'PAYS':'Pays','TIME':'Année', 'Value':"Ecart salarial femmes-hommes"}, template='simple_white', barmode='overlay', opacity=0.5, nbins=bins, range_y=(0,60))

            #Mise à jour de la carte en fonction des pays sélectionnés
            else:
                frames = []
                for i in selected_countries:
                    frames.append(filtered_df[filtered_df["LOCATION"]==i])
                filtered_df = pd.concat(frames)

                bins = int(filtered_df["TIME"].max() - filtered_df["TIME"].min())+1

                fig2 = px.histogram(filtered_df, title='Histogramme',  x="TIME", y="Value", color="PAYS", labels={'PAYS':'Pays','TIME':'Année', 'Value':"Ecart salarial femmes-hommes"}, template='simple_white', barmode='overlay', opacity=0.5, nbins=bins, range_y=(0,60))

        fig2.update_layout(yaxis={'title':{'text':'Ecart salarial femmes-hommes'},"ticksuffix":"%"}, paper_bgcolor='#DCE8FD')

        return fig2


    @dashapp.callback(
        Output('bar-diagram', 'figure'),
        [Input('selection-pays', 'value'), Input('selection-salarial','value'), Input('year-slider','value')])
    def update_figure3(selected_countries, selected_salarial, selected_year):

        #Filtrage des données en fonction du choix salariés ou non-salariés
        if selected_salarial == "SAL":
            filtered_df = df1.loc[df1["SUBJECT"]=="EMPLOYEE"]
        else:
            filtered_df = df1.loc[df1["SUBJECT"]=="SELFEMPLOYED"]

        #Filtrage des données correspondantes à l'année selectionnée sur le slider
        filtered_df = filtered_df.loc[filtered_df["TIME"]==selected_year]

        if selected_salarial != "SAL":
            fig3 = px.histogram(filtered_df, title='Diagramme en barres', x="PAYS", y="Value", color="PAYS", labels={'PAYS':'Pays','TIME':'Année', 'Value':"Ecart salarial femmes-hommes"}, template='simple_white', range_y=(0,60))
        else:
            #Mise à jour de la carte si aucun pays n'a été sélectionné (montre alors tous les pays disponibles)
            if selected_countries==[]:
                fig3 = px.histogram(filtered_df, title='Diagramme en barres', x="PAYS", y="Value", color="PAYS", labels={'PAYS':'Pays','TIME':'Année', 'Value':"Ecart salarial femmes-hommes"}, template='simple_white', range_y=(0,60))

            #Mise à jour de la carte en fonction des pays sélectionnés
            else:
                frames = []
                for i in selected_countries:
                    frames.append(filtered_df[filtered_df["LOCATION"]==i])
                filtered_df = pd.concat(frames)

                fig3 = px.histogram(filtered_df, title='Diagramme en barres', x="PAYS", y="Value", color="PAYS", labels={'PAYS':'Pays','TIME':'Année', 'Value':"Ecart salarial femmes-hommes"}, template='simple_white', range_y=(0,60))


        fig3.update_layout(yaxis={'title':{'text':'Ecart salarial femmes-hommes'},"ticksuffix":"%"}, paper_bgcolor='#DCE8FD')

        return fig3


    @dashapp.callback(
        [Output('year-slider', 'min'), Output('year-slider', 'max'), Output('year-slider', 'marks'), Output('year-slider', 'value')],
        [Input('selection-pays', 'value'), Input('selection-salarial','value')])
    def update_slider(selected_countries, selected_salarial):

        #Filtrage des données en fonction du choix salariés ou non-salariés
        if selected_salarial == "SAL":
            filtered_df = df1.loc[df1["SUBJECT"]=="EMPLOYEE"]
        else:
            filtered_df = df1.loc[df1["SUBJECT"]=="SELFEMPLOYED"]

        if selected_salarial == "SAL":
            if selected_countries!=[]:
                frames = []
                for i in selected_countries:
                    frames.append(filtered_df[filtered_df["LOCATION"]==i])
                filtered_df = pd.concat(frames)

                #Enlève les données qui ne peuvent être comparées (par ex. qu'une seule donnée/pays pour l'année 1975)
                for i in range(filtered_df["TIME"].min(),filtered_df["TIME"].max()+1):
                    if filtered_df.loc[filtered_df["TIME"]==i].shape[0] != len(frames):
                        filtered_df = filtered_df.drop(filtered_df[filtered_df.TIME==i].index)

        #Valeurs min et max du slider mises à jour
        min = filtered_df["TIME"].min()
        max = filtered_df["TIME"].max()

        #Valeurs intermédiaires du slider mises à jour
        a = [i for i in filtered_df["TIME"]]
        marks = {str(i): str(i) for i in a}

        #Mise à jour de l'année sélectionnée sur le Slider
        value = filtered_df["TIME"].min()

        return min, max, marks, value
