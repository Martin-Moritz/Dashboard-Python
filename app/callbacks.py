import dash
from dash.dependencies import *

from .data import *
from .figures import *


def register_callbacks(dashapp):
    @dashapp.callback(
        Output('mapbox', 'figure'),
        [Input('selection-pays', 'value')])
    def update_figure(selected_country):

        #df1_2016 = df1.loc[(df1["TIME"]==2016) & (df1["SUBJECT"]=="EMPLOYEE")]
        df1_emp = df1.loc[df1["SUBJECT"]=="EMPLOYEE"]

        frames = []

        if selected_country==[]:
            filtered_df = df1_emp
            fig1 = px.choropleth(filtered_df, locations="LOCATION", color="Value",
                                                color_continuous_scale="Jet",
                                                range_color=(0,50),
                                                scope="world",
                                                labels={"LOCATION":"Pays","TIME":"Année","Value":"Pourcentage d'écart de salaire homme-femme"},
                                                template = "plotly_dark",
                                                animation_frame="TIME",
                                                title="Carte",
                                                height= 700)

        else:
            for i in selected_country:
                frames.append(df1_emp[df1_emp["LOCATION"]==i])
            filtered_df = pd.concat(frames)

            fig1 = px.choropleth(filtered_df,locations="LOCATION", color="Value",
                                                color_continuous_scale="Jet",
                                                range_color=(0,50),
                                                scope="world",
                                                labels={"LOCATION":"Pays","TIME":"Année","Value":"Pourcentage d'écart de salaire homme-femme"},
                                                template = "plotly_dark",
                                                animation_frame="TIME",
                                                title="Carte",
                                                height=700)

        return fig1
