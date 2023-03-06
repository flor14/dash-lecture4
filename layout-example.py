from dash import dash, html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.MINTY])

row = html.Div(
    [
        dbc.Row(
            dbc.Col(
                html.Div("A single, half-width column", 
                         style = {'background-color':'yellow'}),
                width={"size": 6, "offset": 3},
            )
        ),
        dbc.Row(
            [
                dbc.Col(
                    html.Div("The last of three columns"),
                    width={"size": 3, "order": "last", "offset": 1},
                ),
                dbc.Col(
                    html.Div("The first of three columns", style = {'background-color':'green'}),
                    width={"size": 4, "order": 1, "offset": 2},
                ),
                dbc.Col(
                    html.Div("The second of three columns"),
                    width={"size": 3, "order": 5},
                ),
            ]
        ),
    ]
)

app.layout = dbc.Container([
    row
])

if __name__ == '__main__':
    app.run_server(debug=True)