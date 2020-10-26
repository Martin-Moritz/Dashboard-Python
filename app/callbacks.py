import dash
from dash.dependencies import *

from .data import *
from .figures import *

#Callbacks pour rafraichir et mettre à jour les différentes figures et composants
def register_callbacks(dashapp):
    @dashapp.callback(
        Output('mapbox', 'figure'),
        [Input('selection-pays', 'value'), Input('selection-salarial','value')])
    def update_carte(selected_countries, selected_salarial):
        """
        Retourne une carte choroplèthe.

        Parameters:
            selected_countries : list of str
            selected_salarial : str

        Returns:
            Return type : plotly.graph_objects.Figure
        """

        #focus de la carte
        focus = 'world'

        #Filtrage des données en fonction du choix salariés ou non-salariés
        if selected_salarial == "SAL":
            filtered_df = df1.loc[df1["SUBJECT"]=="EMPLOYEE"]
        else:
            filtered_df = df1.loc[df1["SUBJECT"]=="SELFEMPLOYED"]

        if selected_salarial == "SAL":
            if selected_countries==[]:
                filtered_df = filtered_df.drop(filtered_df[filtered_df.TIME==1996].index)

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

                #Enlève les données qui ne peuvent pas être comparées (par ex. qu'une seule donnée/pays pour l'année 1996)
                for i in range(filtered_df["TIME"].min(),filtered_df["TIME"].max()+1):
                    if filtered_df.loc[filtered_df["TIME"]==i].shape[0] != len(frames):
                        filtered_df = filtered_df.drop(filtered_df[filtered_df.TIME==i].index)

        #Création de la figure
        carte = create_carte(filtered_df,focus)

        return carte


    @dashapp.callback(
        Output('histogram', 'figure'),
        [Input('selection-pays', 'value'), Input('selection-salarial','value')])
    def update_histogramme(selected_countries, selected_salarial):
        """
        Retourne un histogramme.

        Parameters:
            selected_countries : list of str
            selected_salarial : str

        Returns:
            Return type : plotly.graph_objects.Figure
        """

        #Filtrage des données en fonction du choix salariés ou non-salariés
        if selected_salarial == "SAL":
            filtered_df = df1.loc[df1["SUBJECT"]=="EMPLOYEE"]
        else:
            filtered_df = df1.loc[df1["SUBJECT"]=="SELFEMPLOYED"]

        if selected_salarial == "SAL":
            #Filtrage des données en fonction des pays sélectionnés
            if selected_countries!=[]:
                frames = []
                for i in selected_countries:
                    frames.append(filtered_df[filtered_df["LOCATION"]==i])
                filtered_df = pd.concat(frames)

        #Création de la figure
        histogramme = create_histogramme(filtered_df)

        return histogramme


    @dashapp.callback(
        Output('bar-diagram', 'figure'),
        [Input('selection-pays', 'value'), Input('selection-salarial','value'), Input('year-slider','value')])
    def update_diagramme(selected_countries, selected_salarial, selected_year):
        """
        Retourne un diagramme.

        Parameters:
            selected_countries : list of str
            selected_salarial : str
            selected_year : int

        Returns:
            Return type : plotly.graph_objects.Figure
        """

        #Filtrage des données en fonction du choix salariés ou non-salariés
        if selected_salarial == "SAL":
            filtered_df = df1.loc[df1["SUBJECT"]=="EMPLOYEE"]
        else:
            filtered_df = df1.loc[df1["SUBJECT"]=="SELFEMPLOYED"]

        #Filtrage des données correspondantes à l'année selectionnée sur le slider
        filtered_df = filtered_df.loc[filtered_df["TIME"]==selected_year]

        if selected_salarial == "SAL":
            #Filtrage des données en fonction des pays sélectionnés
            if selected_countries!=[]:
                frames = []
                for i in selected_countries:
                    frames.append(filtered_df[filtered_df["LOCATION"]==i])
                filtered_df = pd.concat(frames)

        #Création de la figure
        diagramme = create_diagramme(filtered_df,str(selected_year))

        return diagramme


    @dashapp.callback(
        [Output('year-slider', 'min'), Output('year-slider', 'max'), Output('year-slider', 'marks'), Output('year-slider', 'value')],
        [Input('selection-pays', 'value'), Input('selection-salarial','value')])
    def update_slider(selected_countries, selected_salarial):
        """
        Retourne 4 paramètres d'un dcc.Slider

        Parameters:
            selected_countries : list of str
            selected_salarial : str

        Returns:
            Return type : int, int, dict, int
        """

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

                #Enlève les données qui ne peuvent pas être comparées (par ex. qu'une seule donnée/pays pour l'année 1996)
                for i in range(filtered_df["TIME"].min(),filtered_df["TIME"].max()+1):
                    if filtered_df.loc[filtered_df["TIME"]==i].shape[0] != len(frames):
                        filtered_df = filtered_df.drop(filtered_df[filtered_df.TIME==i].index)

        #Nouvelles valeurs min et max du slider
        min = filtered_df["TIME"].min()
        max = filtered_df["TIME"].max()

        #Nouvelles marques du slider
        a = [i for i in filtered_df["TIME"]]
        marks = {str(i): str(i) for i in a}

        #Nouvelle année sélectionnée par défaut sur le Slider
        value = filtered_df["TIME"].max()

        return min, max, marks, value


    @dashapp.callback(
        Output('selection-pays', 'disabled'),
        [Input('selection-salarial','value')])
    def update_dropdown(selected_salarial):
        """
        Retourne un paramètre d'un dcc.Dropdown

        Parameters:
            selected_salarial : str

        Returns:
            Return type : bool
        """

        #Activation du menu déroulant selon le choix salariés/non-salariés
        if selected_salarial == "SAL":
            disabled = False
        else:
            disabled = True

        return disabled
