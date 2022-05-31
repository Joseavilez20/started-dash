
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
# from views import graph_test

# myCuttyGraph = dcc.Graph(
#         id='example-graph2',
#         figure=graph_test.fig
#     )

container= dbc.Container(
                id='container_test',
                children=[
                    dcc.Location(id='test-url',pathname='/test'),
                    html.H1("Masivo Capital", className="display-5 mt-2"),
                    html.P(
                    "Here testing,"
                    "optimization of fleet allocation for passenger mobilization.",
                    className="lead",
                    ),
                html.Img(src="/assets/datascience.png", height="70px"),
                # html.Div(myCuttyGraph)
                         ]
)