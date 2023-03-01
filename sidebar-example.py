import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

app = dash.Dash(__name__, 
                external_stylesheets=[dbc.themes.DARKLY])

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "1rem 1rem",
   # "background-color": "#ff6666",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Sidebar", className="display-4"),
        html.Hr(),
        html.P(
            "A simple sidebar layout", className="lead"
        ),
        dbc.Nav(
            [
              dcc.Dropdown(id='drop',
                options=['option A',
                         'option B',
                         'option C'],
                value='option A',
                placeholder='Select', 
            style={
                'width': '100%'
            })
            ]),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(style=CONTENT_STYLE)

app.layout = html.Div([sidebar, content])

if __name__ == "__main__":
    app.run_server(debug = True)