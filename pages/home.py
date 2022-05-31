
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
container= dbc.Container(
                id='container_home',
                children=[
                    dcc.Location(id='home-url',pathname='/home'),
                    html.H1("Masivo Capital", className="display-5 mt-2"),
                    html.P(
                    "Monitoring the performance of operators on the road,"
                    "optimization of fleet allocation for passenger mobilization.",
                    className="lead",
                )
                         ]
)