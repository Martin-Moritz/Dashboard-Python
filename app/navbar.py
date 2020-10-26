import dash_bootstrap_components as dbc
import dash_html_components as html

logo = "assets/img/logo.png"

items=[
        dbc.DropdownMenuItem("Moritz Martin",href="https://www.linkedin.com/in/martin-moritz-1944731b1",external_link=True),
        dbc.DropdownMenuItem("Rogissart Vincent",href="https://www.linkedin.com/in/vincent-rogissart-20743a1aa/",external_link=True),
        ]

navbar = dbc.Navbar(
    [
        dbc.Col([
            html.A(html.Img(src=logo, height="50px"),href="https://www.esiee.fr/"),
        ], width=4),
        dbc.Col([
            html.H1(
                children='Dashboard Python',
                style={
                    'textAlign': 'center',
                    'color': '#49BBEE',
                    'fontWeight': 'bold'
                }
            ),
        ], width=4),
        dbc.DropdownMenu(items,label="Aide",color="info",className="ml-auto p-2 bd-highlight",in_navbar=True,direction="left"),
    ],
    color="dark",
    dark=True,
)
