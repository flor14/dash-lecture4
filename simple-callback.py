from dash import dash, html, dcc, Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='widget-1'),
    dcc.Textarea(id='widget-2')])

@app.callback(
    Output('widget-2', 'value'),
    Input('widget-1', 'value'))
def update_output(input_value):
    return input_value

if __name__ == '__main__':
    app.run_server(debug=True) 