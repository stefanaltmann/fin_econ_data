import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('data.csv')

available_series = df['description'].unique()

app.layout = html.Div([
    html.Div([

        html.Div([
            dcc.Dropdown(
                id='series_description',
                options=[{'label': i, 'value': i} for i in available_series],
                value='10Y treasury minus 2Y treasury'
            ),
        ],
        style={'width': '20%', 'display': 'inline-block'}
        ),
    html.Div([
        dcc.Graph(id='graph1')
    ],
    style={'width': '60%', 'display': 'inline-block'}
    )

], style={'columnCount': 1})
])

@app.callback(
    Output('graph1', 'figure'),
    Input('series_description', 'value')
    )


def update_graph(series_description):

    fig = px.line(df[df['description'] == series_description],
                  x='date',
                  y='value',
                  title=series_description)

    fig.update_layout(margin={'l': 40, 'b': 40, 't': 40, 'r': 0}, hovermode='closest')

    fig.update_xaxes(title='date')

    fig.update_yaxes(title=series_description, type='linear')

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)