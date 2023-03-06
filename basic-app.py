from dash import dash, html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__,
                external_stylesheets = [dbc.themes.LUX])

app.layout = html.Div('Hello!')

if __name__ == '__main__':
    app.run_server(debug=True)