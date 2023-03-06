from dash import dash, dcc, html, Input, Output
import pandas as pd

data = pd.DataFrame({
    'column-1': ['A', 'A', 'B', 'B', 'C', 'C'],
    'column-2': ['A-X', 'A-Y', 'B-Z', 'B-W', 'C-Y', 'C-Z']
})

# Define the app
app = dash.Dash(__name__)

# Define the layout of the UI
app.layout = html.Div([
    html.H1('Dropdown Example'),
    dcc.Dropdown(
        id='dropdown-1',
        options=[{'label': i, 'value': i} for i in data['column-1'].unique()]
    ),
    dcc.Dropdown(
        id='dropdown-2'
    )
])

# Define the callback function to update dropdown-2
@app.callback(
    Output(component_id='dropdown-2', component_property='options'),
    [Input(component_id='dropdown-1', component_property='value')]
)
def update_dropdown_2(selected_value):
    filtered_data = data[data['column-1'] == selected_value]
    return [{'label': i, 'value': i} for i in filtered_data['column-2'].unique()]

# Launch the app
if __name__ == '__main__':
    app.run_server(debug=True)