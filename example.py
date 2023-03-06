from dash import dash, dcc, html, Input, Output
import pandas as pd

data = pd.DataFrame({
    'column-1': ['A', 'A', 'B', 'B', 'C', 'C'],
    'column-2': ['A-X', 'A-Y', 'B-Z', 'B-W', 'C-Y', 'C-Z']
})

app = dash.Dash(__name__)

app.layout = html.Div([
  
])

if __name__ == '__main__':
    app.run_server(debug=True)