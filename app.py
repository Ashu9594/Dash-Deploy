from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# Initialize the app
app = Dash(__name__)
server = app.server  # Need this for Render deployment

# Create some sample data
df = pd.DataFrame({
    'Fruit': ['Apples', 'Oranges', 'Bananas', 'Apples', 'Oranges', 'Bananas'],
    'Amount': [4, 1, 2, 2, 4, 5],
    'City': ['SF', 'SF', 'SF', 'NYC', 'NYC', 'NYC']
})

# Create a bar chart
fig = px.bar(df, x='Fruit', y='Amount', color='City', barmode='group')

# Define the app layout
app.layout = html.Div(children=[
    html.H1(children='My First Dash App'),
    
    html.Div(children='''
        A simple example of a Dash app deployed on Render.
    '''),
    
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

# Add this for deployment
if __name__ == '__main__':
    app.run_server(debug=False, host='0.0.0.0')