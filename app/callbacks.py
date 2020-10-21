import dash
from dash.dependencies import *

from .data import *
from .figures import *


def register_callbacks(dashapp):
    @dashapp.callback(
        Output('mapbox', 'figure'),
        [Input('selection-pays', 'value')])
    def update_figure(selected_countries):

        focus = 'world'

        filtered_df = df1.loc[df1["SUBJECT"]=="EMPLOYEE"]

        if selected_countries==[]:
            filtered_df = filtered_df.drop(df1[df1.TIME==1996].index)
            fig1 = px.choropleth(filtered_df, locations="LOCATION", color="Value",
                                                color_continuous_scale="Jet",
                                                range_color=(0,50),
                                                scope=focus,
                                                labels={"LOCATION":"Pays","TIME":"Année","Value":"Ecart salarial femmes-hommes (%)"},
                                                template = "plotly_dark",
                                                animation_frame="TIME",
                                                title="Carte",
                                                height= 700)

        else:
            frames = []
            for i in selected_countries:
                frames.append(filtered_df[filtered_df["LOCATION"]==i])
            filtered_df = pd.concat(frames)

            #AJOUTER UN FOCUS APPROPRIE SELON LES PAYS SELECTIONNES
            """if len(selected_countries)==1:
                focus='asia'
            """
            for i in range(filtered_df["TIME"].min(),filtered_df["TIME"].max()+1):
                if filtered_df.loc[filtered_df["TIME"]==i].shape[0] != len(frames):
                    filtered_df = filtered_df.drop(filtered_df[filtered_df.TIME==i].index)

            fig1 = px.choropleth(filtered_df,locations="LOCATION", color="Value",
                                                color_continuous_scale="Jet",
                                                range_color=(0,50),
                                                scope=focus,
                                                labels={"LOCATION":"Pays","TIME":"Année","Value":"Ecart salarial femmes-hommes (%)"},
                                                template = "plotly_dark",
                                                animation_frame="TIME",
                                                title="Carte",
                                                height=700)

        return fig1
