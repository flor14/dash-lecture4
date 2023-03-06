from dash import dash, dcc, html, Input, Output
import plotly.express as px

colorscales = px.colors.named_colorscales()
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H4('Interactive color scale'),
    html.P("Select your palette:"),
    dcc.Dropdown(
        id='dropdown', 
        options=colorscales,
        value='viridis'
    ),
    dcc.Graph(id="graph"),
])

@app.callback(
    Output("graph", "figure"), 
    Input("dropdown", "value"))
def change_colorscale(scale):
    df = px.data.iris() # replace with your own data source
    fig = px.scatter(
        df, x="sepal_width", y="sepal_length", 
        color="sepal_length", color_continuous_scale=scale)
    return fig
    
app.run_server(debug=True) 